import os
from dotenv import load_dotenv
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
from user_management import UserManagement

load_dotenv()
MY_CITY = os.environ["MY_CITY"]


data_manager = DataManager()
user_management = UserManagement()
flight_search = FlightSearch()
notification_manager = NotificationManager(users=user_management.get_users())


def update_flight_codes():
    flights = data_manager.get_flights()

    for flight in flights:
        flight_id, city_name = flight["id"], flight["city"]
        iata_code = flight_search.get_iata_code(term=city_name)
        data = {
            'iataCode': iata_code
        }
        data_manager.update_flight(flight_id, data)


def get_cheapest_flights():
    fly_to = ",".join(flight_dict.keys())

    return flight_search.get_cheapest_flights(from_city=MY_CITY, to_cities=fly_to)


def create_user():
    first_name = input("What is your first name? ")
    last_name = input("What is your last name? ")
    email = input("What is your email? ")

    data = {
        "firstname": first_name,
        "lastname": last_name,
        "email": email
    }

    print(user_management.create_user(data))


flights = data_manager.get_flights()
flight_dict = {flight["iataCode"]: flight for flight in flights}

cheapest_flights = get_cheapest_flights()

for flight_data in cheapest_flights:
    cityCodeTo, price = flight_data.cityCodeTo, flight_data.price
    if price < flight_dict[cityCodeTo]["lowestPrice"]:
        notification_manager.send_emails(flight_data)











