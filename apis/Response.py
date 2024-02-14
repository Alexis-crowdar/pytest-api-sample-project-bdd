import pytest


class Headers:
    def __init__(self, headers):
        self.headers = headers

    def get_headers(self):
        return self.headers


class Response:
    def __init__(self, status_code, message, response, headers):
        self.status_code = status_code
        self.message = message
        self.response = response
        self.headers = headers

    def get_status_code(self):
        return self.status_code

    def get_message(self):
        return self.message

    def get_response(self):
        return self.response

    def get_headers(self):
        return self.headers.get_headers()
