"""Output formatters for MooWeather."""

import json


def format_plain(weather):
    return f"{weather['name']}: {weather['main']['temp']}°C, {weather['weather'][0]['description']}"


def format_json(weather):
    return json.dumps(weather, indent=2)
