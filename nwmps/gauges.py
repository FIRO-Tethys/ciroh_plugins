from intake.source import base
import httpx
from .utilities import get_metadata_from_api

# import datetime
import pandas as pd
from datetime import datetime


# This will be used for the TimeSeries of the NWM data
class NWMPSGaugesSeries(base.DataSource):
    container = "python"
    version = "0.0.1"
    name = "nwmp_api"
    visualization_args = {"id": "text"}
    visualization_group = "NWMP"
    visualization_label = "NWMP Gauges Time Series"
    visualization_type = "plotly"

    def __init__(self, id, metadata=None):
        self.api_base_url = "https://api.water.noaa.gov/nwps/v1"
        self.id = id
        self.data = None
        self.metadata = None
        # store important kwargs
        super(NWMPSGaugesSeries, self).__init__(metadata=metadata)

    def read(self):
        self.data = self.get_gauge_data()
        self.metadata = get_metadata_from_api(self.api_base_url, self.id, "gauges")
        traces = self.create_traces()
        # Generate flood event shapes and annotations
        flood_data = self.metadata.get("flood", {})
        shapes, annotations = self.create_flood_events(flood_data)
        secondary_range = self.get_secondary_data_range(self.data)
        # Generate layout
        layout = self.create_layout(shapes, annotations, secondary_range)
        return {"data": traces, "layout": layout}

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

    def create_traces(self):
        """
        Creates JSON-serializable traces for the provided time series data.

        Parameters:
            data (dict): The data containing 'observed' and/or 'forecast' time series.

        Returns:
            list: A list of dictionaries representing Plotly traces.
        """
        traces = []

        # List of possible datasets
        datasets = ["observed", "forecast"]

        for dataset_name in datasets:
            if dataset_name in self.data:
                dataset = self.data[dataset_name]
                data_points = dataset.get("data", [])
                times = [d["validTime"] for d in data_points]
                primary_values = [d.get("primary", None) for d in data_points]
                secondary_values = [d.get("secondary", None) for d in data_points]

                # Create hover text
                hover_text = []
                for t, p, s in zip(times, primary_values, secondary_values):
                    utc_time = datetime.strptime(t, "%Y-%m-%dT%H:%M:%SZ")
                    formatted_time = utc_time.strftime("%a %B %d %Y %I:%M:%S %p")
                    text = (
                        f"Time: {formatted_time}<br>{dataset.get('primaryUnits')}: {p}"
                    )
                    if s is not None and s >= 0:
                        text += f"<br>{dataset.get('secondaryUnits')}: {s}"
                    hover_text.append(text)

                # Define the trace
                trace = {
                    "x": times,
                    "y": primary_values,
                    "mode": "lines",
                    "name": dataset_name.capitalize(),
                    "yaxis": "y1",  # Assign to primary y-axis
                    "hoverinfo": "text",
                    "text": hover_text,
                }

                traces.append(trace)

                traceFake = {"x": times[0], "y": [0], "yaxis": "y2", "visible": False}
                traces.append(traceFake)

        return traces

    @staticmethod
    def create_flood_events(flood_data):
        """
        Creates Plotly-compatible shapes and annotations for flood events.

        Parameters:
            flood_data (dict): The flood data containing 'categories' with 'stage' values.

        Returns:
            tuple: Two lists containing shapes and annotations respectively.
        """
        shapes = []
        annotations = []

        if "categories" not in flood_data:
            return shapes, annotations  # Return empty lists if no categories

        categories = flood_data["categories"]
        # Define a color mapping for flood categories
        category_colors = {
            "action": "orange",
            "minor": "yellow",
            "moderate": "red",
            "major": "purple",
        }

        for category, details in categories.items():
            stage = details.get("stage", None)
            if stage is not None:
                # Add a horizontal dashed line for the flood stage
                shapes.append(
                    {
                        "type": "line",
                        "x0": 0,
                        "x1": 1,
                        "xref": "paper",
                        "y0": stage,
                        "y1": stage,
                        "yref": "y1",
                        "line": {
                            "color": category_colors.get(category.lower(), "black"),
                            "width": 2,
                            "dash": "dash",
                        },
                    }
                )

                # Add an annotation (label) for the flood stage
                annotations.append(
                    {
                        "x": 0,  # Position at the far right of the plot
                        "y": stage,
                        "xref": "paper",
                        "yref": "y1",
                        "text": f"{stage} {flood_data.get('stageUnits', '')} - {category}".strip(),
                        "showarrow": False,
                        "xanchor": "left",
                        "yanchor": "bottom",
                        "font": {
                            "color": "black",
                            "size": 12,
                        },
                    }
                )

        return shapes, annotations

    @staticmethod
    def get_secondary_data_range(data):
        """
        Computes the minimum and maximum of all secondary values across 'observed' and 'forecast' datasets.

        Parameters:
            data (dict): The data containing 'observed' and/or 'forecast' time series.

        Returns:
            tuple: A tuple containing (min_secondary, max_secondary).
        """
        secondary_values = []

        # List of possible datasets
        datasets = ["observed", "forecast"]

        for dataset_name in datasets:
            if dataset_name in data:
                dataset = data[dataset_name]
                data_points = dataset.get("data", [])
                for d in data_points:
                    s = d.get("secondary", None)
                    if s is not None:
                        secondary_values.append(s)

        if not secondary_values:
            # Default range if no secondary data is present
            return (0, 1)
        else:
            min_secondary = min(secondary_values)
            max_secondary = max(secondary_values)
            # Add some padding to the range
            padding = (
                (max_secondary - min_secondary) * 0.1
                if max_secondary != min_secondary
                else 1
            )
            return (min_secondary - padding, max_secondary + padding)

    # Helper function to extract names and units
    @staticmethod
    def extract_names_units(dataset, data_type):
        if data_type == "primary":
            return (dataset.get("primaryName", ""), dataset.get("primaryUnits", ""))
        elif data_type == "secondary":
            return (
                dataset.get("secondaryName", ""),
                dataset.get("secondaryUnits", ""),
            )
        else:
            raise ValueError("data_type must be 'primary' or 'secondary'")

    def create_layout(self, shapes, annotations, secondary_range):
        """
        Creates a JSON-serializable layout for the time series chart, including flood event lines.

        Parameters:
            data (dict): The data containing 'observed' and/or 'forecast' for axis labels.
            shapes (list): A list of Plotly shape dictionaries for flood events.
            annotations (list): A list of Plotly annotation dictionaries for flood event labels.
            secondary_range (tuple): A tuple containing (min_secondary, max_secondary) for yaxis2.

        Returns:
            dict: A dictionary representing the Plotly layout.
        """
        # Initialize default axis titles and units
        primary_name = ""
        primary_units = ""
        secondary_name = ""
        secondary_units = ""

        # Extract names and units from 'observed' or 'forecast' data
        if "observed" in self.data:
            primary_name, primary_units = self.extract_names_units(
                self.data["observed"], "primary"
            )
            secondary_name, secondary_units = self.extract_names_units(
                self.data["observed"], "secondary"
            )
        elif "forecast" in self.data:
            primary_name, primary_units = self.extract_names_units(
                self.data["forecast"], "primary"
            )
            secondary_name, secondary_units = self.extract_names_units(
                self.data["forecast"], "secondary"
            )
        else:
            primary_name = "Primary"
            primary_units = ""
            secondary_name = "Secondary"
            secondary_units = ""

        layout = {
            "title": "<b>Gauge</b>: {} <br><sub>ID:{}</sub>".format(
                self.metadata.get("name", "Unknown"), self.id
            ),
            "xaxis": {"tickformat": "%I %p<br>%b %d"},
            "yaxis": {
                "title": f"{primary_name} ({primary_units})".strip(),
                "side": "left",
            },
            "yaxis2": {
                "title": f"{secondary_name} ({secondary_units})".strip(),
                "side": "right",
                "overlaying": "y",
                "showgrid": False,
                "range": secondary_range,  # Set the range based on secondary data
            },
            "legend": {
                "orientation": "h",  # Horizontal legend at the bottom
                "x": 0,
                "y": -0.2,
            },
            "margin": {"l": 50, "r": 50, "t": 50, "b": 50},
            "hovermode": "x unified",
            "shapes": shapes,  # Incorporate flood event lines
            "annotations": annotations,  # Incorporate flood event labels
        }

        return layout
