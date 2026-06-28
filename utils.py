from datetime import datetime


def weather_icon(weather):

    icons = {
        "Clear": "☀️",
        "Clouds": "☁️",
        "Rain": "🌧️",
        "Snow": "❄️",
        "Thunderstorm": "⛈️",
        "Drizzle": "🌦️",
        "Mist": "🌫️",
        "Fog": "🌫️",
        "Haze": "🌫️"
    }

    return icons.get(weather, "🌍")


def format_time(timestamp):

    return datetime.fromtimestamp(timestamp).strftime("%I:%M %p")