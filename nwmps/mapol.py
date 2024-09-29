


from .utilities import DATA_SERVICES, BASE_URL_SERVICES

from intake.source import base
from shapely.geometry import Point, LineString, Polygon
from arcgis.geometry import Geometry


class OLMap(base.DataSource):
    container = "python"
    version = "0.0.1"
    name = "nwmp_map"
    visualization_args = {}
    visualization_group = "NWMP"
    visualization_label = "NWMP Map"
    visualization_type = "map"

    def __init__(self,geom, metadata=None):
        # store important kwargs
        self.layers = self.get_service_layers()
        self.geom = geom
        super(OLMap, self).__init__(metadata=metadata)

    def read(self):
        """Return a version of the xarray with all the data in memory"""
        pass

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
        if geom_type == 'Point':
            x, y = geom.coords[0]
            return {'x': x, 'y': y}
        elif geom_type == 'LineString':
            coords = [{'x': x, 'y': y} for x, y in geom.coords]
            return {'paths': [coords]}
        elif geom_type == 'Polygon':
            exterior = [{'x': x, 'y': y} for x, y in geom.exterior.coords]
            interiors = [
                [{'x': x, 'y': y} for x, y in interior.coords]
                for interior in geom.interiors
            ]
            return {'rings': [exterior] + interiors}
        elif geom_type == 'MultiPoint':
            points = [{'x': p.x, 'y': p.y} for p in geom.geoms]
            return {'points': points}
        elif geom_type == 'MultiLineString':
            paths = [
                [{'x': x, 'y': y} for x, y in line.coords]
                for line in geom.geoms
            ]
            return {'paths': paths}
        elif geom_type == 'MultiPolygon':
            rings = []
            for polygon in geom.geoms:
                exterior = [{'x': x, 'y': y} for x, y in polygon.exterior.coords]
                interiors = [
                    [{'x': x, 'y': y} for x, y in interior.coords]
                    for interior in polygon.interiors
                ]
                rings.extend([exterior] + interiors)
            return {'rings': rings}
        else:
            raise ValueError(f"Unsupported geometry type: {geom_type}")

    def arcGisGeomObject(self,esri_geom_dict):
        return Geometry(esri_geom_dict)
    
    # TODO: make a function that allows the user to find the layers of a service by name from DATA_SERVICES using a layer_list
    def get_ol_service_layers_dict(self, layers_list):
        for layer in layers_list:
            layer_dict = {}
            layer_dict["type"] = "ImageLayer"
            layer_dict["prop"] = {"url": f"{BASE_URL_SERVICES}/"}
        pass


    #we only want the 