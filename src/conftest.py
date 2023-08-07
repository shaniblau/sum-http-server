import pytest
import app
from set_logger import extendable_logger


@pytest.fixture
def app_fixture():
    return app


@pytest.fixture
def logger_fixture():
    return extendable_logger
