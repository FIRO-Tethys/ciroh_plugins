from intake.source import base
import json
import os
from .utilities import get_drought_dates, get_geojson, get_service_dropdown, DATA_SERVICES


class DroughtMap(base.DataSource):
    container = "python"
    version = "0.0.4"
    name = "drought_map"
    visualization_args = {}
    visualization_group = "Drought_Monitor"
    visualization_label = "Drought Map"
    visualization_type = "map"
    visualization_args = {
        "date": get_drought_dates(),
        "service": get_service_dropdown(),
    }
    visualization_description = (
        "Provide various map services for the temperature, precipitation and drought. "
    )
    visualization_tags = [
        "map", "drought", "temperature", "precipitation"
    ]
    visualization_attribution = "NOAA, USGS, NDMC, USDA"
    _user_parameters = []

    def __init__(self, date, service, metadata=None, **kwargs):
        self.date = date
        self.service_url = service
        if service.endswith('/'):
            self.service_url = service[:-1]
        self.service_key = self.service_url.split('/')[-2]
        if "service.Layer" in kwargs:
            self.layer = kwargs["service.Layer"]
        super(DroughtMap, self).__init__(metadata=metadata)

    def read(self):
        geojson = self.get_usdm_layer()
        geojson['crs'] = {"type": "name", "properties": {"name": "EPSG:4326"}}
        dir_path = os.path.dirname(__file__)
        with open(f"{dir_path}/style.json") as file:
            style = json.load(file)
        legend = {
          "title": "USDM Archive",
          "items": [
            {
              "label": "Abnormally Dry",
              "color": "#ffff00",
              "symbol": "square"
            },
            {
              "label": "Moderate Drought",
              "color": "#fcd37f",
              "symbol": "square"
            },
            {
              "label": "Severe Drought",
              "color": "#ffaa00",
              "symbol": "square"
            },
            {
              "label": "Extreme Drought",
              "color": "#e60000",
              "symbol": "square"
            },
            {
              "label": "Exceptional Drought",
              "color": "#730000",
              "symbol": "square"
            },
            {
              "label": "No Data",
              "color": "#808080",
              "symbol": "square"
            },
            {
              "label": "None",
              "color": "#ffffff",
              "symbol": "square"
            }
          ]
        }
        geojson_layer = {
            "configuration": {
                "type": "VectorLayer",
                "props": {
                    "name": "USDM Archive",
                    "source": {
                        "type": "GeoJSON",
                        "props": {},
                        "geojson": geojson,
                    }
                },
                "style": style
            },
            "legend": legend
        }

        service = DATA_SERVICES[self.service_key]
        source_type = service["type"]
        layer_name = service["name"]
        if source_type in ["WMS", "ESRI Image and Map Service"]:
            other_layer = {
                "configuration": {
                    "type": "ImageLayer",
                    "props": {
                        "name": layer_name,
                        "source": {
                            "type": source_type,
                            "props": {
                                "url": self.service_url,
                                "params": {
                                    "LAYERS": self.layer if source_type == 'WMS' else f"show:{self.layer}"
                                }
                            }
                        }
                    }
                }
            }
        elif service["type"] == "Image Tile":
            other_layer = {
                "configuration": {
                    "type": "TileLayer",
                    "props": {
                        "name": layer_name,
                        "source": {
                            "type": "Image Tile",
                            "props": {
                                "url": self.service_url + "/tile/{z}/{y}/{x}"
                            }
                        }
                    }
                }
            }

        return {
            "baseMap": "https://server.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Base/MapServer",
            "layers": [
                geojson_layer,
                other_layer
            ],
            "layerControl": True,
        }

    def get_usdm_layer(self):
        url = f"https://droughtmonitor.unl.edu/data/json/usdm_{self.date}.json"
        try:
            usdm_layer = get_geojson(url)
        except Exception as e:
            print(f"Unexpected error: {e}")
            return None
        return usdm_layer
