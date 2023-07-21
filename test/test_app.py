import os
from fastapi import UploadFile
from fastapi.testclient import TestClient


def test_create_upload_file_endpoint(app_fixture):
    client = TestClient(app_fixture)
    files = [
        ("file_a.jpg", b"Test file content A"),
        ("file_b.jpg", b"Test file content B"),
    ]
    response = client.post("/uploadfile", files=files)
    assert response.status_code == 200


def test_sort_files(app_fixture):
    file_a = File(filename='file_a.jpg')
    file_b = File(filename="file_b.jpg")
    files = [file_b, file_a]
    expected = [file_a, file_b]
    result = app_fixture.sort_files(files)
    assert result == expected


def test_create_single_file(app_fixture, mocker):
    create_files()
    files = [UploadFile(filename='file_a', file=open('/home/runner/work/sum-http-client/images/file_a', "rb")),
             UploadFile(filename='file_a', file=open('/home/runner/work/sum-http-client/images/file_a', "rb"))]
    mocker.patch('app.sing_file')
    app_fixture.create_single_file(files)
    expected = b'ab'
    with open('/home/runner/work/sum-http-client/images/file.jpg', 'rb') as file:
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



