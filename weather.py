import requests
from config import API_KEY

CURRENT_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_current_weather(city):

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(CURRENT_URL, params=params)

    if response.status_code != 200:
        return None

    return response.json()