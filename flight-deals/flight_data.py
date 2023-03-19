from pprint import pprint

class FlightData:

    def __init__(self, route=[], **kwargs):
        self.id = kwargs["id"]
        self.cityFrom = kwargs["cityFrom"]
        self.cityCodeFrom = kwargs["cityCodeFrom"]
        self.cityTo = kwargs["cityTo"]
        self.cityCodeTo = kwargs["cityCodeTo"]
        self.price = kwargs["price"]
        self.local_arrival = kwargs["local_arrival"]
        self.local_departure = kwargs["local_departure"]
        self.via_city = [flight["cityTo"] for flight in route][:-1]
        self.stop_over = len(self.via_city)

