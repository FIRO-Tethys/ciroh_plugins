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
        "id": "000000",  # empty text it will be an variable input on the dashboard
    }
    visualization_group = "NWMP"
    visualization_label = "NWMP API"
    visualization_type = "ploty"

    def __init__(self, id, metadata=None):
        self.base_pi_url = "https://api.water.noaa.gov/nwps/v1"
        self.id = id
        # store important kwargs
        super(NWMPSSeries, self).__init__(metadata=metadata)

    def read(self):
        print("Reading data from NWMPSSeries")
        data = self.getReachData()
        # needs to make  plotly chart placeholder for it
        return {"data": [], "layout": {}}

    # make functions to check if it is a gauge or a reach
    # make functions for the gauge data
    # make placeholder plotly chart for the gauge data

    async def api_call(self, api_base_url, method_name):
        try:
            async with httpx.AsyncClient(verify=False) as client:
                response = await client.get(
                    url=f"{api_base_url}/reaches/{self.id}/streamflow",
                    params={"series": method_name},
                    timeout=None,
                )
                print(f"Request URL: {api_base_url}/reaches/{self.id}/streamflow")
                if response.status_code != 200:
                    print(f"Error: {response.status_code}")
                    print(response.text)
                    return None
                else:
                    return response.json()
        except Exception as e:
            print("api_call error")
            print(e)
            return None  # Ensure the function returns a value

    async def make_api_calls(self, api_base_url, products):
        tasks = []
        for product in products:
            task = asyncio.create_task(self.api_call(api_base_url, product))
            tasks.append(task)
        # Await all tasks concurrently
        results = await asyncio.gather(*tasks)
        return results  # Return the list of results

    def getReachData(self):
        products = [
            "analysis_assimilation",
            "short_range",
            "medium_range",
            "long_range",
            "medium_range_blend",
        ]
        try:
            api_base_url = self.base_pi_url
            # Capture the results from the async function
            results = asyncio.run(self.make_api_calls(api_base_url, products))
            return results  # Return the results
        except Exception as e:
            print("getReachData error")
            print(e)
            return None  # Ensure the function returns a value
