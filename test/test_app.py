from fastapi import UploadFile
from fastapi.testclient import TestClient


def test_sort_files(app_fixture):
    file_a = File(filename='file_a.jpg')
    file_b = File(filename="file_b.jpg")
    files = [file_b, file_a]
    expected = [file_a, file_b]
    result = app_fixture.sort_files(files)
    assert result == expected


def test_create_single_file(app_fixture):
    files = [("files", ('file_a.txt', open('file_a.txt', "rb"), "image/jpg")),
             ("files", ('file_b.txt', open('file_b.txt', "rb"), "image/jpg"))]
    app_fixture.create_single_file(files)
    expected_file_content = b'ab'
    with open('../../Images/file_jpg', 'rb') as file:
        result = file.read()
    assert expected_file_content == result


class File:
    def __init__(self, filename, content=''):
        self.filename = filename
        self.content = content
