import argparse
import sys
import requests


# Define constants
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"



def get_weather_data(city, api_key, units="metric"):
    """
    Fetch weather data from OpenWeatherMap API.
    Returns a dictionary on success, None on failure.
    """
    request_url = f"{BASE_URL}?q={city}&appid={api_key}&units={units}"


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


def display_weather_data(data, units):
    """
    Display weather data nicely.
    """
    unit_symbol = "°C" if units == "metric" else "°F"
    
    print()
    print(f"Weather in {data['city']}:")
    print("-" * 20)
    print(f"Temperature: {data['temperature']}{unit_symbol}")
    print(f"Humidity: {data['humidity']} %")
    print(f"Description: {data['description'].capitalize()}")
    print()
    
def main():
    
    #The main function to run the weather CLI tool.
    
    #create the argument parser
    parser = argparse.ArgumentParser(description="Get the current weather for a specific city.")
    parser.add_argument("city", help="The name of the city to get the weather for.")
    
    # Add an optional argument for the units.
    # 'choices' restricts the input to the given values.
    # 'default' sets a fallback value if the argument is not provided.

    parser.add_argument(
        "--units",
        choices=["metric", "imperial"],
        default="metric",
        help="The units for temperature (metric=Celsius, imperial=Fahrenheit). Default: metric",
    )
    
    # This line reads the command-line input and returns the parsed arguments.
    args = parser.parse_args()
    
    
    API_KEY = "e0d1a458ae1c542756c32dd5f996e723"  # API key
        
    # 1. Get the data
    weather_data = get_weather_data(args.city, API_KEY, args.units)
     
     # 2. If data was retrieved successfully, display it
    if weather_data:
        display_weather_data(weather_data, args.units)
    else:
        print("Unable to retrieve weather data.")
# Entry point
if __name__ == "__main__":
    main()