#!/usr/bin/env python3
"""MOOweather main entry point."""

import argparse
import sys

from mooweather.weather_client import get_weather
from mooweather.formatters import format_plain, format_json


def main():
    parser = argparse.ArgumentParser(
        prog='mooweather',
        description='MOOweather: Fetch current weather for any city.',
        epilog='Thanks for using MOOweather! Powered by OpenWeatherMap.'
    )
    parser.add_argument('city', help='The city name')
    parser.add_argument('--json', action='store_true', help='Output in JSON format')
    args = parser.parse_args()

    weather = get_weather(args.city)
    if args.json:
        print(format_json(weather))
    else:
        print(format_plain(weather))


if __name__ == '__main__':
    main()
