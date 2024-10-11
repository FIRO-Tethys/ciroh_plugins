import requests
import pandas as pd
from shapely.geometry import MultiPolygon
from pygeoogc import ArcGISRESTful
import pygeoutils as geoutils
from pygeoogc.exceptions import ZeroMatchedError
from pygeohydro import WBD
from intake.source import base
from .utilities import get_services_dropdown, DATA_SERVICES
import numpy as np


class NWMPService(base.DataSource):
    """
    A data source class for NWMP services, extending Intake's DataSource.
    """

    container = "python"
    version = "0.0.1"
    name = "nwmp_data_service"
    visualization_args = {
        "huc_id": "text",
        "service_and_layer_id": get_services_dropdown(),
    }
    visualization_group = "NWMP"
    visualization_label = "NWMP Data Service"
    visualization_type = "card"

    def __init__(self, service_and_layer_id, huc_id, metadata=None):
        """
        Initialize the NWMPService data source.
        """
        super().__init__(metadata=metadata)
        parts = service_and_layer_id.split("/")
        self.service = parts[-3]
        self.layer_id = int(parts[-1])
        self.BASE_URL = "/".join(parts[:-3])
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
        print(f"HUC IDs: {self.huc_id}")
        service_url = f"{self.BASE_URL}/{self.service}/MapServer"
        self.title = self.make_title()
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
        }

    def make_title(self):
        """Create a title for the data."""
        return self.layer_info.get("name", "NWMP Data")

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
        drawing_attr = self.get_drawing_info_attr(self.service, self.layer_id)
        drawings = renderer.get(drawing_attr, {})
        return drawings

    @staticmethod
    def get_drawing_info_attr(service_name, layer_id):
        service = DATA_SERVICES.get(service_name)
        if not service:
            return None

        layers = service.get("layers", [])
        for layer in layers:
            if layer.get("id") == layer_id:
                return layer.get("drawingInfoAttr")

        return None

    @staticmethod
    def get_drawing_info_value_attr(service_name, layer_id):
        service = DATA_SERVICES.get(service_name)
        if not service:
            return None

        layers = service.get("layers", [])
        for layer in layers:
            if layer.get("id") == layer_id:
                return layer.get("drawingInfoValueAttr")
        return None

    @staticmethod
    def rgb_to_hex(rgb_color):
        """Convert RGB color to hex color code."""
        if rgb_color and len(rgb_color) >= 3:
            return "#{:02x}{:02x}{:02x}".format(*rgb_color[:3])
        return "#000000"

    # Define a function to get the label and color based on recur_cat
    def get_label_and_color_for_value(self, filter_attr, symbol_dict):
        # breakpoint()

        match = symbol_dict.get(filter_attr, None)
        if match:
            return match["label"], match["symbol"]["color"]
        return None, None

    def add_symbols_info(self, df, symbols, filter_attr):
        drawing_info_val_attr = self.get_drawing_info_value_attr(
            self.service, self.layer_id
        )
        if drawing_info_val_attr == "value":
            df = self.assign_labels_and_colors_based_on_value(df, symbols, filter_attr)
        else:
            df = self.assign_labels_and_colors_based_on_range(df, filter_attr, symbols)
        return df

    def assign_labels_and_colors_based_on_value(self, df, symbol_list, filter_attr):
        symbol_dict = {str(item["value"]): item for item in symbol_list}
        df["label"], df["color"] = zip(
            *df[filter_attr].apply(
                lambda x: self.get_label_and_color_for_value(str(x), symbol_dict)
            )
        )

        df["hex"] = df["color"].apply(lambda x: self.rgb_to_hex(x))
        return df

    def assign_labels_and_colors_based_on_range(
        self,
        df,
        value_column,
        symbol_list,
        label_column="label",
        color_column="hex",
    ):
        """
        Assign labels and colors to a DataFrame based on a value column and a symbol list.

        Parameters:
        - df: pandas.DataFrame
            The DataFrame containing the values to categorize.
        - value_column: str
            The name of the column in df containing the values to categorize.
        - symbol_list: list of dicts
            The list of symbols containing classMaxValue, label, and color information.
        - label_column: str, optional (default='label')
            The name of the column to be created for labels.
        - color_column: str, optional (default='color')
            The name of the column to be created for colors.
        - hex_color_column: str, optional (default='color_hex')
            The name of the column to be created for hex color codes.

        Returns:
        - df: pandas.DataFrame
            The DataFrame with new columns added for labels and colors.
        """
        # breakpoint()
        # Step 1: Extract bins, labels, and colors from the symbol_list
        bins = [0] + [item["classMaxValue"] for item in symbol_list[:-1]] + [np.inf]
        labels = [item["label"] for item in symbol_list]
        colors = [item["symbol"]["color"] for item in symbol_list]

        # Create a mapping from labels to colors
        label_to_color = dict(zip(labels, colors))

        # Ensure that the value_column is numeric
        df[value_column] = pd.to_numeric(df[value_column], errors="coerce")

        # Step 2: Use pandas.cut to assign labels based on bins
        df[label_column] = pd.cut(
            df[value_column], bins=bins, labels=labels, right=True, include_lowest=True
        )

        # Step 3: Map the labels to colors to create the color column
        label_to_color_hex = {
            label: self.rgb_to_hex(color) for label, color in label_to_color.items()
        }
        df[color_column] = df[label_column].map(label_to_color_hex)
        # breakpoint()
        return df

    def add_symbols(self, df):
        """Add symbols to the DataFrame."""
        # breakpoint()
        filter_attr = self.get_color_attribute()
        # breakpoint()
        symbols = self.get_drawing_info()
        # print(symbols)
        if not symbols:
            print("No drawing symbols found.")
            return df
        # print(df)
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
        dfs = []
        geometries = (
            geometry.geoms if isinstance(geometry, MultiPolygon) else [geometry]
        )
        # Optionally, remove debug prints or breakpoint in production
        # breakpoint()
        for geom in geometries:
            try:
                oids = hr.oids_bygeom(geom, spatial_relation="esriSpatialRelContains")
                if oids:
                    resp = hr.get_features(oids)
                    df_temp = geoutils.json2geodf(resp)
                    dfs.append(df_temp)
                else:
                    print("No OIDs found for the geometry.")
            except ZeroMatchedError:
                print("ZeroMatchedError: No features found within the given geometry.")
                continue  # Skip to the next geometry
            except Exception as e:
                print(f"Error fetching features for a geometry: {e}")
                continue  # Optionally continue or handle differently
        if dfs:
            df = pd.concat(dfs, ignore_index=True)
            return df
        else:
            print("No river features found in any of the geometries.")
            return pd.DataFrame()

    def get_statistics(self, df):
        """Compute statistics from the DataFrame."""

        grouped = df.groupby(by=["label", "hex"], as_index=False).size()
        grouped = grouped[grouped["size"] > 0].reset_index(drop=True)  # tmp fix
        stats = grouped.to_dict("records")
        return stats
