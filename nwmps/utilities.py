from pygeohydro import WBD
import json


# Define a function to convert MultiLineString with 3 dimensions to 2 dimensions
def _to_2d(x, y, z=None):
    if z is None:
        return (x, y)
    return tuple(filter(None, [x, y]))


def get_huc_boundary(huc_layer, ids_list):
    """
    Retrieve the watershed boundary geometry for a given HUC code.

    Parameters:
        huc_code (str): The Hydrologic Unit Code of the watershed.

    Returns:
        geopandas.GeoDataFrame: A GeoDataFrame containing the watershed boundary geometry.
    """
    wbd = WBD(huc_layer)
    gdf = wbd.byids(huc_layer, ids_list)
    return gdf


def get_all_huc_codes(level=4):
    """
    Retrieve a list of all possible HUC codes at a specified level.

    Parameters:
        level (int): The HUC level (2, 4, 6, 8, 10, 12).

    Returns:
        list: A list of HUC codes at the specified level.
    """
    pass


BASEMAP_LAYERS_DROPDOWN = [
    {
        "label": "Esri Basemaps",
        "options": [
            {
                "label": "World Light Gray Base",
                "value": "https://server.arcgisonline.com/arcgis/rest/services/Canvas/World_Light_Gray_Base/MapServer",
            },
            {
                "label": "World Topo Map",
                "value": "https://server.arcgisonline.com/arcgis/rest/services/World_Topo_Map/MapServer",
            },
            {
                "label": "World Imagery",
                "value": "https://server.arcgisonline.com/arcgis/rest/services/World_Imagery/MapServer",
            },
            {
                "label": "World Terrain Base",
                "value": "https://server.arcgisonline.com/arcgis/rest/services/World_Terrain_Base/MapServer",
            },
            {
                "label": "World Street Map",
                "value": "https://server.arcgisonline.com/arcgis/rest/services/World_Street_Map/MapServer",
            },
            {
                "label": "World Physical Map",
                "value": "https://server.arcgisonline.com/arcgis/rest/services/World_Physical_Map/MapServer",
            },
            {
                "label": "World Shaded Relief",
                "value": "https://server.arcgisonline.com/arcgis/rest/services/World_Shaded_Relief/MapServer",
            },
            {
                "label": "World Terrain Reference",
                "value": "https://server.arcgisonline.com/arcgis/rest/services/World_Terrain_Reference/MapServer",
            },
            {
                "label": "World Transportation",
                "value": "https://server.arcgisonline.com/arcgis/rest/services/World_Transportation/MapServer",
            },
        ],
    }
]


BASE_URL_SERVICES = "https://maps.water.noaa.gov/server/rest/services/nwm"


BASEMAP_LAYERS = [
    {
        "type": "WebGLTile",
        "props": {
            "source": {
                "type": "ImageTile",
                "props": {
                    "url": "https://server.arcgisonline.com/arcgis/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}",
                    "attributions": 'Tiles © <a href="https://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer">ArcGIS</a>',
                },
            }
        },
    }
]

LAYERS = [
    {
        "type": "WebGLTile",
        "props": {
            "source": {
                "type": "ImageTile",
                "props": {
                    "url": "https://server.arcgisonline.com/arcgis/rest/services/Canvas/World_Light_Gray_Base/MapServer/tile/{z}/{y}/{x}",
                    "attributions": 'Tiles © <a href="https://services.arcgisonline.com/ArcGIS/rest/services/World_Topo_Map/MapServer">ArcGIS</a>',
                },
            }
        },
    },
    {
        "type": "ImageLayer",
        "props": {
            "source": {
                "type": "ImageArcGISRest",
                "props": {
                    "url": "https://hydro.nationalmap.gov/arcgis/rest/services/wbd/MapServer",
                    "params": {"LAYERS": "hide:0"},
                },
            }
        },
    },
    {
        "type": "ImageLayer",
        "props": {
            "source": {
                "type": "ImageArcGISRest",
                "props": {
                    "url": "https://mapservices.weather.noaa.gov/eventdriven/rest/services/water/riv_gauges/MapServer",
                    "params": {
                        "LAYERS": "show:0",
                        "layerDefs": json.dumps(
                            {
                                "0": "status = 'action' or status='minor' or status='moderate' or status='major'"
                            }
                        ),
                    },
                },
            }
        },
    },
]


