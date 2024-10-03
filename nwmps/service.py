import shapely.wkt
import shapely

from .utilities import (
    _to_2d,
    get_service_layers,
    DATA_SERVICES,
    SERVICES_DROPDOWN,
    LAYERS,
    BASEMAP_LAYERS_DROPDOWN,
)

from geoalchemy2 import WKTElement
import shapely
from pynhd import NHDPlusHR
from pygeoogc import ArcGISRESTful
import pygeoutils as geoutils
from pygeohydro import WBD
from intake.source import base
import requests


class NWMPService(base.DataSource):
    container = "python"
    version = "0.0.1"
    name = "nwmp_data_service"
    visualization_args = {
        # at the end some sort of json containing the map with the layers needed: on this case the HUCs boundaries, and base map of interest
        # by default the map will have the controllers to turn on and off layers
        # should be something like click on the map, then select huc (only one), then make a vector layer to show the boundary
        "huc_id": ["0202"],
        "service_and_layer_id": SERVICES_DROPDOWN,
    }
    visualization_group = "NWMP"
    visualization_label = "NWMP Data Service"
    visualization_type = "card"

    def __init__(self, service_and_layer_id, huc_id, metadata=None):
        # store important kwargs
        self.BASE_URL = "https://maps.water.noaa.gov/server/rest/services/nwm"
        self.service = service_and_layer_id.split("-")[0]
        self.layer_id = service_and_layer_id.split("-")[1]
        self.huc_level = f"huc{len(str(huc_id))}"
        self.huc_id = huc_id
        self.layer_info = self.get_layer_info()
        self.geom = None

        super(NWMPService, self).__init__(metadata=metadata)

    def read(self):
        """Return a version of the xarray with all the data in memory"""
        print("Reading data from NWMP service")
        print(f"Service: {self.BASE_URL}/{self.service}/MapServer")
        print(f"Layer ID: {self.layer_id}")
        print(f"HUC Level: {self.huc_level}")
        print(f"HUC IDs: {self.huc_id}")
        service_url = f"{self.BASE_URL}/{self.service}/MapServer"
        self.geom = self.get_huc_boundary(self.huc_level, self.huc_id)
        df = self.getDfRiverFeaturesFromService(service_url, self.layer_id, self.geom)
        df = self.add_symbols(df)
        stats_json = self.getStatisticsFromService(df)
        title = self.make_title()
        description = self.make_description()
        stats = self.getStatisticsFromService2(df)

        # return {"title": title, "data": stats_json}
        return {"title": title, "data": stats, "description": description}

    def make_title(self):
        service_name = self.layer_info.get("name")
        return service_name

    def make_description(self):
        description = self.get_service_info().get("serviceDescription").split("\n")[0]
        return description

    def get_service_info(self):
        service_url = f"{self.BASE_URL}/{self.service}/MapServer"
        response = requests.get(f"{service_url}?f=json")
        return response.json()

    def get_layer_info(self):
        layer_url = f"{self.BASE_URL}/{self.service}/MapServer/{self.layer_id}"
        response = requests.get(f"{layer_url}?f=json")
        return response.json()

    def get_drawing_info(self):
        layer_info = self.layer_info
        drawing_info = (
            layer_info.get("drawingInfo").get("renderer").get("uniqueValueInfos")
        )
        return drawing_info

    # Define a function to get the label and color based on recur_cat
    def get_label_and_color(self, filter_attr, symbol_dict):
        match = symbol_dict.get(filter_attr, None)
        if match:
            return match["label"], match["symbol"]["color"]
        return None, None

    def rgb_to_hex(self, r, g, b):
        return "#{:02x}{:02x}{:02x}".format(r, g, b)

    def add_symbols_info_df(self, df, symbols, filter_attr):
        # Convert the symbol list to a dictionary for quick lookup
        symbol_dict = {item["value"]: item for item in symbols}
        # Apply the function to each row in the DataFrame using a lambda function to pass symbol_dict
        df["label"], df["color"] = zip(
            *df[filter_attr].apply(lambda x: self.get_label_and_color(x, symbol_dict))
        )
        df["hex"] = df["color"].apply(lambda x: self.rgb_to_hex(x[0], x[1], x[2]))

        return df

    def add_symbols(self, df):
        filter_attr = self.get_color_attribute()
        symbols = self.get_drawing_info()
        df = self.add_symbols_info_df(df, symbols, filter_attr)
        return df

    def get_color_attribute(self):
        attr_name = (
            DATA_SERVICES[self.service]
            .get("layers")[int(self.layer_id)]
            .get("filter_attr")
        )
        return attr_name

    def get_huc_boundary(self, huc_level, huc_id):
        """
        Retrieve the watershed boundary geometry for a given HUC code.

        Parameters:
            huc_code (str): The Hydrologic Unit Code of the watershed.

        Returns:
            geopandas.GeoDataFrame: A GeoDataFrame containing the watershed boundary geometry.
        """
        wbd = WBD(huc_level)
        gdf = wbd.byids(huc_level, huc_id)
        return gdf["geometry"][0]

    def getDfRiverFeaturesFromService(self, url, layer_id, geom):
        hr = ArcGISRESTful(url, layer_id)
        resp = hr.get_features(
            hr.oids_bygeom(geom, spatial_relation="esriSpatialRelContains")
        )
        df = geoutils.json2geodf(resp)
        return df

    def getDfRiverIDsFromHUC(geom):
        # mr = WaterData("nhdflowline_network")
        mr = NHDPlusHR("flowline")
        try:
            nhdp_mr = mr.bygeom(geom)
        except Exception as e:
            print(e)

        nhdp_mr["geometry"] = nhdp_mr["geometry"].apply(
            lambda geom: shapely.ops.transform(_to_2d, geom)
        )
        nhdp_mr = nhdp_mr.explode(index_parts=False)
        nhdp_mr["geometry"] = nhdp_mr["geometry"].apply(
            lambda x: WKTElement(x.wkt, srid=4326)
        )
        return nhdp_mr

    def getTotalRiverIdsFromGeom(geom):
        mr = NHDPlusHR("flowline")
        try:
            nhdp_mr = mr.bygeom(geom)

        except Exception as e:
            print(e)

    def getStatisticsFromService(self, df):
        # filter_attr = self.get_color_attribute()
        # print(filter_attr)
        counts = df["label"].value_counts()
        counts_list = [
            counts.to_dict()
        ]  # this is a hack to make it work with the current implementation on react
        return counts_list

    def getStatisticsFromService2(self, df):
        dfg = df.groupby(by=["label", "hex"], as_index=False).size()
        stats = dfg.to_dict("records")
        print(stats)
        return stats
