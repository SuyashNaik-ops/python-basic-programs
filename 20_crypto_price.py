import requests

coin = input("Enter cryptocurrency (example: bitcoin): ")
currency = input("Enter currency (example: usd): ")

url = "https://api.coingecko.com/api/v3/simple/price"

params = {
    "ids": coin,
    "vs_currencies": currency
}

response = requests.get(url, params=params)

if response.status_code == 200:
    data = response.json()

    if coin in data:
        price = data[coin][currency]
        print(f"{coin} price: {price} {currency.upper()}")
    else:
        print("Cryptocurrency not found.")

else:
    print("Could not fetch cryptocurrency price.")
    print("Status code:", response.status_code)