DATA_SERVICES = {
    "ana_high_flow_magnitude": {
        "name": "National Water Model (NWM) High Flow Magnitude Analysis",
        "layers": [
            {
                "name": "Est. Annual Exceedance Probability (0)",
                "filter_attr": "recur_cat",
                "id": 0,
            }
        ],
    },
    "ana_past_14day_max_high_flow_magnitude": {
        "name": "National Water Model (NWM) Past 14-Day Max High Flow Magnitude Analysis",
        "layers": [
            {
                "name": "Past 7 Days - Est. Annual Exceedance Probability (0)",
                "filter_attr": "recur_cat_7day",
                "id": 0,
            },
            {
                "name": "Past 14 Days - Est. Annual Exceedance Probability (1)",
                "filter_attr": "recur_cat_14day",
                "id": 1,
            },
        ],
    },
    "srf_18hr_high_water_arrival_time": {
        "name": "National Water Model (NWM) 18 / 48-Hour High Water Arrival Time Forecast",
        "layers": [
            {
                "name": "18 Hours - High Water Arrival Time (0)",
                "filter_attr": "high_water_arrival_hour",
                "id": 0,
            },
            {
                "name": "18 Hours - High Water End Time (1)",
                "filter_attr": "below_bank_return_hour",
                "id": 1,
            },
        ],
    },
    "srf_18hr_rapid_onset_flooding": {
        "name": "National Water Model (NWM) 18-Hour Rapid Onset Flooding Forecast",
        "layers": [
            {
                "name": "18 Hours - Rapid Onset Flood Arrival Time (0)",
                "filter_attr": "flood_start_hour",
                "id": 0,
            },
            {
                "name": "18 Hours - Rapid Onset Flood Duration (1)",
                "filter_attr": "flood_length",
                "id": 1,
            },
            {
                "name": "18 Hours - NWM Waterway Length Flooded (2)",
                "filter_attr": "nwm_waterway_length_flooded_percent",
                "id": 2,
            },
        ],
        #
    },
    "srf_12hr_rapid_onset_flooding_probability": {
        "name": "National Water Model (NWM) 12-Hour Rapid Onset Flooding Probability Forecast",
        "layers": [
            {
                "name": "Hours 1-6 - Rapid Onset Flooding Probability (0)",
                "filter_attr": "rapid_onset_prob_1_6",
                "id": 0,
            },
            {
                "name": "Hours 7-12 - Rapid Onset Flooding Probability (1)",
                "filter_attr": "rapid_onset_prob_7_12",
                "id": 1,
            },
            {
                "name": "Hours 1-12 - Rapid Onset Flooding Probability (2)",
                "filter_attr": "rapid_onset_prob_all",
                "id": 2,
            },
            {
                "name": "Hours 1-12 - Hotspots - Average Rapid Onset Flooding Probability (3)",
                "filter_attr": "weighted_mean",
                "id": 3,
            },
        ],
    },
    "srf_12hr_max_high_water_probability": {
        "name": "National Water Model (NWM) 12-Hour Max High Water Probability Forecast",
        "layers": [
            {
                "name": "12 Hours - High Water Probability (0)",
                "filter_attr": "srf_prob",
                "id": 0,
            },
            {
                "name": "12 Hours - Hotspots - Average High Water Probability (1)",
                "filter_attr": "avg_prob",
                "id": 1,
            },
        ],
    },
    "srf_18hr_max_high_flow_magnitude": {
        "name": "National Water Model (NWM) 18 / 48-Hour Max High Flow Magnitude Forecast	",
        "layers": [
            {
                "name": "18 Hours - Est. Annual Exceedance Probability (0)",
                "filter_attr": "recur_cat",
                "id": 0,
            },
        ],
    },
    "mrf_gfs_10day_high_water_arrival_time": {
        "name": "National Water Model(NWM) GFS 10-Day High Water Arrival Time Forecast",
        "layers": [
            {
                "name": "3 Days - High Water Arrival Time (0)",
                "filter_attr": "high_water_arrival_hour",
                "id": 0,
            },
            {
                "name": "10 Days - High Water Arrival Time (1)",
                "filter_attr": "high_water_arrival_hour",
                "id": 1,
            },
            {
                "name": "10 Days - High Water End Time (2)",
                "filter_attr": "below_bank_return_hour",
                "id": 2,
            },
        ],
    },
    "mrf_gfs_5day_max_high_water_probability": {
        "name": "National Water Model (NWM) GFS 5-Day High Water Probability Forecast",
        "layers": [
            {
                "name": "Day 1 - High Water Probability (0)",
                "filter_attr": "hours_3_to_24",
                "id": 0,
            },
            {
                "name": "Day 2 - High Water Probability (1)",
                "filter_attr": "hours_27_to_48",
                "id": 1,
            },
            {
                "name": "Day 3 - High Water Probability (2)",
                "filter_attr": "hours_51_to_72",
                "id": 2,
            },
            {
                "name": "Days 4-5 - High Water Probability (3)",
                "filter_attr": "hours_75_to_120",
                "id": 3,
            },
            {
                "name": "Days 1-5 - High Water Probability (4)",
                "filter_attr": "hours_3_to_120",
                "id": 4,
            },
            {
                "name": "Days 1-5 - Hotspots - Average High Water Probability (5)",
                "filter_attr": "avg_prob",
                "id": 5,
            },
        ],
    },
    "mrf_gfs_10day_max_high_flow_magnitude": {
        "name": "National Water Model (NWM) GFS 10-Day Max High Flow Magnitude Forecast",
        "layers": [
            {
                "name": "3 Days - Est. Annual Exceedance Probability (0)",
                "filter_attr": "recur_cat_3day",
                "id": 0,
            },
            {
                "name": "5 Days - Est. Annual Exceedance Probability (1)",
                "filter_attr": "recur_cat_5day",
                "id": 1,
            },
            {
                "name": "10 Days - Est. Annual Exceedance Probability (2)",
                "filter_attr": "recur_cat_10day",
                "id": 2,
            },
        ],
    },
    "mrf_gfs_10day_rapid_onset_flooding": {
        "name": "National Water Model (NWM) GFS 10-Day Rapid Onset Flooding Forecast",
        "layers": [
            {
                "name": "10 Day - Rapid Onset Flood Arrival Time (0)",
                "filter_attr": "flood_start_hour",
                "id": 0,
            },
            {
                "name": "10 Day - Rapid Onset Flood Duration (1)",
                "filter_attr": "flood_length",
                "id": 1,
            },
            {
                "name": "10 Day - NWM Waterway Length Flooded (2)",
                "filter_attr": "nwm_waterway_length_flooded_percent",
                "id": 2,
            },
        ],
    },
    "mrf_gfs_5day_rapid_onset_flooding_probability": {
        "name": "National Water Model (NWM) GFS 5-Day Rapid Onset Flooding Probability Forecast",
        "layers": [
            {
                "name": "Day 1 - Rapid Onset Flooding Probability (0)",
                "filter_attr": "rapid_onset_prob_day1",
                "id": 0,
            },
            {
                "name": "Day 2 - Rapid Onset Flooding Probability (1)",
                "filter_attr": "rapid_onset_prob_day2",
                "id": 1,
            },
            {
                "name": "Day 3 - Rapid Onset Flooding Probability (2)",
                "filter_attr": "rapid_onset_prob_day3",
                "id": 2,
            },
            {
                "name": "Days 4-5 - Rapid Onset Flooding Probability (3)",
                "filter_attr": "rapid_onset_prob_day4_5",
                "id": 3,
            },
            {
                "name": "Days 1-5 - Rapid Onset Flooding Probability (4)",
                "filter_attr": "rapid_onset_prob_all",
                "id": 4,
            },
            {
                "name": "Days 1-5 - Hotspots - Average Rapid Onset Flooding Probability (5)",
                "filter_attr": "weighted_mean",
                "id": 5,
            },
        ],
    },
}

SERVICES_DROPDOWN = [
    {
        "label": service["name"],
        "options": [
            {
                "label": layer["name"],
                "value": f'{service_key}-{layer["id"]}',
            }
            for layer in service["layers"]
        ],
    }
    for service_key, service in DATA_SERVICES.items()
]


def get_service_layers():
    layers = []
    # Iterate over DATA_SERVICES
    for service_key, service_value in DATA_SERVICES.items():
        for layer in service_value["layers"]:
            obj = {"label": layer["name"], "value": f"{layer['id']}"}
            layers.append(obj)
    return layers
