import requests

api_key = input("Enter your OpenWeather API key: ")
city = input("Enter city name: ")

url = "https://api.openweathermap.org/data/2.5/weather"

params = {
    "q": city,
    "appid": api_key,
    "units": "metric"
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    print("\nWeather Information")
    print("City:", data["name"])
    print("Temperature:", data["main"]["temp"], "°C")
    print("Feels like:", data["main"]["feels_like"], "°C")
    print("Humidity:", data["main"]["humidity"], "%")
    print("Weather:", data["weather"][0]["description"])

else:
    print("Could not fetch weather data.")
    print("Status code:", response.status_code)