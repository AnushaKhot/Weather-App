import requests
from config import API_KEY

FORECAST_URL = "https://api.openweathermap.org/data/2.5/forecast"


def get_forecast(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(FORECAST_URL, params=params)

    if response.status_code != 200:
        return None

    return response.json()