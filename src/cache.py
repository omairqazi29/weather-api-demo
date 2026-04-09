"""Cache module for MooWeather."""

import json
from pathlib import Path
import time

class WeatherCache:
    def __init__(self):
        self.cache_file = Path.home() / '.mooweather_cache.json'

    def get(self, city):
        # placeholder
        return None

    def set(self, city, data):
        # placeholder
        pass
