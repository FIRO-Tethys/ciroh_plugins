import shapely.wkt
import shapely

from .utilities import (
    _to_2d,
    get_service_layers,
    DATA_SERVICES,
    SERVICES_DROPDOWN,
    LAYERS,
)

from geoalchemy2 import WKTElement
import shapely
from pynhd import NHDPlusHR
from pygeoogc import ArcGISRESTful
import pygeoutils as geoutils
from pygeohydro import WBD

from intake.source import base


class NWMPService(base.DataSource):
    container = "python"
    version = "0.0.1"
    name = "nwmp_data_service"
    visualization_args = {
        # at the end some sort of json containing the map with the layers needed: on this case the HUCs boundaries, and base map of interest
        # by default the map will have the controllers to turn on and off layers
        # should be something like click on the map, then select huc (only one), then make a vector layer to show the boundary
        # "plugin": LAYERS,
        "huc_level": ["huc4"],
        "huc_ids": ["0201", "0202"],  # this input needs to depend on the huc_level
        "service_and_layer_id": SERVICES_DROPDOWN,
    }
    visualization_group = "NWMP"
    visualization_label = "NWMP Data Service"
    visualization_type = "card"

    def __init__(self, service_and_layer_id, huc_level, huc_ids, metadata=None):
        # store important kwargs
        self.BASE_URL = "https://maps.water.noaa.gov/server/rest/services/nwm"
        self.service = service_and_layer_id.split("-")[0]
        self.layer_id = service_and_layer_id.split("-")[1]
        self.huc_level = huc_level
        self.huc_ids = huc_ids
        self.geom = None

        super(NWMPService, self).__init__(metadata=metadata)

    def read(self):
        """Return a version of the xarray with all the data in memory"""
        print("Reading data from NWMP service")
        print(f"Service: {self.BASE_URL}/{self.service}/MapServer")
        print(f"Layer ID: {self.layer_id}")
        print(f"HUC Level: {self.huc_level}")
        print(f"HUC IDs: {self.huc_ids}")
        service_url = f"{self.BASE_URL}/{self.service}/MapServer"
        self.geom = self.get_huc_boundary(self.huc_level, self.huc_ids)
        df = self.getDfRiverFeaturesFromService(service_url, self.layer_id, self.geom)
        stats_json = self.getStatisticsFromService(df)
        return {"title": self.service, "data": stats_json}

    def get_color_attribute(self):
        attr_name = (
            DATA_SERVICES[self.service]
            .get("layers")[int(self.layer_id)]
            .get("filter_attr")
        )
        return attr_name

    def get_huc_boundary(self, huc_level, huc_ids):
        """
        Retrieve the watershed boundary geometry for a given HUC code.

        Parameters:
            huc_code (str): The Hydrologic Unit Code of the watershed.

        Returns:
            geopandas.GeoDataFrame: A GeoDataFrame containing the watershed boundary geometry.
        """
        wbd = WBD(huc_level)
        gdf = wbd.byids(huc_level, huc_ids)
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
        print("statisitcs")
        filter_attr = self.get_color_attribute()
        print(filter_attr)
        counts = df[filter_attr].value_counts()
        counts_list = [
            counts.to_dict()
        ]  # this is a hack to make it work with the current implementation on react
        return counts_list
