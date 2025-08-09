import datetime

import pytest
from locust import HttpUser, task, between

from nasa_config import API_KEY_NASA


class NASAAPODUser(HttpUser):
    wait_time = between(60, 120)

    @task
    def nasa_get_todays_apod(self):
        self.client.get(f"/planetary/apod?api_key={API_KEY_NASA}&date={datetime.date.today()}")


