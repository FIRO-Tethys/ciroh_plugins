from intake.source import base
import requests
import pandas as pd
import numpy as np
import httpx


import asyncio


# This will be used for the TimeSeries of the NWM data
class NWMPSSeries(base.DataSource):
    container = "python"
    version = "0.0.1"
    name = "nwmp_api"
    visualization_args = {
        "id": ["00000","222222","333333"],  # empty text it will be an variable input on the dashboard
    }
    visualization_group = "NWMP"
    visualization_label = "NWMP API"
    visualization_type = "plotly"

    def __init__(self, id, metadata=None):
        self.api_base_url = "https://api.water.noaa.gov/nwps/v1"
        self.id = id
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
            "medium_range_blend": "mediumRangeBlend"
        }
        self.type_id = "reaches"
        # store important kwargs
        super(NWMPSSeries, self).__init__(metadata=metadata)

    def read(self):
        self.getData()
        traces = self.create_plotly_data()
        print(traces)
        layout = self.create_plotly_layout()
        # needs to make  plotly chart placeholder for it
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
                print(f"Warning: The product '{product_name}' is None or not a dictionary. Skipping.")
                continue  # Skip to the next product

            # Iterate over simulations within each product
            for simulation_name, simulation in product.items():
                # Check if simulation is None or not a dictionary
                if simulation is None or not isinstance(simulation, dict):
                    print(f"Warning: The simulation '{simulation_name}' in product '{product_name}' is None or not a dictionary. Skipping.")
                    continue  # Skip to the next simulation

                # Extract data points
                data_points = simulation.get('data', [])
                if not data_points:
                    print(f"Warning: No data points found for simulation '{simulation_name}' in product '{product_name}'. Skipping.")
                    continue  # Skip if no data points are available

                # Extract 'validTime' and 'flow' for each data point
                x = [point.get('validTime') for point in data_points if 'validTime' in point]
                y = [point.get('flow') for point in data_points if 'flow' in point]

                # Check if x and y have data
                if not x or not y:
                    print(f"Warning: Missing 'validTime' or 'flow' in data points for simulation '{simulation_name}' in product '{product_name}'. Skipping.")
                    continue  # Skip if data is incomplete

                # Create a trace for this simulation
                trace = {
                    'x': x,
                    'y': y,
                    'type': 'scatter',
                    'mode': 'lines',
                    'name': f"{product_name} {simulation_name}",
                    'line': {'width': 2}
                }

                traces.append(trace)

        return traces


    def create_plotly_layout(self, title="Time Series Plot", yaxis_title="Flow", xaxis_title="Time"):
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
            for simulation_name, simulation in product.items():
                units = simulation.get('units')
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
            'title': {'text': title},
            'xaxis': {
                'title': {'text': xaxis_title},
                'type': 'date',  # Ensures the x-axis is treated as dates
                'tickformat': '%Y-%m-%d\n%H:%M',  # Format for date ticks
            },
            'yaxis': {
                'title': {'text': yaxis_title_with_units},
                'rangemode': 'tozero',  # Ensures y-axis starts at zero
            },
            'legend': {
                'orientation': 'h',  # Horizontal legend at the bottom
                'x': 0,
                'y': -0.2,
            },
            'margin': {
                'l': 50,
                'r': 50,
                't': 80,
                'b': 80,
            },
            'hovermode': 'x unified',  # Shows hover text for all traces at once
        }

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
                    self.reach_data[product] = response.json().get(self.matching_forecast[product], None)
                    return response.json()
        except Exception as e:
            print(e)
            return None  # Ensure the function returns a value


    async def make_reach_api_calls(self):
        tasks = []
        
        for product in self.reach_data.keys():
            task = asyncio.create_task(self.reach_api_call(product))
            tasks.append(task)
        # Await all tasks concurrently
        results = await asyncio.gather(*tasks)
        return results  

    async def make_gauge_api_calls(self):
        tasks = []
        task = asyncio.create_task(self.api_gauge_call())
        tasks.append(task)
        # Await all tasks concurrently
        results = await asyncio.gather(*tasks)
        return results 


    async def api_gauge_call(self):
        try:
            async with httpx.AsyncClient(verify=False) as client:
                response_await = await client.get(
                    url=f"{self.api_base_url}/gauges/{self.id}/stageflow",
                    timeout=None,
                )
                if response_await.status_code != 200:
                    print(f"Error: {response_await.status_code}")
                    print(response_await.text)
                    return None
                else:
                    return response_await.json()                
        except httpx.HTTPError as exc:
            print(f"Error while requesting {exc.request.url!r}.")
            print(str(exc.__class__.__name__))
            return None
        except Exception as e:
            return None


    async def make_api_calls(self):
        results = []
        if self.type_id == "reaches":
            results = await self.make_reach_api_calls()
        if self.type_id == "gauges":
            results = await self.make_gauge_api_calls()            
        return results
    

    def getData(self):
        try:
            # Capture the results from the async function
            results = asyncio.run(self.make_api_calls())
            return results  # Return the results
        except Exception as e:
            print(e)
            return None  # Ensure the function returns a value