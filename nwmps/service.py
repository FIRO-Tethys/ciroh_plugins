import requests
import pandas as pd
from shapely.geometry import MultiPolygon
from pynhd import NHDPlusHR
from pygeoogc import ArcGISRESTful
import pygeoutils as geoutils
from pygeoogc.exceptions import ZeroMatchedError
from pygeohydro import WBD
from intake.source import base
from .utilities import _to_2d, DATA_SERVICES, SERVICES_DROPDOWN


class NWMPService(base.DataSource):
    """
    A data source class for NWMP services, extending Intake's DataSource.
    """

    container = "python"
    version = "0.0.1"
    name = "nwmp_data_service"
    visualization_args = {
        "huc_id": "0202",
        "service_and_layer_id": SERVICES_DROPDOWN,
    }
    visualization_group = "NWMP"
    visualization_label = "NWMP Data Service"
    visualization_type = "card"
    BASE_URL = "https://maps.water.noaa.gov/server/rest/services/nwm"

    def __init__(self, service_and_layer_id, huc_id, metadata=None):
        """
        Initialize the NWMPService data source.
        """
        super().__init__(metadata=metadata)
        parts = service_and_layer_id.split("-")
        if len(parts) != 2:
            raise ValueError(
                "service_and_layer_id must be in 'service-layer_id' format"
            )
        self.service = parts[0]
        self.layer_id = int(parts[1])
        self.huc_level = f"huc{len(str(huc_id))}"
        self.huc_id = huc_id
        self.layer_info = self.get_layer_info()
        self.title = None
        self.description = None

    def read(self):
        """
        Read data from NWMP service and return a dictionary with title, data, and description.
        """
        print("Reading data from NWMP service")
        print(f"Service: {self.BASE_URL}/{self.service}/MapServer")
        print(f"Layer ID: {self.layer_id}")
        print(f"HUC Level: {self.huc_level}")
        print(f"HUC IDs: {self.huc_id}")
        service_url = f"{self.BASE_URL}/{self.service}/MapServer"
        self.title = self.make_title()
        self.description = self.make_description()
        geometry = self.get_huc_boundary()
        if geometry is None:
            df = pd.DataFrame()
        else:
            df = self.get_river_features(service_url, geometry)

        if not df.empty:
            df = self.add_symbols(df)
            stats = self.get_statistics(df)
        else:
            stats = {}

        return {
            "title": self.title,
            "data": stats,
            "description": self.description,
        }

    def make_title(self):
        """Create a title for the data."""
        return self.layer_info.get("name", "NWMP Data")

    def make_description(self):
        """Create a description for the data."""
        service_info = self.get_service_info()
        description = service_info.get("serviceDescription", "")
        return description.split("\n")[0] if description else ""

    def get_service_info(self):
        """Retrieve service information from the NWMP service."""
        service_url = f"{self.BASE_URL}/{self.service}/MapServer"
        try:
            response = requests.get(f"{service_url}?f=json")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching service info: {e}")
            return {}

    def get_layer_info(self):
        """Retrieve layer information from the NWMP service."""
        layer_url = f"{self.BASE_URL}/{self.service}/MapServer/{self.layer_id}"
        try:
            response = requests.get(f"{layer_url}?f=json")
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"Error fetching layer info: {e}")
            return {}

    def get_drawing_info(self):
        """Extract drawing information from layer info."""
        renderer = self.layer_info.get("drawingInfo", {}).get("renderer", {})
        return renderer.get("uniqueValueInfos", [])

    def get_label_and_color(self, attribute_value, symbol_dict):
        """Get label and color for a given attribute value."""
        match = symbol_dict.get(attribute_value)
        if match:
            symbol = match.get("symbol", {})
            color = symbol.get("color", [])
            label = match.get("label", "")
            return label, color
        return None, None

    @staticmethod
    def rgb_to_hex(rgb_color):
        """Convert RGB color to hex color code."""
        if rgb_color and len(rgb_color) >= 3:
            return "#{:02x}{:02x}{:02x}".format(*rgb_color[:3])
        return "#000000"

    def add_symbols_info(self, df, symbols, filter_attr):
        """Add symbol information to the DataFrame."""
        # Convert the symbol list to a dictionary for quick lookup
        symbol_dict = {item["value"]: item for item in symbols}

        # Apply the function to each row in the DataFrame
        def extract_label_color(value):
            label, color = self.get_label_and_color(value, symbol_dict)
            hex_color = self.rgb_to_hex(color)
            return pd.Series({"label": label, "hex": hex_color})

        df[["label", "hex"]] = df[filter_attr].apply(extract_label_color)
        return df

    def add_symbols(self, df):
        """Add symbols to the DataFrame."""
        filter_attr = self.get_color_attribute()
        symbols = self.get_drawing_info()
        if not symbols:
            print("No drawing symbols found.")
            return df
        df = self.add_symbols_info(df, symbols, filter_attr)
        return df

    def get_color_attribute(self):
        """Get the attribute name used for coloring."""
        service_info = DATA_SERVICES.get(self.service, {})
        layers = service_info.get("layers", [])
        layer_info = next(
            (layer for layer in layers if layer.get("id") == self.layer_id), {}
        )
        attr_name = layer_info.get("filter_attr")
        if not attr_name:
            print(f"No filter attribute found for layer ID {self.layer_id}")
        return attr_name

    def get_huc_boundary(self):
        """
        Retrieve the watershed boundary geometry for a given HUC code.

        Returns:
            shapely.geometry: The geometry of the HUC boundary, or None if not found.
        """
        wbd = WBD(self.huc_level)
        try:
            gdf = wbd.byids(self.huc_level, self.huc_id)
            return gdf.iloc[0]["geometry"]
        except ZeroMatchedError:
            print(f"No HUC boundary found for HUC ID {self.huc_id}")
            return None
        except Exception as e:
            print(f"Error fetching HUC boundary: {e}")
            return None

    def get_river_features(self, url, geometry):
        """Fetch river features from the service within the given geometry."""
        hr = ArcGISRESTful(url, self.layer_id)
        try:
            dfs = []
            geometries = (
                geometry.geoms if isinstance(geometry, MultiPolygon) else [geometry]
            )
            for geom in geometries:
                oids = hr.oids_bygeom(geom, spatial_relation="esriSpatialRelContains")
                if oids:
                    resp = hr.get_features(oids)
                    df_temp = geoutils.json2geodf(resp)
                    dfs.append(df_temp)
            if dfs:
                df = pd.concat(dfs, ignore_index=True)
                return df
            else:
                return pd.DataFrame()
        except ZeroMatchedError:
            print("No river features found within the given geometry.")
            return pd.DataFrame()
        except Exception as e:
            print(f"Error fetching river features: {e}")
            return pd.DataFrame()

    def get_statistics(self, df):
        """Compute statistics from the DataFrame."""
        grouped = df.groupby(by=["label", "hex"], as_index=False).size()
        stats = grouped.to_dict("records")
        return stats
