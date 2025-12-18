import requests

API_KEY = "e0d1a458ae1c542756c32dd5f996e723"
city = "Cleveland"

url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}"

response = requests.get(url)
data = response.json()

print(data)
