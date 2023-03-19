import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv

load_dotenv()
api_key = os.environ.get("API_KEY")
my_lat = 10.848160
my_long = 106.772520
account_sid = os.environ.get("ACCOUNT_SID")
auth_token = os.environ.get("AUTH_TOKEN")
client = Client(account_sid, auth_token)

params = {
    "lat": my_lat,
    "lon": my_long,
    "appid": api_key
}
api_endpoint = "https://api.openweathermap.org/data/2.5/forecast"

response = requests.get(url=api_endpoint, params=params)
response.raise_for_status()

# Weather in next 12 hour
weather_slice = response.json()["list"][:3]
will_rain = False

for data in weather_slice:
    weather = data["weather"]
    print(weather)
    if weather[0]["id"] > 700:
        will_rain = True


if will_rain:
    print("Bring an umbrella.")
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔️",
        from_="+15673392760",
        to="+84365896447"
    )
    print(message.sid)



