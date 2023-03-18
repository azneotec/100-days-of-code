# This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the
# program requirements.
import os
from datetime import datetime, timedelta
from notification_manager import NotificationManager

from data_manager import DataManager
from flight_search import FlightSearch

SHEETY_API_ENDPOINT = os.environ["SHEETY_API_ENDPOINT"]
KIWI_API_ENDPOINT = os.environ["KIWI_LOCATION_SEARCH_API_ENDPOINT"]
KIWI_API_KEY = os.environ["KIWI_API_KEY"]
ORIGIN_CITY_IATA = "LON"
ORIGIN_CITY_CURRENCY = "GBP"
# ORIGIN_CITY_IATA = "SIN"
# ORIGIN_CITY_CURRENCY = "SGD"

data_manager = DataManager(SHEETY_API_ENDPOINT)
flight_search = FlightSearch(KIWI_API_ENDPOINT, KIWI_API_KEY)
notification_manager = NotificationManager()
update_destination_data = False

sheet_data = data_manager.get_destination_data()
for sheet in sheet_data:
    if sheet["iataCode"] == "":
        result = flight_search.get_destination_code(sheet["city"])
        sheet["iataCode"] = result
        update_destination_data = True

if update_destination_data:
    data_manager.set_destination_data(sheet_data)

today = datetime.now()
tomorrow = today + timedelta(days=1)
six_month_from_today = today + timedelta(days=(6 * 30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        origin_city_code=ORIGIN_CITY_IATA,
        destination_city_code=destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today,
        currency=ORIGIN_CITY_CURRENCY
    )

    if flight is None:
        continue

    if flight.price < destination["lowestPrice"]:
        message = f"Low price alert! Only £{flight.price} to fly from " \
                  f"{flight.origin_city}-{flight.origin_airport} to " \
                  f"{flight.destination_city}-{flight.destination_airport}, " \
                  f"from {flight.out_date} to {flight.return_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        notification_manager.send_sms(message)
