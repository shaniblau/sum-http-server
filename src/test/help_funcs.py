from datetime import datetime
import logging as log


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


def set_mockers(mocker, logger_fixture):
    date = datetime.now().strftime("%d_%m_%Y")
    mocker.patch('app.created_logger', logger_fixture(f'./logs/files-created/{date}.log', log.INFO))
    mocker.patch('app.error_logger', logger_fixture(f'./logs/errors.log', log.WARNING))
