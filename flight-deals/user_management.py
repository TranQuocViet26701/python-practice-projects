import requests
import os
from dotenv import load_dotenv

load_dotenv()


class UserManagement:

    def __init__(self):
        self.API_ENDPOINT = "https://api.sheety.co/c072070d10ab71b6a7326784fb94992c/flightDeals/users"
        self.TOKEN = os.environ["SHEETY_TOKEN"]
        self.headers = {
            "Authorization": f"Bearer {os.environ['SHEETY_TOKEN']}"
        }

    def get_users(self):
        response = requests.get(url=self.API_ENDPOINT, headers=self.headers)
        response.raise_for_status()

        return response.json()["users"]

    def create_user(self, data):
        request_body = {
            "user": data
        }
        response = requests.post(url=self.API_ENDPOINT, json=request_body, headers=self.headers)
        response.raise_for_status()

        return response.json()
