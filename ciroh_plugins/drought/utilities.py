import httpx
import logging
from .drought_area_types import drought_area_types
import os
import json

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


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
                    "label": "World Hillshade Dark",
                    "value": "https://server.arcgisonline.com/arcgis/rest/services/Elevation/World_Hillshade_Dark/MapServer",
                },
                {
                    "label": "World Hillshade",
                    "value": "https://server.arcgisonline.com/arcgis/rest/services/Elevation/World_Hillshade/MapServer",
                },
                {
                    "label": "World Boundaries and Places Alternate",
                    "value": "https://server.arcgisonline.com/arcgis/rest/services/Reference/World_Boundaries_and_Places_Alternate/MapServer",
                },
                {
                    "label": "World Boundaries and Places",
                    "value": "https://server.arcgisonline.com/arcgis/rest/services/Reference/World_Boundaries_and_Places/MapServer",
                },
                {
                    "label": "World Reference Overlay",
                    "value": "https://server.arcgisonline.com/arcgis/rest/services/Reference/World_Reference_Overlay/MapServer",
                },
                {
                    "label": "World Transportation",
                    "value": "https://server.arcgisonline.com/arcgis/rest/services/Reference/World_Transportation/MapServer",
                },
                {
                    "label": "World Ocean Base ",
                    "value": "https://server.arcgisonline.com/arcgis/rest/services/Ocean/World_Ocean_Base/MapServer",
                },
                {
                    "label": "World Ocean Reference",
                    "value": "https://server.arcgisonline.com/arcgis/rest/services/Ocean/World_Ocean_Reference/MapServer",
                },
            ],
        }
    ]


def rgb_to_hex(rgb_color):
    """Convert RGB color to hex color code."""
    if rgb_color and len(rgb_color) >= 3:
        return "#{:02x}{:02x}{:02x}".format(*rgb_color[:3])
    return "#000000"


# Drought
def get_drought_statistic_type():
    return [
        {
            "label": "Drought Statistic Type",
            "options": [
                {
                    "label": "Cumulative Percent Area",
                    "value": 1,
                },
                {
                    "label": "Categorical Percent Area",
                    "value": 2,
                },
                {
                    "label": "Cumulative Area",
                    "value": 3,
                },
                {
                    "label": "Categorical Area",
                    "value": 4,
                },
            ],
        }
    ]


def get_drought_area_type_dropdown():
    return drought_area_types


def get_drought_data_type():
    return [
        {
            "label": "Drought Data Types",
            "options": [
                {
                    "label": "USDM",
                    "value": "0",
                },
                {
                    "label": "7-day Change",
                    "value": "1",
                },
            ],
        }
    ]


def get_drought_index():

    return [
        {
            "label": "Drought Data Index",
            "options": [
                {
                    "label": "USDM",
                    "value": "usdm",
                },
                {
                    "label": "DSCI",
                    "value": "DSCI",
                },
            ],
        }
    ]


def get_drought_dates():
    print("Getting dates for drought")
    api_endpoint = (
        "https://droughtmonitor.unl.edu/Maps/CompareTwoWeeks.aspx/ReturnDates"
    )
    client = httpx.Client(verify=False)
    response = client.get(
        f"{api_endpoint}", headers={"Content-Type": "application/json"}
    )
    data = response.json()
    dropdown_items = []
    dropdown_item = {"label": "Drought Dates", "options": []}
    for item in data.get("d", []):
        dropdown_item["options"].append(
            {"value": f'{item.get("Value")}', "label": item.get("Text")}
        )
    dropdown_items.append(dropdown_item)
    return dropdown_items


