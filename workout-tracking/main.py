import requests
from datetime import datetime
import os
from dotenv import load_dotenv

load_dotenv()

API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_API_ENDPOINT = "https://api.sheety.co/c072070d10ab71b6a7326784fb94992c/workoutTracking/workouts"


def get_workouts():
    headers = {
        "Authorization": f"Bearer {os.environ['SHEETY_ACCESS_TOKEN']}"
    }
    response = requests.get(url=SHEETY_API_ENDPOINT, headers=headers)
    response.raise_for_status()

    return response.json()


def create_workout(**kwargs):
    headers = {
        "Authorization": f"Bearer {os.environ['SHEETY_ACCESS_TOKEN']}"
    }
    time_now = datetime.now()
    request_body = {
        "workout": {
            "date": time_now.strftime("%d/%m/%Y"),
            "time": time_now.strftime("%X"),
            "exercise": kwargs["exercise"],
            "duration": kwargs["duration"],
            "calories": kwargs["calories"]
        }
    }

    response = requests.post(url=SHEETY_API_ENDPOINT, headers=headers, json=request_body)
    response.raise_for_status()


def make_natural_exercise_query(query: str):
    headers = {
        "x-app-id": os.environ["APP_ID"],
        "x-app-key": os.environ["API_KEY"],
        "Content-Type": "application/json"
    }

    request_body = {
        "query": query,
        "gender": "male",
        "weight_kg": 65,
        "height_cm": 175,
        "age": 22
    }

    response = requests.post(url=API_ENDPOINT, headers=headers, json=request_body)
    response.raise_for_status()

    return response.json()["exercises"]


is_on = True
while is_on:
    user_input = input("Tell me what exercise you did (or ./exit to exit): ")
    if user_input == "./exit":
        is_on = False
    else:
        exercises = make_natural_exercise_query(user_input)
        for exercise in exercises:
            create_workout(exercise=exercise["name"].title(),
                           duration=exercise["duration_min"],
                           calories=exercise["nf_calories"])

        print(get_workouts())

