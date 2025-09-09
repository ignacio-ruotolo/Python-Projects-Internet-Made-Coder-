# Build a weather app that fetches data from an API to display the current weather.

import requests

# city = input("Enter a city: ")
# ?format=3 gives a simple text response
# url = f"https://wttr.in/{city}?format=3"

# response = requests.get(url)

# if response.status_code == 200:
#    print(response.text)
# else:
#    print("Failed to get weather data")

city = input("Enter a city: ")
url = f"https://wttr.in/{city}?format=j1"  # j1 = JSON output

response = requests.get(url)

if response.status_code == 200:
    data = response.json()  # Parse JSON response

    # Accessing weather info
    current_condition = data["current_condition"][0]
    temp_c = current_condition["temp_C"]
    weather_desc = current_condition["weatherDesc"][0]["value"]

    print(f"The weather in {city} is {weather_desc} and {temp_c}°C.")
else:
    print("Failed to get weather data")
