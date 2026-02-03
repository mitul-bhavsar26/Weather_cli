import requests
import sys

# Define constants
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"



def get_weather_data(city, api_key):
    """
    Fetch weather data from OpenWeatherMap API.
    Returns a dictionary on success, None on failure.
    """
    request_url = f"{BASE_URL}?q={city}&appid={api_key}"

    try:
        response = requests.get(request_url)
        response.raise_for_status()

        data = response.json()

        # Create a CLEAN dictionary 
        weather_info = {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "description": data["weather"][0]["description"],
        }

        return weather_info

    except requests.exceptions.HTTPError as http_err:
        if http_err.response.status_code == 401:
            print("Error: Invalid API Key.")
        elif http_err.response.status_code == 404:
            print("Error: City not found.")
        else:
            print(f"HTTP error occurred: {http_err}")
        return None

    except requests.exceptions.RequestException as e:
        print("Network error: Could not connect to the weather service.")
        print(f"Details: {e}")
        return None


def display_weather_data(data):
    """
    Display weather data nicely.
    """
    print()
    print(f"Weather in {data['city']}:")
    print("-" * 20)
    print(f"Temperature: {data['temperature']} K")
    print(f"Humidity: {data['humidity']} %")
    print(f"Description: {data['description'].capitalize()}")
    print()
    
def main():
    
    #The main function to run the weather CLI tool.
    
    API_KEY = "e0d1a458ae1c542756c32dd5f996e723"  # API key
    CITY = "Cleveland"      
    # 1. Get the data
    weather_data = get_weather_data(CITY, API_KEY)
     
     # 2. If data was retrieved successfully, display it
    if weather_data:
        display_weather_data(weather_data)
    else:
        print("Unable to retrieve weather data.")
