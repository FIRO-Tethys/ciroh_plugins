from intake.source import base
import logging
import httpx
from .utilities import get_geojson, get_drought_dates,get_base_map_layers_dropdown
from .sourceUrls import json_urls
# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DroughtMapViewer(base.DataSource):
    container = "python"
    version = "0.0.4"
    name = "drought_map_viewer"
    visualization_args = {
        "date": get_drought_dates(),
        "base_map_layer": get_base_map_layers_dropdown(),
    }
    visualization_group = "Drought_Monitor"
    visualization_label = "Drought Monitor Map Viewer"
    visualization_type = "custom"

    def __init__(self,date,base_map_layer,metadata=None):
        self.date = date
        self.mfe_unpkg_url = "http://localhost:4000/remoteEntry.js"
        self.mfe_scope = "drought_map"
        self.mfe_module = "./MapComponent"
        self.view = self.get_view_config()
        self.map_config = self.get_map_config()
        self.base_map_layer = self.get_esri_base_layer_dict(base_map_layer)
        super(DroughtMapViewer, self).__init__(metadata=metadata)

    def read(self):
        logger.info("Reading map data configuration")
        return {
            "url": self.mfe_unpkg_url,
            "scope": self.mfe_scope,
            "module": self.mfe_module,
            "props": {
                "extraLayers": self.get_extra_layers(),
                "layers": self.get_layers(),
                "viewConfig": self.view,
                "mapConfig": self.map_config,
            },
        }

    def get_extra_layers(self):
        layers = [self.get_usdm_layer()]
        return layers
    
    def get_layers(self):
        layers = [self.base_map_layer]
        return layers
    
    def get_usdm_layer(self):
        url = f'{json_urls['usdm']}_{self.date}.json'
        try:
            usdm_layer = get_geojson(url)
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
            return None
        return usdm_layer


    @staticmethod
    def get_map_config():
        map_config = {
            "className": "ol-map",
            "style": {"width": "100%", "height": "100%", "position": "relative"},
        }
        logger.info("Map configuration created")
        return map_config
    
    @staticmethod
    def get_view_config():

        view_config = {
          "center": [-11807318, 4983337],
          "zoom": 4,
          "maxZoom": 11,
          "minZoom": 3,
        }
        logger.info("View configuration created")
        return view_config


    @staticmethod
    def get_esri_base_layer_dict(base_map_layer):
        layer_dict = {
            "type": "WebGLTile",
            "props": {
                "source": {
                    "type": "ImageTile",
                    "props": {
                        "url": f"{base_map_layer}/tile/" + "{z}/{y}/{x}",
                        "attributions": f'Tiles © <a href="{base_map_layer}">ArcGIS</a>',
                    },
                },
                "name": f'{base_map_layer.split("/")[-2].replace("_"," ").title()}',
            },
        }
        logger.info("Base layer dictionary created")
        return layer_dict