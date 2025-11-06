from xmlrpc.server import SimpleXMLRPCServer
import random

def get_weather(city):
    temp = round(random.uniform(20, 40), 1)
    humidity = random.randint(40, 90)
    condition = random.choice(["Sunny", "Cloudy", "Rainy", "Windy", "Foggy"])
    result = f"City: {city}\nTemperature: {temp}°C\nHumidity: {humidity}%\nCondition: {condition}"
    return result

def main():
    server = SimpleXMLRPCServer(("0.0.0.0", 8000), allow_none=True)
    print("✅ XML-RPC Weather Server is running on port 8000...")
    server.register_function(get_weather, "get_weather")
    server.serve_forever()

if __name__ == "__main__":
    main()
