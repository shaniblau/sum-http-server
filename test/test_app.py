import builtins
import os

import pytest
from fastapi import UploadFile
from fastapi.testclient import TestClient


def test_create_upload_file_endpoint(app_fixture):
    client = TestClient(app_fixture.app)
    create_files()
    files = [('files', ('file_a', open('/home/runner/work/sum-http-client/images/file_a', "rb"), "image/jpg")),
             ('files', ('file_b', open('/home/runner/work/sum-http-client/images/file_b', "rb"), "image/jpg"))]
    response = client.post("/uploadfile", files=files)
    assert response.status_code == 200


def test_sort_files(app_fixture):
    file_a = File(filename='file_a.jpg')
    file_b = File(filename="file_b.jpg")
    files = [file_b, file_a]
    expected = [file_a, file_b]
    result = app_fixture.sort_files(files)
    assert result == expected


@pytest.mark.asyncio
async def test_create_single_file(app_fixture, mocker):
    create_files()
    images_dir = '/home/runner/work/sum-http-client/images'
    files = [
        UploadFile(filename='file_a.jpg', file=open('/home/runner/work/sum-http-client/images/file_a', "rb")),
        UploadFile(filename='file_b.jpg', file=open('/home/runner/work/sum-http-client/images/file_b', "rb")),
    ]
    mocker.patch('app.open', side_effect=lambda file, mode: builtins.open(os.path.join(images_dir, file), mode))
    mocker.patch('app.sign_file')
    await app_fixture.create_single_file(files)
    expected = b'ab'
    with open(os.path.join(images_dir, 'file.jpg'), 'rb') as file:
        result = file.read()
    assert result == expected


class File:
    def __init__(self, filename, content=''):
        self.filename = filename
        self.content = content


def create_files():
    if not os.path.exists('/home/runner/work/sum-http-client/images'):
        os.makedirs('/home/runner/work/sum-http-client/images')
    with open('/home/runner/work/sum-http-client/images/file_a', 'wb') as file:
        file.write(b'a')
    with open('/home/runner/work/sum-http-client/images/file_b', 'wb') as file:
        file.write(b'b')
