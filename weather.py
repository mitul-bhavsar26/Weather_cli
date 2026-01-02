import requests



# Define the core components of our API request as constants
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "e0d1a458ae1c542756c32dd5f996e723"  # replace with your real key
CITY = "New York"


# Construct the full API request URL using an f-string
request_url = f"{BASE_URL}?q={CITY}&appid={API_KEY}"

# Make the API call
response = requests.get(request_url)

# Check the status code of the response.
# A status code of 200 means the request was successful.
if response.status_code == 200:
    data = response.json()

    # Store extracted values in variables
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
    print(f"Error: The request failed with status code {response.status_code}")



