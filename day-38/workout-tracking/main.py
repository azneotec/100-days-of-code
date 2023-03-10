import os

import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime

GENDER = "male"
WEIGHT_KG = 92.25
HEIGHT_CM = 172.0
AGE = 33

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
BASIC_AUTH_TOKEN = os.environ["BASIC_AUTH_TOKEN"]
BEARER_AUTH_TOKEN = os.environ["BEARER_AUTH_TOKEN"]

basic = HTTPBasicAuth(USERNAME, PASSWORD)
withBasicAuthHeader = {
    "Authorization": f"Basic {BASIC_AUTH_TOKEN}"
}
withBearerAuthHeader = {
    "Authorization": f"Bearer {BEARER_AUTH_TOKEN}"
}

EXERCISE_API_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"

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
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=EXERCISE_API_ENDPOINT, json=body, headers=headers)
response.raise_for_status()
exercise_data = response.json()

exercises = exercise_data["exercises"]

# https://api.sheety.co/4a5e188bb442bb3c7d9bccdd75e9d8b1/workoutTracking/workouts

WORKOUT_SHEETY_API_ENDPOINT = "https://api.sheety.co/4a5e188bb442bb3c7d9bccdd75e9d8b1/workoutTracking/workouts"

today = datetime.now()
today_date = today.strftime("%d/%m/%Y")
now_time = today.strftime("%X")

for exercise in exercises:
    workout_data = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"],
        }
    }
    # workout_response = requests.post(url=WORKOUT_SHEETY_API_ENDPOINT, json=workout_data, auth=basic)
    # workout_response = requests.post(url=WORKOUT_SHEETY_API_ENDPOINT, json=workout_data, headers=withBasicAuthHeader)
    workout_response = requests.post(url=WORKOUT_SHEETY_API_ENDPOINT, json=workout_data, headers=withBearerAuthHeader)
    workout_response.raise_for_status()
    # print(workout_response.json())
