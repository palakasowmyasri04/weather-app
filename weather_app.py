import requests
from datetime import datetime
from config import API_KEY, BASE_URL

def main():
    city = input("Enter city name: ")

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        now = datetime.now().strftime("%d %b %Y %H:%M")

        print("\nCity:", data["name"])
        print("Date & Time:", now)
        print("Temperature:", data["main"]["temp"], "°C")
        print("Condition:", data["weather"][0]["description"])
        print("Humidity:", data["main"]["humidity"], "%")
    else:
        print("City not found or API error.")

if __name__ == "__main__":
    main()
