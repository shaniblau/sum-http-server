import pytest
import app
import sign_file
from set_logger import extendable_logger


@pytest.fixture
def app_fixture():
    return app


@pytest.fixture
def logger_fixture():
    return extendable_logger


@pytest.fixture
def sign_fixture():
    return sign_file


@pytest.fixture
def mock_sign_fixture(mocker):
    return mocker.patch('app.sign')


@pytest.fixture
def mock_create_encrypted_hash_fixture(mocker):
    return mocker.patch('sign_file.__create_encrypted_hash')
