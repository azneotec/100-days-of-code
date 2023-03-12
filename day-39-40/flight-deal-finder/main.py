# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
import requests, os
from pprint import pprint
from flight_search import FlightSearch
from data_manager import DataManager

SHEETY_API_ENDPOINT = os.environ["SHEETY_API_ENDPOINT"]
KIWI_LOCATION_SEARCH_API_ENDPOINT = os.environ["KIWI_LOCATION_SEARCH_API_ENDPOINT"]
KIWI_API_KEY = os.environ["KIWI_API_KEY"]

data_manager = DataManager(SHEETY_API_ENDPOINT)
flight_search = FlightSearch(KIWI_LOCATION_SEARCH_API_ENDPOINT, KIWI_API_KEY)

flight_deals_prices_response = requests.get(url=SHEETY_API_ENDPOINT)
flight_deals_prices_response.raise_for_status()
sheet_data = flight_deals_prices_response.json()["prices"]
# sheet_data = [
#     {
#         "iataCode": "",
#         "city": "Paris",
#         "id": "2",
#         "lowest_Price": "54",
#     },
#     {
#         "iataCode": "",
#         "city": "Berlin",
#         "id": "3",
#         "lowest_Price": "42",
#     }
# ]
pprint(sheet_data)

for sheet in sheet_data:
    if sheet["iataCode"] == "":
        result = flight_search.search(sheet["city"])
        sheet["iataCode"] = result

        flight_deals_price_data = {
            "price": {
                "iataCode": result,
            }
        }
        flight_deals_prices_updated_response = data_manager.update_sheet(sheet["id"], flight_deals_price_data)

print("\n")
pprint(sheet_data)
