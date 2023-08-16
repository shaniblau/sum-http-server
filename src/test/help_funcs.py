import os

from fastapi import UploadFile


class File:
    def __init__(self, filename, content=''):
        self.filename = filename
        self.content = content


def create_files():
    with open('./file_a', 'wb') as file:
        file.write(b'a')
    with open('./file_b', 'wb') as file:
        file.write(b'b')
    return [('files', ('file_a', open('./file_a', "rb"), "image/jpg")),
            ('files', ('file_b', open('./file_b', "rb"), "image/jpg"))]


async def prepare_create_single_file(mocker, app_fixture):
    create_files()
    files = [
        UploadFile(filename='file_a.jpg', file=open('./file_a', "rb")),
        UploadFile(filename='file_b.jpg', file=open('./file_b', "rb")),
    ]
    mocker.patch('app.config.IMAGES_DIR', './')
    await app_fixture.create_single_file(files)


def cleanup():
    files_names = ['file_a', 'file_b']
    for name in files_names:
        file_path = os.path.join('./', name)
        os.remove(file_path)
