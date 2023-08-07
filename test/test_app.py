# import os
# import pytest
# from fastapi import UploadFile
# from fastapi.testclient import TestClient

from help_funcs import create_files, File


#
#
# def test_create_upload_file_endpoint(app_fixture):
#     client = TestClient(app_fixture.app)
#     create_files()
#     files = [('files', ('file_a', open('./file_a', "rb"), "image/jpg")),
#              ('files', ('file_b', open('./file_b', "rb"), "image/jpg"))]
#     response = client.post("/uploadfile", files=files)
#     assert response.status_code == 200
#
#
def test_sort_files(app_fixture):
    file_a = File(filename='file_a.jpg')
    file_b = File(filename="file_b.jpg")
    files = [file_b, file_a]
    expected = [file_a, file_b]
    result = app_fixture.sort_files(files)
    assert result == expected

#
# @pytest.mark.asyncio
# async def test_create_single_file(app_fixture, sign_fixture, mocker):
#     create_files()
#     images_dir = './'
#     files = [
#         UploadFile(filename='file_a.jpg', file=open('./file_a', "rb")),
#         UploadFile(filename='file_b.jpg', file=open('./file_b', "rb")),
#     ]
#     mocker.patch('app.config.IMAGES_DIR', images_dir)
#     mocker.patch('app.sign')
#     await app_fixture.create_single_file(files)
#     expected = b'ab'
#     with open(os.path.join(images_dir, 'file.jpg'), 'rb') as file:
#         result = file.read()
#     assert result == expected
