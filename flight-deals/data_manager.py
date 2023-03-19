import requests
import os
from dotenv import load_dotenv

load_dotenv()


class DataManager:

    def __init__(self):
        self.API_ENDPOINT = "https://api.sheety.co/c072070d10ab71b6a7326784fb94992c/flightDeals/prices"
        self.TOKEN = os.environ["SHEETY_TOKEN"]
        self.headers = {
            "Authorization": f"Bearer {os.environ['SHEETY_TOKEN']}"
        }

    def get_flights(self):
        response = requests.get(url=self.API_ENDPOINT, headers=self.headers)
        response.raise_for_status()

        return response.json()["prices"]

    def update_flight(self, id: int, data):
        request_body = {
            "price": data
        }
        response = requests.put(url=f"{self.API_ENDPOINT}/{id}", json=request_body, headers=self.headers)
        response.raise_for_status()

        return response.json()

