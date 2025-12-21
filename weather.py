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
    
    print("Success! The request was fulfilled.")
else:
   
    print(f"Error: The request failed with status code {response.status_code}")
# Convert the response to JSON
data = response.json()

# Print the result
print(data)
