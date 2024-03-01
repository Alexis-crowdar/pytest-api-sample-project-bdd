import pytest
from adapterPytest.src.main.pytest.ltm.TestManagerAPIAdapter import TestManagerAPIAdapter, TestManagerAPIClient

import config

TestManagerAPIClient.initialize_rest_template(RUN_NAME=config.RUN_NAME, PROJECT_CODE=config.PROJECT_CODE)
adapter_instance = TestManagerAPIAdapter()


def pytest_bdd_after_scenario(feature, scenario):
    adapter_instance.pytest_bdd_after_scenario(feature, scenario)

def pytest_bdd_after_step(step,step_func_args):
    adapter_instance.pytest_bdd_after_step(step,step_func_args)

def pytest_bdd_step_error(step, exception):
    adapter_instance.pytest_bdd_step_error(step, exception)
