import os
from twilio.rest import Client
from flight_data import FlightData
from dotenv import load_dotenv
import smtplib

load_dotenv()
MY_EMAIL = os.environ["MY_EMAIL"]
MY_STMP_PASSWORD = os.environ["MY_STMP_PASSWORD"]


class NotificationManager:

    def __init__(self, users=[]):
        account_sid = "AC506a201011e6ede329c1abc7c3d61dd2"
        auth_token = os.environ["TWILIO_AUTH_TOKEN"]
        self.client = Client(account_sid, auth_token)
        self.users = users

    def send_low_price(self, flight: FlightData):
        body = f"Low price alert! Only {flight.price}$ to fly from " \
               f"{flight.cityFrom}-{flight.cityCodeFrom} to {flight.cityTo}-{flight.cityCodeTo}, " \
               f"from {flight.local_departure.split('T')[0]} to {flight.local_arrival.split('T')[0]}."
        message = self.client.messages.create(
            body=body,
            from_="+15673392760",
            to="+84365896447"
        )
        print(message.sid)

    def send_emails(self, flight: FlightData):
        user_emails = [user["email"] for user in self.users]

        stop_over = "" if flight.stop_over == 0 \
            else f"\nFlight has {flight.stop_over} stop over, via {', '.join(flight.via_city)}."

        link = f"https://www.google.com/flights?flt={flight.cityCodeFrom}.{flight.cityCodeTo}.{flight.local_departure.split('T')[0]}" \
               f"*{flight.cityCodeTo}.{flight.cityCodeFrom}.{flight.local_departure.split('T')[0]}"

        message = f"Subject:New Low Price Flight!\n\nLow price alert! Only {flight.price}$ to fly from " \
               f"{flight.cityFrom}-{flight.cityCodeFrom} to {flight.cityTo}-{flight.cityCodeTo}, " \
               f"from {flight.local_departure.split('T')[0]} to {flight.local_arrival.split('T')[0]}.\n{stop_over}\n{link}"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_STMP_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL, to_addrs=user_emails, msg=message)
