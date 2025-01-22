'''
Python module for calling the OpenWeatherMap Geocoding API to get geocode information for a city
'''

# Import requests library
import requests

def get_city_geocode(city, country):
    # Configuration For API
    API_KEY = "d7825274083d3769e5633279e0b7f1fc"
    BASE_URL = "http://api.openweathermap.org/geo/1.0/direct"
    CITY = city
    COUNTRY = country
    LIMIT = 1

    # Send the request
    responses = []
    for city in CITY:
        # Construct the request URL
        url = f"{BASE_URL}?q={city},{COUNTRY}&limit={LIMIT}&appid={API_KEY}"
        response = requests.get(url)
        if response.status_code == 200:
            responses.append(response.json())
        else:
            responses.append(None)
            print("Error")
    
    return responses