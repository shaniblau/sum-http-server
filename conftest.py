import pytest
import app
import sign_file


@pytest.fixture
def app_fixture():
    return app


@pytest.fixture
def sign_fixture():
    return sign_file
