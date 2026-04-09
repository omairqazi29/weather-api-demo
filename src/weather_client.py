import requests
from requests.exceptions import RequestException
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type

class WeatherClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"

    @retry(wait=wait_exponential(multiplier=1, min=4, max=60), stop=stop_after_attempt(5), retry=retry_if_exception_type(RequestException), reraise=True)  # Exponential backoff: 5 attempts, 4-60s wait on RequestException
    def fetch_weather(self, lat: float, lon: float) -> dict:
        url = f"{self.base_url}/weather"
        params = {
            "lat": lat,
            "lon": lon,
            "appid": self.api_key,
            "units": "metric"
        }
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
