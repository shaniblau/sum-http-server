from datetime import datetime
import logging as log

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


def prepare_create_upload_file(mocker, logger_fixture):
    date = datetime.now().strftime("%d_%m_%Y")
    mocker.patch('app.created_logger', logger_fixture(f'./logs/files-created/{date}.log', log.INFO))
    mocker.patch('app.error_logger', logger_fixture(f'./logs/errors.log', log.WARNING))


async def prepare_create_single_file(mocker, app_fixture):
    create_files()
    files = [
        UploadFile(filename='file_a.jpg', file=open('./file_a', "rb")),
        UploadFile(filename='file_b.jpg', file=open('./file_b', "rb")),
    ]
    mocker.patch('app.config.IMAGES_DIR', './')
    mocker.patch('app.sign')
    await app_fixture.create_single_file(files)
