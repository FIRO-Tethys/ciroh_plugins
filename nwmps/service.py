import pandas as pd
import json
import io
import geopandas as gpd
import shapely.wkt
import shapely

from .utilities import _to_2d, DATA_SERVICES

from geoalchemy2 import WKTElement
import shapely
import pandas as pd
from pynhd import NHDPlusHR
from pygeoogc import ArcGISRESTful
import pygeoutils as geoutils

from intake.source import base


class NWMPService(base.DataSource):
    container = "python"
    version = "0.0.1"
    name = "nwmp_data_service"
    visualization_args = {}
    visualization_group = "NWMP"
    visualization_label = "NWMP Data Service"
    visualization_type = "table"

    def __init__(self, service, layer_id, geom, metadata=None):
        # store important kwargs
        self.BASE_URL = "https://maps.water.noaa.gov/server/rest/services/nwm"
        self.service = service
        self.layer_id = layer_id
        self.geom = geom

        super(NWMPService, self).__init__(metadata=metadata)

    def read(self):
        """Return a version of the xarray with all the data in memory"""
        service_url = f"{self.BASE_URL}/{self.service}"
        df = self.getDfRiverFeaturesFromService(service_url, self.layer_id, self.geom)
        stats_json = self.getStatisticsFromService(df)
        return {"data": stats_json}

    def get_color_attribute(self):
        attr_name = (
            DATA_SERVICES[self.service].get("layers")[self.layer_id].get("filter_attr")
        )
        return attr_name

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
        filter_attr = self.get_color_attribute()
        counts = df[filter_attr].value_counts()
        return counts.to_json()
