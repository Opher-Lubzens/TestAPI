import datetime
import random
import time
from typing import Any

import pytest, requests
from jsonschema import validate

from nasa_config import API_KEY_NASA
from nasa_schemas import APOD_SINGLE_SCHEMA, APOD_MULTI_SCHEMA



def request_apod_and_test_status(query_params: dict[str, Any]):
    query_string = ''
    for key, value in query_params.items():
        query_string += f'&{key}={value}'
    response = requests.get(f'https://api.nasa.gov/planetary/apod?'
                            f'api_key={API_KEY_NASA}{query_string}')
    response.raise_for_status()

def request_apod_and_validate_schema(query_params: dict[str, Any], schema: dict, length = 0):
    query_string = ''
    for key, value in query_params.items():
        query_string += f'&{key}={value}'
    response = requests.get(f'https://api.nasa.gov/planetary/apod?'
                            f'api_key={API_KEY_NASA}{query_string}')
    if length != 0:
        assert len(response.json()) == length
    validate(instance=response.json(), schema=schema)

class TestNASAAPODAPI:
    @pytest.mark.parametrize('date', [(time.strftime('%Y-%m-%d'))])
    def test_nasa_apod_api_today_status(self, date):
        request_apod_and_test_status({'date': date})

    @pytest.mark.parametrize('count', [(random.randint(1, 100))])
    def test_nasa_apod_api_random_pics(self, count):
        request_apod_and_test_status({'count': count})

    @pytest.mark.parametrize('days_before_now', [(random.randint(1, 10))])
    def test_nasa_apod_api_days_range_now(self, days_before_now):
        now = datetime.date.today()
        start_date = now - datetime.timedelta(days=days_before_now)
        request_apod_and_test_status({'start_date': start_date, 'end_date': now})

    @pytest.mark.parametrize('date', [(time.strftime('%Y-%m-%d'))])
    def test_nasa_apod_api_today_schema(self, date):
        request_apod_and_validate_schema({'date': date}, APOD_SINGLE_SCHEMA)

    @pytest.mark.parametrize('count', [(random.randint(1, 100))])
    def test_nasa_apod_api_random_pics_schema(self, count):
        request_apod_and_validate_schema({'count': count}, APOD_MULTI_SCHEMA,
                                         length=count)

    @pytest.mark.parametrize('days_before_now', [(random.randint(1, 10))])
    def test_nasa_apod_api_days_range_now_schema(self, days_before_now):
        now = datetime.date.today()
        start_date = now - datetime.timedelta(days=days_before_now)
        request_apod_and_validate_schema({'start_date': start_date, 'end_date': now},
                                         schema=APOD_MULTI_SCHEMA, length=days_before_now + 1)