import pytest
from adapterPytest.src.main.pytest.ltm.TestManagerAPIAdapter import TestManagerAPIAdapter

def pytest_bdd_after_scenario(request, feature, scenario):
    adapter_instance = TestManagerAPIAdapter()
    adapter_instance.pytest_bdd_after_scenario(request, feature, scenario)