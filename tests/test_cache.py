import pytest
from mooweather.cache import WeatherCache


def test_cache_init():
    cache = WeatherCache()
    assert cache.cache_file.exists() == False  # placeholder


def test_cache_get_set():
    cache = WeatherCache()
    cache.set('London', {'temp': 20})
    data = cache.get('London')
    assert data is not None  # placeholder
