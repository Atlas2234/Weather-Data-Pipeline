# Import the get_city_weather function from the weather_api_calls module
from weather_api_calls import get_city_weather, organize_weather_data

from database import insert_to_database, fetch_top_temp, fetch_city_weather, fetch_max_temp, fetch_min_temp, fetch_humidity, fetch_top_wind_speeds

if __name__ == "__main__":
    cities = get_city_weather()
    dicts = organize_weather_data(cities)
    #print(dicts)

    #insert_to_database(dicts)
    top_temp_data = fetch_top_temp()
    weather_data = fetch_city_weather()
    max_temp_data = fetch_max_temp()
    min_temp_data = fetch_min_temp()
    humidity_data = fetch_humidity()
    wind_speed_data = fetch_top_wind_speeds()
