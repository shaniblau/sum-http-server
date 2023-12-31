import os

import pytest
from fastapi.testclient import TestClient

from help_funcs import File, create_files, prepare_create_single_file, cleanup


def test_create_upload_file_should_respond_with_200(app_fixture, logger_fixture, mocker):
    mocker.patch('app.config.LOGS_DIR', './logs')
    client = TestClient(app_fixture.app)
    files = create_files()
    response = client.post("/uploadfile", files=files)
    cleanup()
    assert response.status_code == 200


def test_create_upload_file_should_respond_not_200(app_fixture, logger_fixture, mocker):
    mocker.patch('app.config.LOGS_DIR', './logs')
    client = TestClient(app_fixture.app)
    files = create_files()
    response = client.post("/", files=files)
    cleanup()
    assert response != 200


def test_sort_files_should_replace_file_a_and_file_b_locations_in_the_list(app_fixture):
    file_a = File(filename='file_a.jpg')
    file_b = File(filename="file_b.jpg")
    files = [file_b, file_a]
    expected = [file_a, file_b]
    result = app_fixture.sort_files(files)
    assert result == expected


@pytest.mark.asyncio
async def test_create_single_file_should_create_a_whole_file(app_fixture, mocker, mock_sign_fixture):
    await prepare_create_single_file(mocker, app_fixture)
    create_files()
    expected = b'ab'
    with open(os.path.join('./', 'file.jpg'), 'rb') as file:
        result = file.read()
    cleanup()
    assert result == expected


@pytest.mark.asyncio
async def test_create_single_file_should_call_sign_file_once(app_fixture, mock_sign_fixture, mocker):
    await prepare_create_single_file(mocker, app_fixture)
    mock_sign_fixture.assert_called_once()
