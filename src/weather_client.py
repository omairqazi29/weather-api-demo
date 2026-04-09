"""Weather API client for MooWeather."""

import requests

API_KEY = 'demo'


def get_weather(city, api_key=API_KEY):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    resp = requests.get(url)
    return resp.json()
