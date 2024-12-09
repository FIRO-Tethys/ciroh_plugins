from intake.source import base
import httpx
from .utilities import get_drought_area_type_dropdown,get_drought_index,get_drought_dates
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# This will be used for the TimeSeries of the NWM data
class DroughtDataGraph(base.DataSource):
    container = "python"
    version = "0.0.4"
    name = "nwmp_api_drought_timeseries_data"
    visualization_args = {
        "area_type": get_drought_area_type_dropdown(),
        "date": get_drought_dates()    
    }
    visualization_group = "NWMP"
    visualization_label = "NWMP Drought Data Graph"
    visualization_type = "plotly"

    def __init__(self, area_type,date,metadata=None):

        self.api_base_url = "https://droughtmonitor.unl.edu/DmData/DataGraphs.aspx/ReturnTabularDMAreaPercent"
        self.area_type = area_type.split('-')[0]
        self.area = area_type.split('-')[1]
        self.date = date
        super(DroughtDataGraph, self).__init__(metadata=metadata)

    def read(self):
        data = self.get_pie_data(data)
        layout = self.create_layout()
        return {"data": data, "layout": layout}

    @staticmethod
    def _get_labels(unparsed_stats_data):
        labels = list(unparsed_stats_data[0].keys())
        labels.remove('FileDate')
        labels.remove('NONE')
        labels.remove('ReleaseID')
        labels.remove('dsci')
        labels.remove('mapDate')
        labels.remove('statisticFormatId')
        labels.remove('usName')
        labels.remove('__type')
        return labels
    
    @staticmethod
    def _get_values(unparsed_stats_data):
        data_list=[
            unparsed_stats_data[0]['D0'],
            unparsed_stats_data[0]['D1'],
            unparsed_stats_data[0]['D2'],
            unparsed_stats_data[0]['D3'],
            unparsed_stats_data[0]['D4'],
        ]
        return data_list

    @staticmethod
    def _get_pie_colors():
        colors = [
            '#ffff00',
            '#fcd37f',
            '#ffaa00',
            '#e60000',
            '#730000'
        ]
        return colors
    
    def get_pie_data(self):
        try:
            client = httpx.Client(verify=False)
            params = {
                'area': f'"{self.area}"', 
                'type':f'"{self.area_type}"' , 
                'statstype': self.statistic_type
            }
            r = client.get(
                url=f"{self.api_base_url}_{self.area_type}",
                timeout=None,
                params=params
            )
            data = r.json()
            unparsed_stats_data = data.get('d', [])
            labels = self._get_labels(unparsed_stats_data)
            values = self._get_values(unparsed_stats_data)
            pie_data = [
               {
                    'labels': labels,
                    'values': values,
                    'type': 'pie',
                    'hoverinfo': 'label+percent',
                    'marker': {
                        'colors': self._get_pie_colors()
                    },
                    'automargin': True
               } 
            ]
            return pie_data
    
        except httpx.HTTPError as exc:
            logger.error(f"Error while requesting {exc.request.url!r}: {exc}")
            return []
    

        
    @staticmethod
    def create_layout():
        layout = {
            'height': 400,
            'width': 400,
            'margin': {"t": 0, "b": 0, "l": 0, "r": 0},
        }


        return layout