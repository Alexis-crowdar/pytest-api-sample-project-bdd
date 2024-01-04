import requests


def get_method():
    baseUrl = "https://postman-echo.com/"
    endpoint = "get"
    url = baseUrl + endpoint
    headers = {
        "x-forwarded-proto": "https",
        "x-forwarded-port": "443",
        "host": "postman-echo.com",
        "x-amzn-trace-id": "Root=1-659569eb-0e21da882a1b7dd62c1cd1d4",
        "user-agent": "PostmanRuntime/7.36.0",
        "accept": "*/*",
        "cache-control": "no-cache",
        "postman-token": "dfe5e645-5fca-409f-b162-7b74ff332f00"
    }
    response = requests.get(url, headers=headers)

    return response
