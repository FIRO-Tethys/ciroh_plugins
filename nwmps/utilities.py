def get_base_map_layers_dropdown():
    return [
        {
            "label": "ArcGIS Map Service Base Maps",
            "options": [
                {
                    "label": "World Light Gray Base",
                    "value": "https://server.arcgisonline.com/arcgis/rest/services/Canvas/World_Light_Gray_Base/MapServer",
                },
                {
                    "label": "World Dark Gray Base",
                    "value": "https://server.arcgisonline.com/arcgis/rest/services/Canvas/World_Dark_Gray_Base/MapServer",
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
                {
                    "label": "World Hillshade Dark",
                    "value": "https://server.arcgisonline.com/arcgis/rest/services/Elevation/World_Hillshade_Dark/MapServer",
                },
                {
                    "label": "World Hillshade",
                    "value": "https://server.arcgisonline.com/arcgis/rest/services/Elevation/World_Hillshade/MapServer",
                },
            ],
        }
    ]


def get_services_dropdown():
    return [
        {
            "label": service["name"],
            "options": [
                {
                    "label": layer["name"],
                    "value": f"{service['url']}/{service_key}/MapServer/{layer['id']}",
                    # "value": f'{service_key}-{layer["id"]}',
                }
                for layer in service["layers"]
            ],
        }
        for service_key, service in DATA_SERVICES.items()
    ]


#
# River Stages 240 hour Forecast (10)
#
#
#
#
#
DATA_SERVICES = {
    "riv_gauges": {
        "name": " National Water Prediction Service (NWPS) River Gauge System",
        "url": "https://mapservices.weather.noaa.gov/eventdriven/rest/services/water",
        "layers": [
            {
                "name": "Observed River Stages (0)",
                "filter_attr": "status",
                "id": 0,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "River Stages 24 hour Forecast (1)",
                "filter_attr": "status",
                "id": 1,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "River Stages 48 hour Forecast (2)",
                "filter_attr": "status",
                "id": 2,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "River Stages 72 hour Forecast (3)",
                "filter_attr": "status",
                "id": 3,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "River Stages 96 hour Forecast (4)",
                "filter_attr": "status",
                "id": 4,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "River Stages 120 hour Forecast (5)",
                "filter_attr": "status",
                "id": 5,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "River Stages 144 hour Forecast (6)",
                "filter_attr": "status",
                "id": 6,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "River Stages 168 hour Forecast (7)",
                "filter_attr": "status",
                "id": 7,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "River Stages 216 hour Forecast (9)",
                "filter_attr": "status",
                "id": 9,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "River Stages 240 hour Forecast (10)",
                "filter_attr": "status",
                "id": 10,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "River Stages 264 hour Forecast (11)",
                "filter_attr": "status",
                "id": 11,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "River Stages 288 hour Forecast (12)",
                "filter_attr": "status",
                "id": 12,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "River Stages 312 hour Forecast (13)",
                "filter_attr": "status",
                "id": 13,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "River Stages 336 hour Forecast (14)",
                "filter_attr": "status",
                "id": 14,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "Full Forecast Period Stages (15)",
                "filter_attr": "status",
                "id": 15,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
        ],
    },
    "ana_high_flow_magnitude": {
        "name": "National Water Model (NWM) High Flow Magnitude Analysis",
        "url": "https://maps.water.noaa.gov/server/rest/services/nwm",
        "layers": [
            {
                "name": "Est. Annual Exceedance Probability (0)",
                "filter_attr": "recur_cat",
                "id": 0,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            }
        ],
    },
    "ana_past_14day_max_high_flow_magnitude": {
        "name": "National Water Model (NWM) Past 14-Day Max High Flow Magnitude Analysis",
        "url": "https://maps.water.noaa.gov/server/rest/services/nwm",
        "layers": [
            {
                "name": "Past 7 Days - Est. Annual Exceedance Probability (0)",
                "filter_attr": "recur_cat_7day",
                "id": 0,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "Past 14 Days - Est. Annual Exceedance Probability (1)",
                "filter_attr": "recur_cat_14day",
                "id": 1,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
        ],
    },
    "srf_18hr_high_water_arrival_time": {
        "name": "National Water Model (NWM) 18 / 48-Hour High Water Arrival Time Forecast",
        "url": "https://maps.water.noaa.gov/server/rest/services/nwm",
        "layers": [
            {
                "name": "18 Hours - High Water Arrival Time (0)",
                "filter_attr": "high_water_arrival_hour",
                "id": 0,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            {
                "name": "18 Hours - High Water End Time (1)",
                "filter_attr": "below_bank_return_hour",
                "id": 1,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
        ],
    },
    "srf_18hr_rapid_onset_flooding": {
        "name": "National Water Model (NWM) 18-Hour Rapid Onset Flooding Forecast",
        "url": "https://maps.water.noaa.gov/server/rest/services/nwm",
        "layers": [
            {
                "name": "18 Hours - Rapid Onset Flood Arrival Time (0)",
                "filter_attr": "flood_start_hour",
                "id": 0,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "18 Hours - Rapid Onset Flood Duration (1)",
                "filter_attr": "flood_length",
                "id": 1,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "18 Hours - NWM Waterway Length Flooded (2)",
                "filter_attr": "nwm_waterway_length_flooded_percent",
                "id": 2,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
        ],
        #
    },
    "srf_12hr_rapid_onset_flooding_probability": {
        "name": "National Water Model (NWM) 12-Hour Rapid Onset Flooding Probability Forecast",
        "url": "https://maps.water.noaa.gov/server/rest/services/nwm",
        "layers": [
            {
                "name": "Hours 1-6 - Rapid Onset Flooding Probability (0)",
                "filter_attr": "rapid_onset_prob_1_6",
                "id": 0,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            {
                "name": "Hours 7-12 - Rapid Onset Flooding Probability (1)",
                "filter_attr": "rapid_onset_prob_7_12",
                "id": 1,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            {
                "name": "Hours 1-12 - Rapid Onset Flooding Probability (2)",
                "filter_attr": "rapid_onset_prob_all",
                "id": 2,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            {
                "name": "Hours 1-12 - Hotspots - Average Rapid Onset Flooding Probability (3)",
                "filter_attr": "weighted_mean",
                "id": 3,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
        ],
    },
    "srf_12hr_max_high_water_probability": {
        "name": "National Water Model (NWM) 12-Hour Max High Water Probability Forecast",
        "url": "https://maps.water.noaa.gov/server/rest/services/nwm",
        "layers": [
            {
                "name": "12 Hours - High Water Probability (0)",
                "filter_attr": "srf_prob",
                "id": 0,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            {
                "name": "12 Hours - Hotspots - Average High Water Probability (1)",
                "filter_attr": "avg_prob",
                "id": 1,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
        ],
    },
    "srf_18hr_max_high_flow_magnitude": {
        "name": "National Water Model (NWM) 18 / 48-Hour Max High Flow Magnitude Forecast",
        "url": "https://maps.water.noaa.gov/server/rest/services/nwm",
        "layers": [
            {
                "name": "18 Hours - Est. Annual Exceedance Probability (0)",
                "filter_attr": "recur_cat",
                "id": 0,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
        ],
    },
    "mrf_gfs_10day_high_water_arrival_time": {
        "name": "National Water Model(NWM) GFS 10-Day High Water Arrival Time Forecast",
        "url": "https://maps.water.noaa.gov/server/rest/services/nwm",
        "layers": [
            {
                "name": "3 Days - High Water Arrival Time (0)",
                "filter_attr": "high_water_arrival_hour",
                "id": 0,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            {
                "name": "10 Days - High Water Arrival Time (1)",
                "filter_attr": "high_water_arrival_hour",
                "id": 1,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            {
                "name": "10 Days - High Water End Time (2)",
                "filter_attr": "below_bank_return_hour",
                "id": 2,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
        ],
    },
    "mrf_gfs_5day_max_high_water_probability": {
        "name": "National Water Model (NWM) GFS 5-Day High Water Probability Forecast",
        "url": "https://maps.water.noaa.gov/server/rest/services/nwm",
        "layers": [
            {
                "name": "Day 1 - High Water Probability (0)",
                "filter_attr": "hours_3_to_24",
                "id": 0,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            {
                "name": "Day 2 - High Water Probability (1)",
                "filter_attr": "hours_27_to_48",
                "id": 1,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            {
                "name": "Day 3 - High Water Probability (2)",
                "filter_attr": "hours_51_to_72",
                "id": 2,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            {
                "name": "Days 4-5 - High Water Probability (3)",
                "filter_attr": "hours_75_to_120",
                "id": 3,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            {
                "name": "Days 1-5 - High Water Probability (4)",
                "filter_attr": "hours_3_to_120",
                "id": 4,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            {
                "name": "Days 1-5 - Hotspots - Average High Water Probability (5)",
                "filter_attr": "avg_prob",
                "id": 5,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
        ],
    },
    "mrf_gfs_10day_max_high_flow_magnitude": {
        "name": "National Water Model (NWM) GFS 10-Day Max High Flow Magnitude Forecast",
        "url": "https://maps.water.noaa.gov/server/rest/services/nwm",
        "layers": [
            {
                "name": "3 Days - Est. Annual Exceedance Probability (0)",
                "filter_attr": "recur_cat_3day",
                "id": 0,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "5 Days - Est. Annual Exceedance Probability (1)",
                "filter_attr": "recur_cat_5day",
                "id": 1,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
            {
                "name": "10 Days - Est. Annual Exceedance Probability (2)",
                "filter_attr": "recur_cat_10day",
                "id": 2,
                "drawingInfoAttr": "uniqueValueInfos",
                "drawingInfoValueAttr": "value",
            },
        ],
    },
    "mrf_gfs_10day_rapid_onset_flooding": {
        "name": "National Water Model (NWM) GFS 10-Day Rapid Onset Flooding Forecast",
        "url": "https://maps.water.noaa.gov/server/rest/services/nwm",
        "layers": [
            {
                "name": "10 Day - Rapid Onset Flood Arrival Time (0)",
                "filter_attr": "flood_start_hour",
                "id": 0,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            {
                "name": "10 Day - Rapid Onset Flood Duration (1)",
                "filter_attr": "flood_length",
                "id": 1,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            # {
            #     "name": "10 Day - NWM Waterway Length Flooded (2)",
            #     "filter_attr": "nwm_waterway_length_flooded_percent",
            #     "id": 2,
            #     "drawingInfoAttr": "uniqueValueInfos",
            #     "drawingInfoValueAttr": "value",
            # },
        ],
    },
    "mrf_gfs_5day_rapid_onset_flooding_probability": {
        "name": "National Water Model (NWM) GFS 5-Day Rapid Onset Flooding Probability Forecast",
        "url": "https://maps.water.noaa.gov/server/rest/services/nwm",
        "layers": [
            {
                "name": "Day 1 - Rapid Onset Flooding Probability (0)",
                "filter_attr": "rapid_onset_prob_day1",
                "id": 0,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            {
                "name": "Day 2 - Rapid Onset Flooding Probability (1)",
                "filter_attr": "rapid_onset_prob_day2",
                "id": 1,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            {
                "name": "Day 3 - Rapid Onset Flooding Probability (2)",
                "filter_attr": "rapid_onset_prob_day3",
                "id": 2,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            {
                "name": "Days 4-5 - Rapid Onset Flooding Probability (3)",
                "filter_attr": "rapid_onset_prob_day4_5",
                "id": 3,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            {
                "name": "Days 1-5 - Rapid Onset Flooding Probability (4)",
                "filter_attr": "rapid_onset_prob_all",
                "id": 4,
                "drawingInfoAttr": "classBreakInfos",
                "drawingInfoValueAttr": "classMaxValue",
            },
            # {
            #     "name": "Days 1-5 - Hotspots - Average Rapid Onset Flooding Probability (5)",
            #     "filter_attr": "weighted_mean",
            #     "id": 5,
            # },
        ],
    },
}


def get_service_layers():
    layers = []
    # Iterate over DATA_SERVICES
    for service_key, service_value in DATA_SERVICES.items():
        for layer in service_value["layers"]:
            obj = {"label": layer["name"], "value": f"{layer['id']}"}
            layers.append(obj)
    return layers

    # {
    #   type: "ImageLayer",
    #   props: {
    #     source:{
    #       type: "ImageArcGISRest",
    #       props:{
    #         url: 'https://mapservices.weather.noaa.gov/eventdriven/rest/services/water/riv_gauges/MapServer',
    #         params: {
    #           LAYERS: "show:0",
    #           layerDefs: JSON.stringify({ "0": "status = 'action' or status='minor' or status='moderate' or status='major'" })
    #         }
    #       }
    #     }
    #   }
    # },


# SOMETHIGS THAT WE MIGHT NEED LATER ON
# def shaplyGeom2ArcGISGeom(self, geom):
#     geom_type = geom.geom_type
#     if geom_type == "Point":
#         x, y = geom.coords[0]
#         return {"x": x, "y": y}
#     elif geom_type == "LineString":
#         coords = [{"x": x, "y": y} for x, y in geom.coords]
#         return {"paths": [coords]}
#     elif geom_type == "Polygon":
#         exterior = [{"x": x, "y": y} for x, y in geom.exterior.coords]
#         interiors = [
#             [{"x": x, "y": y} for x, y in interior.coords]
#             for interior in geom.interiors
#         ]
#         return {"rings": [exterior] + interiors}
#     elif geom_type == "MultiPoint":
#         points = [{"x": p.x, "y": p.y} for p in geom.geoms]
#         return {"points": points}
#     elif geom_type == "MultiLineString":
#         paths = [[{"x": x, "y": y} for x, y in line.coords] for line in geom.geoms]
#         return {"paths": paths}
#     elif geom_type == "MultiPolygon":
#         rings = []
#         for polygon in geom.geoms:
#             exterior = [{"x": x, "y": y} for x, y in polygon.exterior.coords]
#             interiors = [
#                 [{"x": x, "y": y} for x, y in interior.coords]
#                 for interior in polygon.interiors
#             ]
#             rings.extend([exterior] + interiors)
#         return {"rings": rings}
#     else:
#         raise ValueError(f"Unsupported geometry type: {geom_type}")

# def arcGisGeomObject(self, esri_geom_dict):
#     return Geometry(esri_geom_dict)


# def get_huc_options():
#     """
#     Create a dictionary containing all the HUC IDs of the Watershed Boundary Dataset.

#     Returns:
#         list: A list of dictionaries, each containing HUC level and options.
#     """

#     huc_levels = [2, 4, 6, 8, 10, 12]
#     huc_data = []
#     for huc_level in huc_levels:
#         huc_level_str = f"huc{huc_level}"
#         wbd = WBD(huc_level_str)
#         breakpoint()
#         try:
#             print(f"Fetching data for {huc_level_str}...")
#             # Fetch HUC IDs for the current level
#             gdf = wbd.get_huc_boundaries(huc_level_str)
#             # Extract unique HUC IDs and sort them
#             huc_ids = sorted(gdf[huc_level_str].unique())
#             # Build the options list
#             options = [{"label": huc_id, "value": huc_id} for huc_id in huc_ids]
#             # Add to huc_data
#             huc_data.append({"label": huc_level_str, "options": options})
#         except Exception as e:
#             print(f"Error getting HUC level {huc_level}: {e}")
#             continue

#     return huc_data
