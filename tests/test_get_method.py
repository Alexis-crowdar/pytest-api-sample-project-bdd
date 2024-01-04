import pytest
from jsonschema import validate
from commons.jsonOpen import open_schema
from apis.api_postman import get_method


class TestGetTokenEndpoint:

    @pytest.fixture
    def reponse_get_method(self):
        return get_method()

    @pytest.mark.test
    def test_get_method(self, reponse_get_method):
        response = reponse_get_method
        print(response)
        assert response.status_code == 200
        expected_url = 'https://postman-echo.com/get'
        assert response.json()['url'] == expected_url

