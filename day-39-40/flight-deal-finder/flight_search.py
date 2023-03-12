class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, city_name):
        self.city_name = city_name

    def search(self):
        print(self.city_name)
        return "TESTING"
