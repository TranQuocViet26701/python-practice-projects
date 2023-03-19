import requests
from datetime import datetime

PIXELA_ENDPOINT = "https://pixe.la/v1/users"
TOKEN = "thisissecret"
USERNAME = "tranviet26701"
GRAPH_ID = "running-graph"


def create_user():
    user_config = {
        "token": TOKEN,
        "username": USERNAME,
        "agreeTermsOfService": "yes",
        "notMinor": "yes"
    }

    response = requests.post(url=PIXELA_ENDPOINT, json=user_config)
    response.raise_for_status()


def create_graph():
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    graph_config = {
        "id": GRAPH_ID,
        "name": "Running Graph",
        "unit": "Km",
        "type": "float",
        "color": "shibafu",
    }

    response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)
    response.raise_for_status()
    print(response)


def create_pixel():
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    date = datetime.now().strftime("%Y%m%d")
    graph_config = {
        "date": date,
        "quantity": "4.73",
    }

    response = requests.post(url=graph_endpoint, headers=headers, json=graph_config)
    response.raise_for_status()


def update_pixel(date, quantity: str):
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
    headers = {
        "X-USER-TOKEN": TOKEN
    }
    graph_config = {
        "quantity": quantity,
    }

    response = requests.put(url=graph_endpoint, headers=headers, json=graph_config)
    response.raise_for_status()


def delete_pixel(date):
    graph_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{date}"
    headers = {
        "X-USER-TOKEN": TOKEN
    }

    response = requests.delete(url=graph_endpoint, headers=headers)
    response.raise_for_status()






