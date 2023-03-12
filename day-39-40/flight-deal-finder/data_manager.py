import requests


class DataManager:
    # This class is responsible for talking to the Google Sheet.
    def __init__(self, endpoint):
        self.endpoint = endpoint
        pass

    def update_sheet(self, row_id, sheet_data):
        update_endpoint = f"{self.endpoint}/{row_id}"
        response = requests.put(url=update_endpoint, json=sheet_data)
        response.raise_for_status()
        return response
