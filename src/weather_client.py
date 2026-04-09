import requests
from requests.exceptions import ConnectionError, Timeout, ConnectTimeout, ReadTimeout
from tenacity import retry, wait_exponential, stop_after_attempt, retry_if_exception_type

class WeatherClient:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.openweathermap.org/data/2.5"

    @retry(wait=wait_exponential(multiplier=1, min=1, max=60), stop=stop_after_attempt(5), retry=retry_if_exception_type((ConnectionError, Timeout, ConnectTimeout, ReadTimeout)), reraise=True)  # Exponential backoff: retries up to 5 times on transient network errors with backoff starting at 1s, doubling each time up to 60s max wait.
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
