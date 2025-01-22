'''
Python module for calling the OpenWeatherMap API
'''

# Import requests library
import requests

# Import get_city_geocode function in the geocoding_calls module to get the geocode information for a location
from geocoding_calls import get_city_geocode

# Configuration For API
API_KEY = "d7825274083d3769e5633279e0b7f1fc"
BASEURL = "https://api.openweathermap.org/data/2.5/weather"
UNIT = "metric"

# Get geocode information for a city
CITY = ["Vancouver", "Toronto", "Montreal"]
COUNTRY = "CA"

city_response = get_city_geocode(CITY, COUNTRY)

def get_city_weather():
    # Send the request
    CNT = 7
    city_weathers = []
    for city in city_response:
        if city != None:
            # Construct the URL
            url = f"{BASEURL}?lat={city[0]["lat"]}&lon={city[0]["lon"]}&cnt={CNT}&units={UNIT}&appid={API_KEY}"
            response = requests.get(url)
            if response.status_code == 200:
                city_weathers.append(response.json())
            else:
                city_weathers.append(None)
                print("Error")
    
    return city_weathers

def organize_weather_data(response):
    dictList = []
    for city in response:
        if city != None:
            cityDict = {"cityId": city["id"], 
                        "name": city["name"], 
                        "weather": city["weather"][0]["main"], 
                        "temperature": city["main"]["temp"], 
                        "feels": city["main"]["feels_like"], 
                        "max_temp": city["main"]["temp_max"], 
                        "min_temp": city["main"]["temp_min"],
                        "humidity": city["main"]["humidity"],
                        "wind_speed": city["wind"]["speed"],}
            dictList.append(cityDict)

    return dictList

def testingModule():
    for response in city_response:
        if response != None:
            print(response.json())
        else:
            print("Error")
