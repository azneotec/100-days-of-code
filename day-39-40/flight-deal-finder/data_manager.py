import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, sheety_endpoint, sheety_users_endpoint):
        self.sheety_endpoint = sheety_endpoint
        self.sheety_users_endpoint = sheety_users_endpoint
        self.destination_data = {}
        self.customer_data = {}

    def get_destination_data(self):
        response = requests.get(url=self.sheety_endpoint)
        response.raise_for_status()
        data = response.json()
        self.destination_data = data["prices"]
        # self.use_test_data()
        return self.destination_data

    def use_test_data(self):
        sheet_data = [
            {
                "iataCode": "",
                "city": "Paris",
                "id": "2",
                "lowest_Price": "54",
            },
            {
                "iataCode": "",
                "city": "Berlin",
                "id": "3",
                "lowest_Price": "42",
            }
        ]
        self.destination_data = sheet_data

    def set_destination_data(self, sheet_data):
        self.destination_data = sheet_data
        self.update_destination_codes()

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            update_endpoint = f"{self.sheety_endpoint}/{city['id']}"
            response = requests.put(url=update_endpoint, json=new_data)
            print(response.text)

    def get_customer_emails(self):
        customers_endpoint = self.sheety_users_endpoint
        response = requests.get(customers_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
