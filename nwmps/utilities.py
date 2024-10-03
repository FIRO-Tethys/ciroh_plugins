from pygeohydro import WBD


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
    # {
    #     "type": "ImageLayer",
    #     "props": {
    #         "source": {
    #             "type": "ImageArcGISRest",
    #             "props": {
    #                 "url": "https://mapservices.weather.noaa.gov/eventdriven/rest/services/water/riv_gauges/MapServer",
    #                 "params": {
    #                     "LAYERS": "show:0",
    #                     "layerDefs": json.dumps(
    #                         {
    #                             "0": "status = 'action' or status='minor' or status='moderate' or status='major'"
    #                         }
    #                     ),
    #                 },
    #             },
    #         }
    #     },
    # },
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


CLIPP = {
    "rings": [
        [
            [-111.67769536502314, 40.27410185919322],
            [-111.66122765757531, 40.33344327929173],
            [-111.65407279679609, 40.3533406128824],
            [-111.63343945284758, 40.372747698382746],
            [-111.6367109191067, 40.38428411165247],
            [-111.63041535027348, 40.413030546767104],
            [-111.61257319763656, 40.43208411384723],
            [-111.58412454710836, 40.47688329862195],
            [-111.57472049931805, 40.486737264209154],
            [-111.57424088551053, 40.49276882192537],
            [-111.57539757581836, 40.50294074330499],
            [-111.56780591883177, 40.547315945910675],
            [-111.58034871522177, 40.563135080121185],
            [-111.55997173306062, 40.59063498264238],
            [-111.51790982300362, 40.60859268064733],
            [-111.48824897196609, 40.6005779758602],
            [-111.48689588920377, 40.601016091971786],
            [-111.48536402246557, 40.60229051788704],
            [-111.48216954274861, 40.60919835631484],
            [-111.4709234782738, 40.63392572845042],
            [-111.46353775137719, 40.644876915632565],
            [-111.43448453318503, 40.661201452616375],
            [-111.41164050791352, 40.681100386751716],
            [-111.39091346311885, 40.67088040810839],
            [-111.38143464187674, 40.6457136751914],
            [-111.37039107019828, 40.629965841700006],
            [-111.31618752182912, 40.61731024307969],
            [-111.21025160203341, 40.59136676776753],
            [-111.1957031187419, 40.58769968297194],
            [-111.15512631663128, 40.59937844956704],
            [-111.14066712314984, 40.59949226182036],
            [-111.09305617951466, 40.613894558156034],
            [-111.0836226977531, 40.623977293579756],
            [-111.02973690729904, 40.68385849167403],
            [-111.00090486917045, 40.68973723903028],
            [-110.97986950701383, 40.69820773548937],
            [-110.9478840350193, 40.706346706241575],
            [-110.92731095536811, 40.69820935113627],
            [-110.90351967745279, 40.678246864639455],
            [-110.93944302052044, 40.62544688353046],
            [-110.93789280213838, 40.616410564643104],
            [-110.94434769618323, 40.57849177114925],
            [-110.95702723036703, 40.56830645535559],
            [-110.97587391677165, 40.575283824168956],
            [-110.97832123848482, 40.57146680756925],
            [-110.97435977251001, 40.56814189942777],
            [-110.95439003294271, 40.550722066076524],
            [-110.93855953236181, 40.542570725456024],
            [-110.93183459994415, 40.512456725979284],
            [-110.97882180141936, 40.51581308498783],
            [-110.99415388796719, 40.51479799257695],
            [-111.01147655859849, 40.49591527123266],
            [-111.04907641728948, 40.47216007061717],
            [-111.05770275214306, 40.47193957372065],
            [-111.10327067116381, 40.46700911182717],
            [-111.11429277158135, 40.4678526401511],
            [-111.14037724352187, 40.46308224263645],
            [-111.15833622034023, 40.45413361004241],
            [-111.185550701015, 40.4378232665067],
            [-111.18405193465361, 40.43420690453141],
            [-111.22367683511014, 40.418554470561986],
            [-111.23970426209858, 40.40575703877542],
            [-111.23943000450853, 40.40280621361273],
            [-111.24232774519739, 40.37098513673442],
            [-111.24471742609921, 40.363641247882875],
            [-111.25369531735801, 40.32321320397315],
            [-111.29673967448456, 40.31036867574403],
            [-111.2993319930271, 40.3073391056577],
            [-111.3220307112355, 40.28720086812643],
            [-111.32238204110499, 40.28715787885308],
            [-111.35982608149746, 40.2885393651349],
            [-111.37430019156484, 40.29707357382034],
            [-111.37868831037167, 40.29734876926456],
            [-111.42992773772306, 40.28914593981956],
            [-111.45727664703887, 40.300426444867085],
            [-111.45914848004203, 40.30073812094347],
            [-111.49294812813687, 40.29031884237591],
            [-111.52175977484522, 40.28186494353975],
            [-111.54068575153855, 40.269474773323395],
            [-111.54514778399103, 40.26186409170148],
            [-111.55682200929003, 40.24440023634269],
            [-111.58407524366447, 40.24372267259811],
            [-111.60674983123863, 40.25663920090108],
            [-111.63528651721582, 40.26502023920273],
            [-111.69781949809497, 40.236287166270614],
            [-111.68255200100008, 40.269964207240136],
            [-111.67769536502314, 40.27410185919322],
        ],
        [
            [-111.09850230028593, 40.59533812361579],
            [-111.09285460851441, 40.59601598677398],
            [-111.09461951778776, 40.59580418223172],
            [-111.09850230028593, 40.59533812361579],
        ],
    ],
    "spatialReference": {"wkid": 4326},
}
