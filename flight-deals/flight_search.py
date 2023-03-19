from typing import List
import requests
from datetime import datetime, timedelta
from flight_data import FlightData
import os
from dotenv import load_dotenv
from pprint import pprint

load_dotenv()

TEQUILA_API_KEY = os.environ["TEQUILA_API_KEY"]


class FlightSearch:

    def __init__(self):
        self.API_ENDPOINT = "https://api.tequila.kiwi.com"
        self.API_KEY = os.environ["TEQUILA_API_KEY"]
        self.headers = {
            "apikey": os.environ["TEQUILA_API_KEY"]
        }

    def get_iata_code(self, term):
        params = {
            "term": term
        }
        response = requests.get(url=f"{self.API_ENDPOINT}/locations/query", headers=self.headers, params=params)
        response.raise_for_status()

        try:
            code = response.json()["locations"][0]["code"]
        except KeyError or IndexError:
            return ""
        else:
            return code

    def get_cheapest_flights(self, from_city, to_cities) -> List[FlightData]:
        time_now = datetime.now()
        date_from = time_now.strftime("%d/%m/%Y")
        date_to = (time_now + timedelta(days= 6 * 30)).strftime("%d/%m/%Y")
        params = {
            "fly_from": from_city,
            "fly_to": to_cities,
            "date_from": date_from,
            "date_to": date_to,
            "one_for_city": 1,
            "curr": "USD",
            "locale": "us"
        }
        response = requests.get(url=f"{self.API_ENDPOINT}/v2/search", headers=self.headers, params=params)
        response.raise_for_status()

        return [FlightData(id=flight["id"],
                           cityFrom=flight["cityFrom"],
                           cityCodeFrom=flight["cityCodeFrom"],
                           cityTo=flight["cityTo"],
                           cityCodeTo=flight["cityCodeTo"],
                           price=flight["price"],
                           local_arrival=flight["local_arrival"],
                           local_departure=flight["local_departure"],
                           route=flight["route"])
                for flight in response.json()["data"]]

