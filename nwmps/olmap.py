from .utilities import (
    DATA_SERVICES,
    SERVICES_DROPDOWN,
    BASEMAP_LAYERS_DROPDOWN,
    HUC_LAYER,
)

from intake.source import base
from shapely.geometry import Point, LineString, Polygon
from arcgis.geometry import Geometry
import json
from pyproj import Transformer


class MapVisualization(base.DataSource):
    container = "python"
    version = "0.0.1"
    name = "nwmp_map"
    visualization_args = {
        "basemap_layer": BASEMAP_LAYERS_DROPDOWN,
        "services": SERVICES_DROPDOWN,
        "huc_id": "0202",  # empty text it will be an variable input on the dashboard app
    }
    visualization_group = "NWMP"
    visualization_label = "NWMP Map"
    visualization_type = "map"

    def __init__(self, basemap_layer, services, huc_id=None, metadata=None):
        # store important kwargs
        self.BASE_URL = "https://maps.water.noaa.gov/server/rest/services/nwm"
        self.service = services.split("-")[0]
        self.layer_id = services.split("-")[1]
        self.basemap_layer = self.get_esri_base_layer_dict(basemap_layer)
        self.service_layer = self.get_service_layer_dict()
        self.geom = None
        self.view = self.get_view_config(center=[-110.875, 37.345], zoom=5)
        super(MapVisualization, self).__init__(metadata=metadata)

    def read(self):
        """Return a version of the xarray with all the data in memory"""
        print("Reading data from MapVisualization")
        layers = [self.basemap_layer, HUC_LAYER, self.service_layer]
        # layers = LAYERS
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

    def shaplyGeom2ArcGISGeom(self, geom):
        geom_type = geom.geom_type
        if geom_type == "Point":
            x, y = geom.coords[0]
            return {"x": x, "y": y}
        elif geom_type == "LineString":
            coords = [{"x": x, "y": y} for x, y in geom.coords]
            return {"paths": [coords]}
        elif geom_type == "Polygon":
            exterior = [{"x": x, "y": y} for x, y in geom.exterior.coords]
            interiors = [
                [{"x": x, "y": y} for x, y in interior.coords]
                for interior in geom.interiors
            ]
            return {"rings": [exterior] + interiors}
        elif geom_type == "MultiPoint":
            points = [{"x": p.x, "y": p.y} for p in geom.geoms]
            return {"points": points}
        elif geom_type == "MultiLineString":
            paths = [[{"x": x, "y": y} for x, y in line.coords] for line in geom.geoms]
            return {"paths": paths}
        elif geom_type == "MultiPolygon":
            rings = []
            for polygon in geom.geoms:
                exterior = [{"x": x, "y": y} for x, y in polygon.exterior.coords]
                interiors = [
                    [{"x": x, "y": y} for x, y in interior.coords]
                    for interior in polygon.interiors
                ]
                rings.extend([exterior] + interiors)
            return {"rings": rings}
        else:
            raise ValueError(f"Unsupported geometry type: {geom_type}")

    def arcGisGeomObject(self, esri_geom_dict):
        return Geometry(esri_geom_dict)

    def get_service_layer_dict(self):
        self.BASE_URL = "https://maps.water.noaa.gov/server/rest/services/nwm"
        service_url = f"{self.BASE_URL}/{self.service}/MapServer"
        layer_dict = {}
        layer_dict["type"] = "ImageLayer"
        layer_dict["props"] = {
            "source": {
                "type": "ImageArcGISRest",
                "props": {
                    "url": service_url,
                    # "params": {
                    #     "LAYERS": f"show:{self.layer_id}",
                    #     "spatialFilter": json.dumps(
                    #         {
                    #             "spatialRel": "esriSpatialRelContains",
                    #             "geometryType": "esriGeometryPolygon",
                    #             "geometry": CLIPP,
                    #         }
                    #     ),
                    # },
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

    # we only want the
