from pathlib import Path

import requests
from pytest_bdd import given, when, then, scenario, parsers

from apis.APIManager import APIManager
from apis.api_postman import get_method


@scenario('api.feature', 'Retrieve data from API')
def test_navigate_to_domains_page():
    pass


@given(parsers.parse('realizo la operacion "{method}" con el endpoint "{url}"'))
def perform_method(method, url):
     APIManager.set_last_response(get_method(method, url))
     print(method, url)


@then(parsers.parse('Obtengo el status code "{statusCode}"'))
def validar_status_code(statusCode):
    assert APIManager.get_last_response().status_code == int(statusCode)
    print(APIManager.get_last_response().headers)
