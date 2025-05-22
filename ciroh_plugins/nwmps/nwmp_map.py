from intake.source import base
from .utilities import get_services_dropdown, DATA_SERVICES


class NWMPMap(base.DataSource):
    container = "python"
    version = "0.0.4"
    name = "nwmp_map"
    visualization_args = {}
    visualization_group = "NWMP"
    visualization_label = "NWMP Map"
    visualization_type = "map"
    visualization_args = {
        "service": get_services_dropdown()
    }
    visualization_description = (
        "Provide various map services for National Water Model (NWM) and National Water Prediction Service (NWPS). "
    )
    visualization_tags = [
        "map", "water", "water prediction", "flooding forecast"
    ]
    _user_parameters = []

    def __init__(self, service, metadata=None, **kwargs):
        self.service_url = service
        if service.endswith('/'):
            self.service_url = service[:-1]
        self.service_key = self.service_url.split('/')[-2]
        if "service.Layer" in kwargs:
            self.layer = kwargs["service.Layer"]
        super(NWMPMap, self).__init__(metadata=metadata)

    def read(self):
        service = DATA_SERVICES[self.service_key]
        layer_name = service["name"]
        return {
            "baseMap": "https://server.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Base/MapServer",
            "layers": [
                {
                    "configuration": {
                        "type": "ImageLayer",
                        "props": {
                            "name": layer_name,
                            "source": {
                                "type": "ESRI Image and Map Service",
                                "props": {
                                    "url": self.service_url,
                                    "params": {
                                        "LAYERS": f"show:{self.layer}"
                                    }
                                }
                            }
                        }
                    }
                }
            ],
            "layerControl": True,
            "viewConfig": {
                "center": [-10686671.116154263, 4721671.572580108],
                "zoom": 4.5
            }
        }
