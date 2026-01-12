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
    # The http_err object contains the response, which we can inspect.
    # We check if the status code of the response is 401 (Unauthorized).
    if http_err.response.status_code == 401:
        # If it is, we print a very specific and helpful error message.
        print("Error: Invalid API Key. Please check your API_KEY variable.")
    
    # THEN, check for a 404 (Not Found) error.
    elif http_err.response.status_code == 404:
        print("Error: City not found. Please check the spelling of the city name.")
        
    else:
        # For any other HTTP error, we can fall back to the generic message.
        print(f"An HTTP error occurred: {http_err}")
    
    # We still exit gracefully after printing the error.
    sys.exit(1)
    
except requests.exceptions.RequestException as e:
    # This block will catch any network-related errors (e.g., no internet, DNS failure).
    print("Network error: Could not connect to the weather service.")
    print(f"Details: {e}")
    sys.exit(1)

















