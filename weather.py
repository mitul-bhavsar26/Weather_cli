import requests
import sys



# Define the core components of our API request as constants
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "e0d1a458ae1c542756c32dd5f996e723"  # replace with your real key
CITY = "Cleveland"


# Construct the full API request URL using an f-string
request_url = f"{BASE_URL}?q={CITY}&appid={API_KEY}"
try:
    # Make the API call
    response = requests.get(request_url)

    # This line automatically checks if the request failed
    response.raise_for_status()

    # If we reach here, the request was successful
    data = response.json()

    # Extract the relevant data
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather_description = data['weather'][0]['description']

    # Display the weather information
    print()
    print(f"Weather in {CITY}:")
    print("-" * 20)
    print(f"Temperature: {temperature} K")
    print(f"Humidity: {humidity} %")
    print(f"Description: {weather_description.capitalize()}")
    print()

except requests.exceptions.HTTPError as http_err:
    # This block will be executed for any 4xx or 5xx HTTP status codes.
    print(f"An HTTP error occurred: {http_err}")
    sys.exit(1)

except requests.exceptions.RequestException as e:
    # This block will catch any network-related errors (e.g., no internet, DNS failure).
    print("Network error: Could not connect to the weather service.")
    print(f"Details: {e}")
    sys.exit(1)

















