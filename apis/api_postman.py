import json

import pytest
import requests

def get_method(operacion, url):
    if operacion == "GET":
        response = requests.get(url)
    elif operacion == "POST":
        response = requests.post(url, data={"data": "value"})
    else:
        raise ValueError("Operación no válida")
    return response