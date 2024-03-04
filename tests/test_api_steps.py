from pytest_bdd import given, when, then, scenario, parsers, scenarios

from apis.APIManager import APIManager
from apis.api_postman import get_method

scenarios('api.feature')

@given(parsers.parse('realizo la operacion "{method}" con el endpoint "{url}"'))
def perform_method(method, url):
     APIManager.set_last_response(get_method(method, url))


@then(parsers.parse('Obtengo el status code "{statusCode}"'))
def validar_status_code(statusCode):
    assert APIManager.get_last_response().status_code == int(statusCode)
