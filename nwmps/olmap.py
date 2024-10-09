from .utilities import (
    get_base_map_layers_dropdown,
    get_services_dropdown,
    DATA_SERVICES
)

from intake.source import base
from pyproj import Transformer
import geopandas as gpd
import requests


class MapVisualization(base.DataSource):
    container = "python"
    version = "0.0.1"
    name = "nwmp_map"
    visualization_args = {
        "latitude": "number",
        "longitude":"number",
        "zoom": "number",
        "huc_id": "text",
        "base_map_layer": get_base_map_layers_dropdown(),
        "services": get_services_dropdown(),

    }
    visualization_group = "NWMP"
    visualization_label = "NWMP Map"
    visualization_type = "map"

    def __init__(self,latitude, longitude, zoom, base_map_layer, services, huc_id, metadata=None):
        # store important kwargs
        self.BASE_URL = "https://maps.water.noaa.gov/server/rest/services/nwm"
        self.center = [longitude, latitude]
        self.zoom = zoom
        self.huc_id = huc_id
        self.service = services.split("-")[0]
        self.layer_id = services.split("-")[1]
        self.base_map_layer = self.get_esri_base_layer_dict(base_map_layer)
        self.service_layer = self.get_service_layer_dict()
        self.view = self.get_view_config(center=self.center, zoom=self.zoom)
        self.layer_huc = self.make_huc_vector_layer()
        self.map_config = self.get_map_config()
        super(MapVisualization, self).__init__(metadata=metadata)

    def read(self):
        """Return a version of the xarray with all the data in memory"""
        HUC_LAYER = self.get_wbd_layer()
        
        if self.layer_huc is not None:
            layers = [self.base_map_layer, HUC_LAYER, self.layer_huc, self.service_layer]
        else:
            layers = [self.base_map_layer, HUC_LAYER, self.service_layer]
        return {
            "layers": layers,
            "view_config": self.view,
            "map_config": self.map_config
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
        if len(str(self.huc_id)) < 2 or len(str(self.huc_id)) > 12: return None 
        huc_level = f"huc{len(str(self.huc_id))}"
        service_url = f"https://hydro.nationalmap.gov/arcgis/rest/services/wbd/MapServer/{int(len(str(self.huc_id))/2)}/query"
        payload = {"where": f"{huc_level} = '{self.huc_id}'", "f": "geojson"}
        rr = requests.get(service_url, params=payload)
        if rr.status_code != 200:
            return None
        gdf = gpd.read_file(rr.url)
        centroid = gdf.geometry.unary_union.centroid
        self.view = self.get_view_config(center=[centroid.x, centroid.y], zoom=self.zoom)
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
            "style": "Polygon",
            "name": f"{self.huc_id} huc id",
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
            "name": f'{self.service.replace("_"," ").title()}',
        }
        return layer_dict

    def get_esri_base_layer_dict(self, base_map_layer):
        layer_dict = {}
        layer_dict["type"] = "WebGLTile"
        layer_dict["props"] = {
            "source": {
                "type": "ImageTile",
                "props": {
                    "url": f"{base_map_layer}/tile/" + "{z}/{y}/{x}",
                    "attributions": f'Tiles © <a href="{base_map_layer}">ArcGIS</a>',
                },
            },
            "name": f'{base_map_layer.split("/")[-2].replace("_"," ").title()}',
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

    def get_map_config(self):
        map_config = {
            "className": "ol-map",
            "style": {
                "width": "100%", 
                "height": "100%"
            }
        }
        return map_config

    def get_esri_base_layers_dict(self, base_map_layers):
        base_map_layers = []
        for layer in base_map_layers:
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

    @staticmethod
    def get_wbd_layer():
        return {
            "type": "ImageLayer",
            "props": {
                "source": {
                    "type": "ImageArcGISRest",
                    "props": {
                        "url": "https://hydro.nationalmap.gov/arcgis/rest/services/wbd/MapServer",
                        "params": {"LAYERS": "hide:0"},
                    },
                },
                "visible": False,
                "name": "wbd Map Service",
            },
        }
    

