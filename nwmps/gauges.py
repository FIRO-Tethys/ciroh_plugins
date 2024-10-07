from intake.source import base
import requests
import pandas as pd
import numpy as np
import httpx


import asyncio


# This will be used for the TimeSeries of the NWM data
class NWMPSGaugesSeries(base.DataSource):
    container = "python"
    version = "0.0.1"
    name = "nwmp_api"
    visualization_args = {
        "id": [
            "000000",
        ],  # empty text it will be an variable input on the dashboard
    }
    visualization_group = "NWMP"
    visualization_label = "NWMP Gauges Time Series"
    visualization_type = "plotly"

    def __init__(self, id, metadata=None):
        self.api_base_url = "https://api.water.noaa.gov/nwps/v1"
        self.id = id
        # store important kwargs
        super(NWMPSGaugesSeries, self).__init__(metadata=metadata)

    def read(self):
        self.getData()
        pass

    def create_plotly_data(self):
        pass

    def create_plotly_layout(self, yaxis_title="Flow", xaxis_title="Time"):
        pass

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
