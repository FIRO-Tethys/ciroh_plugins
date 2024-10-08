from .utilities import (
    DATA_SERVICES,
    SERVICES_DROPDOWN,
    BASEMAP_LAYERS_DROPDOWN,
    HUC_LAYER,
)

from intake.source import base
from shapely.geometry import Point, LineString, Polygon

# from arcgis.geometry import Geometry
import json
from pyproj import Transformer

import requests


class MapVisualization(base.DataSource):
    container = "python"
    version = "0.0.1"
    name = "nwmp_map"
    visualization_args = {
        "basemap_layer": BASEMAP_LAYERS_DROPDOWN,
        "services": SERVICES_DROPDOWN,
        "huc_id": "text",
    }
    visualization_group = "NWMP"
    visualization_label = "NWMP Map"
    visualization_type = "map"

    def __init__(self, basemap_layer, services, huc_id, metadata=None):
        # store important kwargs
        self.BASE_URL = "https://maps.water.noaa.gov/server/rest/services/nwm"
        self.huc_id = huc_id
        self.service = services.split("-")[0]
        self.layer_id = services.split("-")[1]
        self.basemap_layer = self.get_esri_base_layer_dict(basemap_layer)
        self.service_layer = self.get_service_layer_dict()

        self.layer_huc = None  # self.make_huc_vector_layer()
        self.view = self.get_view_config(center=[-110.875, 37.345], zoom=5)
        super(MapVisualization, self).__init__(metadata=metadata)

    def read(self):
        """Return a version of the xarray with all the data in memory"""
        layers = [self.basemap_layer, HUC_LAYER, self.service_layer]
        if self.layer_huc is not None:
            layers = [self.basemap_layer, HUC_LAYER, self.layer_huc, self.service_layer]
        return {
            "layers": layers,
            "view_config": self.view,
        }

    def get_service_layers(self):
        result = []
        for service_value in DATA_SERVICES.items():
            service_dict = {
                "name": service_value["name"],
                "layers": [
                    {"name": layer["name"], "id": layer["id"]}
                    for layer in service_value["layers"]
                ],
            }
            result.append(service_dict)
        return result

    def make_huc_vector_layer(self):
        huc_level = f"huc{len(str(self.huc_id))}"
        service_url = f"https://hydro.nationalmap.gov/arcgis/rest/services/wbd/MapServer/{int(len(str(self.huc_id))/2)}/query"
        payload = {"where": f"{huc_level} = '{self.huc_id}'", "f": "geojson"}
        rr = requests.get(service_url, params=payload)
        if rr.status_code != 200:
            return None
        # breakpoint()
        layer_dict = {}
        layer_dict["type"] = "VectorLayer"
        layer_dict["props"] = {
            "source": {
                "type": "Vector",
                "props": {
                    "url": rr.url,
                    "format": {"type": "GeoJSON"},
                },
            },
            "name": "huc_vector_selection",
        }
        return layer_dict

    def get_service_layer_dict(self):
        service_url = f"{self.BASE_URL}/{self.service}/MapServer"
        layer_dict = {}
        layer_dict["type"] = "ImageLayer"
        layer_dict["props"] = {
            "source": {
                "type": "ImageArcGISRest",
                "props": {
                    "url": service_url,
                    "params": {"LAYERS": f"show:{self.layer_id}"},
                },
            },
            "name": f'{self.service.replace("_"," ")}',
        }
        return layer_dict

    def get_esri_base_layer_dict(self, basemap_layer):
        layer_dict = {}
        layer_dict["type"] = "WebGLTile"
        layer_dict["props"] = {
            "source": {
                "type": "ImageTile",
                "props": {
                    "url": f"{basemap_layer}/tile/" + "{z}/{y}/{x}",
                    "attributions": f'Tiles © <a href="{basemap_layer}">ArcGIS</a>',
                },
            },
            "name": f'{basemap_layer.split("/")[-2].replace("_"," ")}',
        }
        return layer_dict

    def get_view_config(self, center, zoom):
        transformer = Transformer.from_crs("EPSG:4326", "EPSG:3857", always_xy=True)
        x, y = transformer.transform(center[0], center[1])
        view_config = {
            "center": [x, y],
            "zoom": zoom,
        }
        return view_config

    def get_esri_base_layers_dict(self, basemap_layers):
        base_map_layers = []
        for layer in basemap_layers:
            layer_dict = {}
            layer_dict["type"] = "WebGLTile"
            layer_dict["prop"] = {
                "source": {
                    "type": "ImageTile",
                    "props": {
                        "url": f"{layer}/tile/" + "{z}/{y}/{x}",
                        "attributions": f'Tiles © <a href="{layer}">ArcGIS</a>',
                    },
                }
            }
            base_map_layers.append(layer_dict)

        return base_map_layers
