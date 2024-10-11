from intake.source import base
import requests
import httpx
import asyncio
from .utilities import get_metadata_from_api


class NWMPSReachesSeries(base.DataSource):
    container = "python"
    version = "0.0.1"
    name = "nwmp_api"
    visualization_args = {
        "id": "text",
    }
    visualization_group = "NWMP"
    visualization_label = "NWMP Reaches Time Series"
    visualization_type = "plotly"

    def __init__(self, id, metadata=None):
        self.api_base_url = "https://api.water.noaa.gov/nwps/v1"
        self.id = id
        self.metadata = None
        self.reach_data = {
            "analysis_assimilation": None,
            "short_range": None,
            "medium_range": None,
            "long_range": None,
            "medium_range_blend": None,
        }
        self.matching_forecast = {
            "analysis_assimilation": "analysisAssimilation",
            "short_range": "shortRange",
            "medium_range": "mediumRange",
            "long_range": "longRange",
            "medium_range_blend": "mediumRangeBlend",
        }
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        super(NWMPSReachesSeries, self).__init__(metadata=metadata)

    def read(self):
        self.metadata = get_metadata_from_api(self.api_base_url, self.id, "reaches")
        if self.metadata is not None:
            self.getData()
        traces = self.create_plotly_data()
        layout = self.create_plotly_layout()
        return {"data": traces, "layout": layout}

    def create_plotly_data(self):
        """
        Process the data object to create a list of traces for Plotly.js.

        Parameters:
        - data_object (dict): The input data containing time series information.

        Returns:
        - list: A list of trace dictionaries suitable for Plotly.js.
        """
        traces = []
        # Iterate over forecast products
        for product_name, product in self.reach_data.items():
            if product_name == "reach":
                continue  # Skip the 'reach' key as it doesn't contain time series data

            # Check if product is None or not a dictionary
            if product is None or not isinstance(product, dict):
                print(
                    f"Warning: The product '{product_name}' is None or not a dictionary. Skipping."
                )
                continue  # Skip to the next product

            # Iterate over simulations within each product
            for simulation_name, simulation in product.items():
                # Check if simulation is None or not a dictionary
                if simulation is None or not isinstance(simulation, dict):
                    print(
                        f"Warning: The simulation '{simulation_name}' in product '{product_name}' is None or not a dictionary. Skipping."
                    )
                    continue  # Skip to the next simulation

                # Extract data points
                data_points = simulation.get("data", [])
                if not data_points:
                    print(
                        f"Warning: No data points found for simulation '{simulation_name}' in product '{product_name}'. Skipping."
                    )
                    continue  # Skip if no data points are available

                # Extract 'validTime' and 'flow' for each data point
                x = [
                    point.get("validTime")
                    for point in data_points
                    if "validTime" in point
                ]
                y = [point.get("flow") for point in data_points if "flow" in point]

                # Check if x and y have data
                if not x or not y:
                    print(
                        f"Warning: Missing 'validTime' or 'flow' in data points for simulation '{simulation_name}' in product '{product_name}'. Skipping."
                    )
                    continue  # Skip if data is incomplete

                # Create a trace for this simulation
                trace = {
                    "x": x,
                    "y": y,
                    "type": "scatter",
                    "mode": "lines",
                    "name": f"{product_name} {simulation_name}",
                    "line": {"width": 2},
                }

                traces.append(trace)

        return traces

    def create_plotly_layout(self, yaxis_title="Flow"):
        """
        Create a layout dictionary for Plotly.js based on the data object.

        Parameters:
        - data_object (dict): The input data containing time series information.
        - title (str): The title of the plot.
        - yaxis_title (str): The label for the y-axis.
        - xaxis_title (str): The label for the x-axis.

        Returns:
        - dict: A layout dictionary suitable for Plotly.js.
        """
        # Extract units from the data_object if available
        units = None
        for product_name, product in self.reach_data.items():
            if product_name == "reach":
                continue  # Skip the 'reach' key

            if product is None or not isinstance(product, dict):
                continue  # Skip to the next product

            for simulation_name, simulation in product.items():
                units = simulation.get("units")
                if units:
                    break  # Use the first available units
            if units:
                break

        # Set y-axis title with units if available
        if units:
            yaxis_title_with_units = f"{yaxis_title} ({units})"
        else:
            yaxis_title_with_units = yaxis_title

        layout = {
            "title": "<b>Reach</b>: {} <br><sub>ID:{} </sub>".format(
                (
                    self.metadata.get("name", "Unknown")
                    if self.metadata.get("name", "Unknown") != ""
                    else "Unknown"
                ),
                self.id,
            ),
            "xaxis": {
                "type": "date",  # Ensures the x-axis is treated as dates
                "tickformat": "%Y-%m-%d\n%H:%M",  # Format for date ticks
            },
            "yaxis": {
                "title": {"text": yaxis_title_with_units},
                "rangemode": "tozero",  # Ensures y-axis starts at zero
            },
            "legend": {
                "orientation": "h",  # Horizontal legend at the bottom
                "x": 0,
                "y": -0.2,
            },
            "margin": {
                "l": 50,
                "r": 50,
                "t": 80,
                "b": 80,
            },
            "hovermode": "x unified",  # Shows hover text for all traces at once
        }

        # + "<br>"
        # + {"text": f"id: {self.id}"},
        return layout

    async def reach_api_call(self, product):
        try:
            async with httpx.AsyncClient(verify=False) as client:
                response = await client.get(
                    url=f"{self.api_base_url}/reaches/{self.id}/streamflow",
                    params={"series": product},
                    timeout=None,
                )
                print(f"Request URL: {product}", response.status_code)

                if response.status_code != 200:
                    print(f"Error: {response.status_code}")
                    print(response.text)
                    return None
                else:
                    self.reach_data[product] = response.json().get(
                        self.matching_forecast[product], None
                    )
                    return response.json()
        except Exception as e:
            print(e)
            return None

    async def make_reach_api_calls(self, products):
        tasks = []
        for product in products:
            task = self.reach_api_call(product)
            tasks.append(task)
        results = await asyncio.gather(*tasks)
        return results

    def getData(self):
        try:
            products = self.reach_data.keys()
            # Run the coroutine using the event loop
            results = self.loop.run_until_complete(self.make_reach_api_calls(products))
            return results
        except Exception as e:
            print(e)
            return None
