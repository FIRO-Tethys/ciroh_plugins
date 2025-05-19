from intake.source import base
import logging
from .utilities import get_layers_dropdown

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DroughtMapLayerFinder(base.DataSource):
    """
    A data source class for NWMP services, extending Intake's DataSource.
    """

    container = "python"
    version = "0.0.4"
    name = "drought_map_layer_finder"

    visualization_tags = ["national", "water", "model"]
    visualization_description = (
        "Provides a summary of RFC gauges inside a HUC and their current flood status"
    )
    visualization_args = {
        "service": "text",
    }
    visualization_group = "Drought_Monitor"
    visualization_label = "Drought Map Layer Finder"
    visualization_type = "variable_input"

    def __init__(self, service, metadata=None):
        """
        Initialize the drought map layer finder.
        """
        self.service_url = service
        if service.endswith('/'):
            self.service_url = service[:-1]
        self.service_key = self.service_url.split('/')[-2]
        super().__init__(metadata=metadata)

    def read(self):
        """
        Read data from NWMP service and return a dictionary with title, data, and description.
        """
        layer_names = get_layers_dropdown(self.service_key)

        return {
            "variable_name": "Layer Name",
            "initial_value": "0",
            "variable_options_source": layer_names,
        }
