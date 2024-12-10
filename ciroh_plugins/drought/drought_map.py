from intake.source import base
import logging


# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


class DroughtMapViewer(base.DataSource):
    container = "python"
    version = "0.0.4"
    name = "drought_map_viewer"
    visualization_args = {}
    visualization_group = "Drought_Monitor"
    visualization_label = "Drought Monitor Map Viewer"
    visualization_type = "custom"

    def __init__(self,metadata=None):
        self.mfe_unpkg_url = "http://localhost:3000/remoteEntry.js"
        self.mfe_scope = "drought_map"
        self.mfe_module = "./MapComponent"
        super(DroughtMapViewer, self).__init__(metadata=metadata)

    def read(self):
        logger.info("Reading map data configuration")
        return {
            "url": self.mfe_unpkg_url,
            "scope": self.mfe_scope,
            "module": self.mfe_module,
            "props": {},
        }