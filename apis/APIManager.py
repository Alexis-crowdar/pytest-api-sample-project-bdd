import os
from threading import local

class APIManager:
    BASE_URL = os.environ.get('base_api_url')
    LAST_RESPONSE = local()

    @classmethod
    def set_last_response(cls, last_response):
        cls.LAST_RESPONSE.last_response = last_response

    @classmethod
    def get_last_response(cls):
        return cls.LAST_RESPONSE.last_response