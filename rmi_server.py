from xmlrpc.server import SimpleXMLRPCServer
import os
import random
import requests

def get_weather(city):
    geo_url = f"https://geocoding-api.open-meteo.com/v1/search?name={city}"
    geo_data = requests.get(geo_url).json()

    if not geo_data.get("results"):
        return f"City '{city}' not found."

    lat = geo_data["results"][0]["latitude"]
    lon = geo_data["results"][0]["longitude"]

    weather_url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current_weather=true"
    weather_data = requests.get(weather_url).json()

    current = weather_data.get("current_weather", {})
    temp = current.get("temperature")
    wind = current.get("windspeed")
    result = f"🌍 City: {city}\n🌡 Temperature: {temp}°C\n💨 Wind Speed: {wind} km/h"
    return result

def main():
    port = int(os.environ.get("PORT", 8000))  # Use Render-assigned port
    server = SimpleXMLRPCServer(("0.0.0.0", port), allow_none=True)
    print(f"✅ XML-RPC Weather Server running on port {port}...")
    server.register_function(get_weather, "get_weather")
    server.serve_forever()

if __name__ == "__main__":
    main()
