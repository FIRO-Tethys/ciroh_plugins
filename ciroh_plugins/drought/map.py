from intake.source import base
import json
import os
from .utilities import get_drought_dates, get_geojson


class Map(base.DataSource):
    container = "python"
    version = "0.0.1"
    name = "drought_map_preconfigured"
    visualization_args = {}
    visualization_group = "Drought_Monitor"
    visualization_label = "Drought Map Preconfigured"
    visualization_type = "map"
    visualization_args = {
        "date": get_drought_dates(),
    }
    _user_parameters = []

    def __init__(self, date, metadata=None, **kwargs):
        self.date = date
        super(Map, self).__init__(metadata=metadata)
        
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
        return {
            "baseMap": "https://server.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Base/MapServer",
            "layers": [
                {
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
        