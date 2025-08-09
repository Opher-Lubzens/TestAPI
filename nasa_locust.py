import datetime

import pytest
from locust import HttpUser, task, between

from nasa_config import API_KEY_NASA


class NASAAPODUser(HttpUser):
    wait_time = between(60, 120)

    @task
    @pytest.mark.parametrize('date', [(datetime.date.today())])
    def nasa_get_todays_apod(self,date):
        self.client.get(f"/planetary/apod?api_key={API_KEY_NASA}&date={date}")