def get_geojson(url):
    try:
        with httpx.Client(verify=False) as client:
            r = client.get(
                url=url,
                timeout=None,
            )
            if r.status_code != 200:
                logger.error(f"Error: {r.status_code}")
                logger.error(r.text)
                return None
            else:
                return r.json()
    except httpx.HTTPError as exc:
        logger.error(f"Error while requesting {exc.request.url!r}: {exc}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return None


dir_path = os.path.dirname(__file__)
rfc_qpe_layers = []
with open(f"{dir_path}/rfc_qpe_layers.json") as file:
    rfc_qpe_layers = json.load(file)

DATA_SERVICES = {
    "vegdri_conus_week_data": {
        "name": "quickdri_vegdri_conus_week_data",
        "url": "https://dmsdata.cr.usgs.gov/geoserver/quickdri_vegdri_conus_week_data/vegdri_conus_week_data/wms/",
        "layers": [
            {
                "name": "vegdri_conus_week_data",
                "id": "quickdri_vegdri_conus_week_data:vegdri_conus_week_data"
            }
        ],
        "type": "WMS"
    },
    "quickdri_conus_week_data": {
        "name": "quickdri_quickdri_conus_week_data",
        "url": "https://dmsdata.cr.usgs.gov/geoserver/quickdri_quickdri_conus_week_data/quickdri_conus_week_data/wms/",
        "layers": [
            {
                "name": "quickdri_conus_week_data",
                "id": "quickdri_quickdri_conus_week_data:quickdri_conus_week_data",
            }
        ],
        "type": "WMS"
    },
    "rfc_qpe": {
        "name": "River Forecast Centers Quantative Precipitation Estimates (QPE)",
        "url": "https://mapservices.weather.noaa.gov/raster/rest/services/obs/rfc_qpe/MapServer/",
        "layers": rfc_qpe_layers,
        "type": "ESRI Image and Map Service"
    },
    "cpc_6_10_day_outlk": {
        "name": "6-10 Day Temperature and Precipitation Outlooks",
        "url": "https://mapservices.weather.noaa.gov/vector/rest/services/outlooks/cpc_6_10_day_outlk/MapServer/",
        "layers": [
            {
                "name": "CPC 6-10 Day Temperature Outlook (0)",
                "id": 0
            },
            {
                "name": "CPC 6-10 Day Precipitation Outlook (1)",
                "id": 1
            }
        ],
        "type": "ESRI Image and Map Service"
    },
    "cpc_8_14_day_outlk": {
        "name": "8-14 Day Temperature and Precipitation Outlooks",
        "url": "https://mapservices.weather.noaa.gov/vector/rest/services/outlooks/cpc_8_14_day_outlk/MapServer/",
        "layers": [
            {
                "name": "CPC 8-14 Day Temperature Outlook (0)",
                "id": 0
            },
            {
                "name": "CPC 8-14 Day Precipitation Outlook (1)",
                "id": 1
            }
        ],
        "type": "ESRI Image and Map Service"
    },
    "cpc_mthly_temp_outlk": {
        "name": "Monthly Temperature Outlooks",
        "url": "https://mapservices.weather.noaa.gov/vector/rest/services/outlooks/cpc_mthly_temp_outlk/MapServer/",
        "layers": [
            {
                "name": "Monthly Temperature Outlook (0)",
                "id": 0
            }
        ],
        "type": "ESRI Image and Map Service"
    },
    "cpc_mthly_precip_outlk": {
        "name": "Monthly Precipitation Outlooks",
        "url": "https://mapservices.weather.noaa.gov/vector/rest/services/outlooks/cpc_mthly_precip_outlk/MapServer/",
        "layers": [
            {
                "name": "Monthly Precipitation Outlook (0)",
                "id": 0
            }
        ],
        "type": "ESRI Image and Map Service"
    },
    "cpc_sea_temp_outlk": {
        "name": "Seasonal Temperature Outlooks",
        "url": "https://mapservices.weather.noaa.gov/vector/rest/services/outlooks/cpc_sea_temp_outlk/MapServer/",
        "layers": [
            {'name': 'Lead 1', 'id': 0},
            {'name': 'Lead 2', 'id': 1},
            {'name': 'Lead 3', 'id': 2},
            {'name': 'Lead 4', 'id': 3},
            {'name': 'Lead 5', 'id': 4},
            {'name': 'Lead 6', 'id': 5},
            {'name': 'Lead 7', 'id': 6},
            {'name': 'Lead 8', 'id': 7},
            {'name': 'Lead 9', 'id': 8},
            {'name': 'Lead 10', 'id': 9},
            {'name': 'Lead 11', 'id': 10},
            {'name': 'Lead 12', 'id': 11},
            {'name': 'Lead 13', 'id': 12}
        ],
        "type": "ESRI Image and Map Service"
    },
    "cpc_sea_precip_outlk": {
        "name": "Seasonal Precipitation Outlooks",
        "url": "https://mapservices.weather.noaa.gov/vector/rest/services/outlooks/cpc_sea_precip_outlk/MapServer/",
        "layers": [
            {'name': 'Lead 1', 'id': 0},
            {'name': 'Lead 2', 'id': 1},
            {'name': 'Lead 3', 'id': 2},
            {'name': 'Lead 4', 'id': 3},
            {'name': 'Lead 5', 'id': 4},
            {'name': 'Lead 6', 'id': 5},
            {'name': 'Lead 7', 'id': 6},
            {'name': 'Lead 8', 'id': 7},
            {'name': 'Lead 9', 'id': 8},
            {'name': 'Lead 10', 'id': 9},
            {'name': 'Lead 11', 'id': 10},
            {'name': 'Lead 12', 'id': 11},
            {'name': 'Lead 13', 'id': 12}
        ],
        "type": "ESRI Image and Map Service"
    },
    "cpc_drought_outlk": {
        "name": "Drought Outlooks",
        "url": "https://mapservices.weather.noaa.gov/vector/rest/services/outlooks/cpc_drought_outlk/MapServer/",
        "layers": [
            {'name': 'Monthly Drought Outlook', 'id': 0},
            {'name': 'Monthly Drought Outlook For US and Puerto Rico', 'id': 1},
            {'name': 'Monthly Drought Outlook For US Island Territories', 'id': 2},
            {'name': 'Seasonal Drought Outlook', 'id': 3},
            {'name': 'Seasonal Drought Outlook For US and Puerto Rico', 'id': 4},
            {'name': 'Seasonal Drought Outlook For US Island Territories', 'id': 5}
        ],
        "type": "ESRI Image and Map Service"
    },
    "VegDRI_Example": {
        "name": "VegDRI Example",
        "url": "https://tiles.arcgis.com/tiles/0OTVzJS4K09zlixn/arcgis/rest/services/VegDRI_Example/MapServer/",
        "layers": [],
        "type": "Image Tile"
    },
    "Land_Cover_2020": {
        "name": "Land Cover 2020",
        "url": "https://tiles.arcgis.com/tiles/0OTVzJS4K09zlixn/arcgis/rest/services/Land_Cover_2020/MapServer/",
        "layers": [],
        "type": "Image Tile"
    },
    "Land_Use_2020": {
        "name": "Land Use 2020",
        "url": "https://tiles.arcgis.com/tiles/0OTVzJS4K09zlixn/arcgis/rest/services/Land_Use_2020/MapServer/",
        "layers": [],
        "type": "Image Tile"
    },
    "HUC4_Simplified": {
        "name": "HUC4 Simplified",
        "url": "https://tiles.arcgis.com/tiles/0OTVzJS4K09zlixn/arcgis/rest/services/HUC4_Simplified/MapServer/",
        "layers": [],
        "type": "Image Tile"
    },
    "Counties_Simplified": {
        "name": "Counties Simplified",
        "url": "https://tiles.arcgis.com/tiles/0OTVzJS4K09zlixn/arcgis/rest/services/Counties_Simplified/MapServer/",
        "layers": [],
        "type": "Image Tile"
    },
    "NWS_Radar_10k": {
        "name": "NWS Radar 10k",
        "url": "https://tiles.arcgis.com/tiles/0OTVzJS4K09zlixn/arcgis/rest/services/NWS_Radar_10k/MapServer",
        "layers": [],
        "type": "Image Tile"
    },
    "Median_RMA_Payments": {
        "name": "Median RMA Payments",
        "url": "https://tiles.arcgis.com/tiles/0OTVzJS4K09zlixn/arcgis/rest/services/Median_RMA_Payments/MapServer/",
        "layers": [],
        "type": "Image Tile"
    }
}


def get_service_dropdown():
    return [
        {
            "label": service["name"],
            "value": service["url"]
        }
        for _key, service in DATA_SERVICES.items()
    ]


def get_layers_dropdown(service_key):
    layers = DATA_SERVICES[service_key]['layers']
    return [{'label': layer['name'], 'value': layer['id']} for layer in layers]
