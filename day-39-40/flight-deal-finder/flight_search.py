import requests


class FlightSearch:
    # This class is responsible for talking to the Flight Search API.
    def __init__(self, location_query_endpoint, api_key):
        self.location_query_endpoint = location_query_endpoint
        self.api_key = api_key

    def search(self, city_name):
        search_data = {
            "term": city_name,
            "locale": "en-US",
            "location_types": "airport",
            "limit": "10",
            "active_only": "true",
        }
        headers = {
            "accept": "application/json",
            "apikey": self.api_key,
        }
        response = requests.get(
            url=self.location_query_endpoint,
            params=search_data,
            headers=headers
        )
        response.raise_for_status()
        iata_code = response.json()["locations"][0]["city"]["code"]
        return iata_code
