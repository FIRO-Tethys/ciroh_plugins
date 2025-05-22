from intake.source import base
from .utilities import get_layers_dropdown
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class LayerFinder(base.DataSource):
    """
    A data source class for NWMP services, extending Intake's DataSource.
    """

    container = "python"
    version = "0.0.4"
    name = "nwmp_map_layer_finder"

    visualization_tags = ["map layers", "water", "water prediction", "flooding forecast"]
    visualization_description = (
        "Provides all available layers for the selected NWMP Map service"
    )
    visualization_args = {
        "service": "text",
    }
    visualization_group = "NWMP"
    visualization_label = "NWMP Map Layer Finder"
    visualization_type = "variable_input"

    def __init__(self, service, metadata=None):
        """
        Initialize the NWMPService data source.
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
        layers = get_layers_dropdown(self.service_key)
        return {
            "variable_name": "Layer Name",
            "initial_value": "0",
            "variable_options_source": layers,
        }
