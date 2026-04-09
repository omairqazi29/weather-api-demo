#!/usr/bin/env python3
"""
MOOweather - CLI weather tool.
"""

import argparse
from .weather_client import get_weather
from .formatters import format_weather
from .cache import get_cached_weather, cache_weather


def main():
    parser = argparse.ArgumentParser(
        prog='MOOweather',
        description='Get the current weather for any city with MOOweather.'
    )
    parser.add_argument('city')
    parser.add_argument('--no-cache', action='store_true')
    args = parser.parse_args()

    if not args.no_cache:
        cached = get_cached_weather(args.city)
        if cached:
            print(format_weather(cached))
            return

    weather = get_weather(args.city)
    print(format_weather(weather))
    cache_weather(args.city, weather)


if __name__ == '__main__':
    main()