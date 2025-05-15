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
    name = "nwmp_data_service"

    visualization_tags = ["national", "water", "model", "nwm", "gauge", "flood"]
    visualization_description = (
        "Provides a summary of RFC gauges inside a HUC and their current flood status"
    )
    visualization_args = {
        "service": "text",
    }
    visualization_group = "NWMP"
    visualization_label = "NWMP Layer Finder"
    visualization_type = "variable_input"

    def __init__(self, service, metadata=None):
        """
        Initialize the NWMPService data source.
        """
        self.service_url = service
        super().__init__(metadata=metadata)

    def read(self):
        """
        Read data from NWMP service and return a dictionary with title, data, and description.
        """
        layer_names = get_layers_dropdown(self.service_url)

        return {
            "variable_name": "Layer Name",
            "initial_value": "0",
            "variable_options_source": layer_names,
        }
