from intake.source import base
import requests
import pandas as pd
import numpy as np
from datetime import datetime, timedelta, timezone
import re



#This will be used for the TimeSeries of the NWM reach data
class Gauge(base.DataSource):
    container = "python"
    version = "0.0.1"
    name = "nwmp_gauge"
    visualization_args = {}
    visualization_group = "NWMP"
    visualization_label = "NWMP Gauge"
    visualization_type = "ploty"
    _user_parameters = []

    def __init__(self, metadata=None):
        # store important kwargs
        super(Gauge, self).__init__(metadata=metadata)

    def read(self):
        """Return a version of the xarray with all the data in memory"""
        pass