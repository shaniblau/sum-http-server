import pytest
from src import app


@pytest.fixture
def app_fixture():
    return app
