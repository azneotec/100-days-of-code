import requests

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/onecall"
api_key = "fake_api_key"

weather_params = {
    "lat": 51.507351,
    "lon": -0.127758,
    "appid": api_key,
}

response = requests.get(OWM_Endpoint, params=weather_params)
print(response.status_code)
print(response.json())
