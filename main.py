# Import the get_city_weather function from the weather_api_calls module
from weather_api_calls import get_city_weather, organize_weather_data

from database import connect_to_database

if __name__ == "__main__":
    cities = get_city_weather()
    dicts = organize_weather_data(cities)
    print(dicts)

    connect_to_database()
