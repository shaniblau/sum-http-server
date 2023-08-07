import os
import pytest
from fastapi import UploadFile
from fastapi.testclient import TestClient

from help_funcs import File, create_files, prepare_create_single_file, prepare_create_upload_file


def test_create_upload_file_should_respond_with_200(app_fixture, logger_fixture, mocker):
    prepare_create_upload_file(mocker, logger_fixture)
    client = TestClient(app_fixture.app)
    files = create_files()
    response = client.post("/uploadfile", files=files)
    print(response)
    assert response.status_code == 200


def test_create_upload_file_should_respond_not_200(app_fixture, logger_fixture, mocker):
    prepare_create_upload_file(mocker, logger_fixture)
    client = TestClient(app_fixture.app)
    files = create_files()
    response = client.post("/", files=files)
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
    create_files()
    images_dir = './'
    files = [
        UploadFile(filename='file_a.jpg', file=open('./file_a', "rb")),
        UploadFile(filename='file_b.jpg', file=open('./file_b', "rb")),
    ]
    mocker.patch('app.config.IMAGES_DIR', images_dir)

    await app_fixture.create_single_file(files)
    expected = b'ab'
    with open(os.path.join(images_dir, 'file.jpg'), 'rb') as file:
        result = file.read()
    assert result == expected

@pytest.mark.asyncio
async def test_create_single_file_should_call_sign_file_once(app_fixture, mock_sign_fixture, mocker):
    create_files()
    images_dir = './'
    files = [
        UploadFile(filename='file_a.jpg', file=open('./file_a', "rb")),
        UploadFile(filename='file_b.jpg', file=open('./file_b', "rb")),
    ]
    mocker.patch('app.config.IMAGES_DIR', images_dir)

    await app_fixture.create_single_file(files)
    mock_sign_fixture.assert_called_once()
