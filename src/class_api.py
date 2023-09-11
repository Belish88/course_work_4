import os
from abc import ABC, abstractmethod

import requests

from src.setting import SJ_URL, HH_URL


class ApiAbc(ABC):
    @abstractmethod
    def get_request(self):
        pass


class HH(ApiAbc):
    def __init__(self, keyword):
        self.url = HH_URL
        self.params = {
            'text': keyword,
            'page': 0,
            'per_page': 100,
            'search_field': 'name'
        }

    def get_request(self):
        return requests.get(self.url, params=self.params)


class SJ(ApiAbc):
    def __init__(self, keyword):
        self.url = SJ_URL
        self.params ={
            'keyword': keyword,
            'page': 0,
            'count': 100,
        }

    def get_request(self):
        headers = {'X-Api-App-Id': os.environ['SJ_API_KEY']}
        return requests.get(self.url, headers=headers, params=self.params)

