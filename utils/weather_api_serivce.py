import requests
from config.config import METEO_KEY
import pprint

#TODO move to confing
API_key = METEO_KEY
weather_units = 'metric'

def get_current_weather_by_city(city_name):

    current_weather = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_key}&units={weather_units}")

    print(current_weather.json()['weather'])
    print('\n')
    print(current_weather.json()['main'])
    print('\n')
    pprint.pprint(current_weather.json())

    return current_weather.json()


if __name__ == '__main__':
    get_current_weather_by_city('warsaw')