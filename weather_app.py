import requests
from datetime import datetime
from config import API_KEY, BASE_URL


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "condition": data["weather"][0]["description"],
            "humidity": data["main"]["humidity"]
        }
    else:
        return None


def main():
    city = input("Enter city name: ")

    weather = get_weather(city)

    if weather:
        current_time = datetime.now().strftime("%d %b %Y, %I:%M %p")

        print("\n🌍 Weather Report")
        print("-" * 25)
        print(f"📍 City       : {weather['city']}")
        print(f"📅 Date & Time: {current_time}")
        print(f"🌡 Temperature: {weather['temperature']}°C")
        print(f"☁ Condition  : {weather['condition'].title()}")
        print(f"💧 Humidity   : {weather['humidity']}%")

    else:
        print("❌ City not found or API error.")


if __name__ == "__main__":
    main()
