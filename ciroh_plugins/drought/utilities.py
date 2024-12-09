
import httpx
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Drought
def get_drought_statistic_type():
        return [
            {
                "label": "Drought Statistic Type",
                "options": [
                    {
                        "label": "Cumulative Percent Area",
                        "value": "1",
                    },
                    {
                        "label": "Categorical Percent Area",
                        "value": "2",
                    },
                    {
                        "label": "Cumulative Area",
                        "value": "3",
                    },
                    {
                        "label": "Categorical Area",
                        "value": "4",
                    },
                ]
            }
        ]

def get_drought_area_type_dropdown():
    api_endpoint = 'https://droughtmonitor.unl.edu/DmData/DataTables.aspx/ReturnAOI'
    area_types_dict = {
        "national": "National",
        "state": "State",
        "climdiv": "Climate Division",
        "dregion": "Geographic Regions",
        "county": "County",
        "fema": "FEMA Region",
        "huc2": "HUC (2 digit)",
        "huc4": "HUC (4 digit)",
        "huc6": "HUC (6 digit)",
        "huc8": "HUC (8 digit)",
        "nws": "NWS Region",
        "wfo": "NWS Weather Forecast Offices",
        "rfc": "River Forecast Centers",
        "tribal": "Tribal Areas",
        "usaceds": "USACE District",
        "usacedv": "USACE Division",
        "chubs": "USDA Climate Hubs",
        "rdews": "Regional Drought Early Warning System",
        "rcc": "Regional Climate Centers",
        "oregion": "Other Regions",
    }
    dropdown_items = []
    client = httpx.Client(verify=False)
    for key, value in area_types_dict.items():
        dropdown_item ={
            "label": value,
            "options":[]
        }
        try:
            response = client.get(f'{api_endpoint}?aoi="{key}"', headers={"Content-Type": "application/json"})
            data = response.json()
            for item in data.get('d', []):
                dropdown_item['options'].append({
                    "value": f'{key}-{item.get("Value")}',
                    "label": item.get("Text")
                })
            dropdown_items.append(dropdown_item)
        except httpx.HTTPError as exc:
            logger.error(f"Error while requesting {exc.request.url!r}: {str(exc.__class__.__name__)}")
        except Exception as e:
            logger.error(f"Unexpected error: {e}")
    return dropdown_items

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
                }
            ]
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
                }
            ]
        }
    ]


def get_drought_dates():
    api_endpoint = 'https://droughtmonitor.unl.edu/Maps/CompareTwoWeeks.aspx/ReturnDates'
    client = httpx.Client(verify=False)
    response = client.get(f'{api_endpoint}', headers={"Content-Type": "application/json"})
    data = response.json()
    dropdown_items = []
    dropdown_item ={
        "label": "Drought Dates",
        "options":[]
    }
    for item in data.get('d', []):
        dropdown_item['options'].append({
            "value": f'{item.get("Value")}',
            "label": item.get("Text")
        })
    dropdown_items.append(dropdown_item)
    return dropdown_items