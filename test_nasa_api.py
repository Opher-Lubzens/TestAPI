import datetime
import random
import time

import pytest, requests
from jsonschema import validate

API_KEY_NASA = '13HsxoQe9A9ofBg6NGMEhc9xUYKG8HrtSe6EV5xN'

class TestNASAAPODAPI:
    @pytest.mark.parametrize('date', [(time.strftime('%Y-%m-%d'))])
    def test_nasa_apod_api_today_status(self, date):
        response = requests.get(f'https://api.nasa.gov/planetary/apod?'
                                f'api_key={API_KEY_NASA}&date={date}')
        response.raise_for_status()

    @pytest.mark.parametrize('count', [(random.randint(1, 100))])
    def test_nasa_apod_api_random_pics(self, count):
        response = requests.get(f'https://api.nasa.gov/planetary/apod?'
                                f'api_key={API_KEY_NASA}&count={count}')
        response.raise_for_status()

    @pytest.mark.parametrize('days_before_now', [(random.randint(1, 10))])
    def test_nasa_apod_api_days_range_now(self, days_before_now):
        now = datetime.date.today()
        start_date = now - datetime.timedelta(days=days_before_now)
        response = requests.get(f'https://api.nasa.gov/planetary/apod?'
                                f'api_key={API_KEY_NASA}&start_date={start_date}&end_date={now}')
        response.raise_for_status()