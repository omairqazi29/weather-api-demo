import json
import pytest
from mooweather.formatters import format_plain, format_json

SAMPLE_WEATHER = {
    'name': 'London',
    'main': {'temp': 15.0},
    'weather': [{'description': 'cloudy'}]
}


def test_format_plain():
    result = format_plain(SAMPLE_WEATHER)
    assert 'London' in result
    assert '15.0' in result


def test_format_json():
    result = format_json(SAMPLE_WEATHER)
    assert isinstance(json.loads(result), dict)
