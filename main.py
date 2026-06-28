from weather import get_current_weather
from forecast import get_forecast
from utils import weather_icon, format_time

city = input("Enter City Name: ")

weather = get_current_weather(city)

if weather is None:
    print("❌ City not found!")
    exit()

icon = weather_icon(weather["weather"][0]["main"])

print("\n======================================")
print("          🌤 WEATHER REPORT")
print("======================================")

print(f"\n📍 City        : {weather['name']}, {weather['sys']['country']}")
print(f"{icon} Weather     : {weather['weather'][0]['description'].title()}")

print(f"\n🌡 Temperature : {weather['main']['temp']} °C")
print(f"🤗 Feels Like  : {weather['main']['feels_like']} °C")
print(f"💧 Humidity    : {weather['main']['humidity']}%")
print(f"💨 Wind Speed  : {weather['wind']['speed']} m/s")
print(f"☁️ Clouds      : {weather['clouds']['all']}%")
print(f"👁 Visibility  : {weather['visibility']/1000} km")
print(f"🌍 Pressure    : {weather['main']['pressure']} hPa")
print(f"🌅 Sunrise     : {format_time(weather['sys']['sunrise'])}")
print(f"🌇 Sunset      : {format_time(weather['sys']['sunset'])}")

print("\n======================================")

forecast = get_forecast(city)

if forecast:

    print("\n📅 5-Day Forecast")
    print("--------------------------------------")

    shown = 0

    for item in forecast["list"]:

        if "12:00:00" in item["dt_txt"]:

            date = item["dt_txt"].split()[0]

            temp = item["main"]["temp"]

            desc = item["weather"][0]["main"]

            icon = weather_icon(desc)

            print(f"{date}   {icon}   {temp}°C   {desc}")

            shown += 1

            if shown == 5:
                break