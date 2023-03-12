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

sheet_data = data_manager.get_destination_data()
pprint(sheet_data)

update_destination_data = False
for sheet in sheet_data:
    if sheet["iataCode"] == "":
        result = flight_search.search(sheet["city"])
        sheet["iataCode"] = result
        update_destination_data = True

if update_destination_data:
    pprint(sheet_data)
    data_manager.set_destination_data(sheet_data)
