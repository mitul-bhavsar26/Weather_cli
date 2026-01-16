import requests
import sys



# Define the core components of our API request as constants
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "e0d1a458ae1c542756c32dd5f996e723"  # replace with your real key
CITY = "Cleveland"

def get_weather_data(city, api_key):
    request_url = f"{BASE_URL}?q={city}&appid={api_key}"

    try:
        response = requests.get(request_url)
        response.raise_for_status()
        return response.json()

    except requests.exceptions.HTTPError as http_err:
        if http_err.response.status_code == 401:
            print("Error: Invalid API Key. Please check your API_KEY variable.")
        elif http_err.response.status_code == 404:
            print("Error: City not found. Please check the spelling of the city name.")
        else:
            print(f"An HTTP error occurred: {http_err}")
        return None

    except requests.exceptions.RequestException as e:
        print("Network error: Could not connect to the weather service.")
        print(f"Details: {e}")
        return None

data = get_weather_data(CITY, API_KEY)

if data:
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_description = data['weather'][0]['description']

    print()
    print(f"Weather in {CITY}:")
    print("-" * 20)
    print(f"Temperature: {temperature} K")
    print(f"Humidity: {humidity} %")
    print(f"Description: {weather_description.capitalize()}")
    print()
else:
    print("Unable to retrieve weather data.")

    
    
