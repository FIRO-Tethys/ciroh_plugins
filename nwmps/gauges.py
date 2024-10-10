from intake.source import base
import httpx
import datetime


# This will be used for the TimeSeries of the NWM data
class NWMPSGaugesSeries(base.DataSource):
    container = "python"
    version = "0.0.1"
    name = "nwmp_api"
    visualization_args = {"id": "text", "units": ["primary", "secondary"]}
    visualization_group = "NWMP"
    visualization_label = "NWMP Gauges Time Series"
    visualization_type = "plotly"

    def __init__(self, id, units, metadata=None):
        self.api_base_url = "https://api.water.noaa.gov/nwps/v1"
        self.id = id
        self.units = units
        self.data = None
        # store important kwargs
        super(NWMPSGaugesSeries, self).__init__(metadata=metadata)

    def read(self):
        self.data = self.get_gauge_data()
        traces = self.create_traces()
        layout = self.create_layout()
        return {"data": traces, "layout": layout}

    @staticmethod
    def process_dataset(dataset, dataset_name, data_type):
        traces = []
        data = dataset.get("data", [])
        times = [
            datetime.datetime.fromisoformat(
                d["validTime"].replace("Z", "+00:00")
            ).isoformat()
            for d in data
        ]

        # Process data based on data_type
        if data_type in ("primary", "secondary"):
            values = [d.get(data_type, None) for d in data]
            trace = {
                "x": times,
                "y": values,
                "mode": "lines+markers",
                "name": f"{dataset_name} {dataset.get(data_type + 'Name', data_type.capitalize())}",
                "yaxis": "y1",  # Using yaxis since only one y-axis is configured
            }
            traces.append(trace)
        else:
            raise ValueError("data_type must be 'primary' or 'secondary'")
        return traces

    # Helper function to extract name and units for the specified data_type
    @staticmethod
    def extract_name_units(dataset, data_type):
        if data_type == "primary":
            return (dataset.get("primaryName", ""), dataset.get("primaryUnits", ""))
        else:
            return (dataset.get("secondaryName", ""), dataset.get("secondaryUnits", ""))

    def create_traces(self):
        """
        Creates JSON-serializable traces for the provided time series data.

        Parameters:
            data_response (dict): The data containing 'observed' and/or 'forecast' time series.

        Returns:
            list: A list of dictionaries representing Plotly traces.
        """

        traces = []

        # Process 'observed' data if present
        if "observed" in self.data:
            traces = self.process_dataset(self.data["observed"], "Observed", self.units)
        # Process 'forecast' data if present
        if "forecast" in self.data:
            traces = self.process_dataset(self.data["forecast"], "Forecast", self.units)

        return traces

    def create_layout(self):
        """
        Creates a JSON-serializable layout for the time series chart based on the specified data type.

        Returns:
            dict: A dictionary representing the Plotly layout.
        """
        # Initialize default axis title and units
        name = ""
        units = ""

        # Extract name and units from 'observed' or 'forecast' data
        if "observed" in self.data and f"{self.units}Name" in self.data["observed"]:
            name, units = self.extract_name_units(self.data["observed"], self.units)
        elif "forecast" in self.data and f"{self.units}Name" in self.data["forecast"]:
            name, units = self.extract_name_units(self.data["forecast"], self.units)
        else:
            # Default values if names are not available
            name = self.units.capitalize()
            units = ""

        # Configure the y-axis based on the selected data_type
        layout = {
            "title": "Time Series Plot",
            "xaxis": {"title": "Time"},
            "yaxis": {"title": f"{name} ({units})".strip(), "side": "left"},
            "legend": {"x": 0, "y": 1.1, "orientation": "h"},
            "margin": {"l": 50, "r": 50, "t": 50, "b": 50},
            "hovermode": "x unified",
        }
        return layout

    def get_gauge_data(self):
        try:
            with httpx.Client(verify=False) as client:
                r = client.get(
                    url=f"{self.api_base_url}/gauges/{self.id}/stageflow",
                    timeout=None,
                )
                if r.status_code != 200:
                    print(f"Error: {r.status_code}")
                    print(r.text)
                    return None
                else:
                    return r.json()
        except httpx.HTTPError as exc:
            print(f"Error while requesting {exc.request.url!r}.")
            print(str(exc.__class__.__name__))
            return None
        except Exception:
            return None
