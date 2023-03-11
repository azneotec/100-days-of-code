import requests

APP_ID = "FAKE_APP_ID"
API_KEY = "FAKE_API_KEY"

user_entry = input("Tell me which exercises you did: ")

# Run 2 miles and walked for 3Km.
# user_entry = "Run 2 miles and walked for 3Km."

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Content-Type": "application/json",
}

body = {
    "query": user_entry,
}

response = requests.post(url="https://trackapi.nutritionix.com/v2/natural/exercise", json=body, headers=headers)
response.raise_for_status()
print(response.json())
