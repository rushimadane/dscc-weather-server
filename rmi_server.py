import requests

def get_weather(city):
    # Use Open-Meteo Geocoding API to get coordinates
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo_data = requests.get(geo_url).json()

    if not geo_data.get("results"):
        return f"City '{city}' not found."

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    # Fetch current weather data
    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_data = requests.get(weather_url).json()

    current = weather_data.get("current_weather", {})
    temp = current.get("temperature")
    wind = current.get("windspeed")
    weather = current.get("weathercode", "")

    result = f"🌍 City: {city}\n🌡 Temperature: {temp}°C\n💨 Wind Speed: {wind} km/h"
    return result

