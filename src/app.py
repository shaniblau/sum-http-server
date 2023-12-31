import logging as log
import os
from typing import List
from datetime import datetime

from fastapi import FastAPI, UploadFile

from configuration import config
from sign_file import digital_sign
from set_logger import extendable_logger

app = FastAPI()
current_date = datetime.now().strftime("%d_%m_%Y")
created_logger = extendable_logger('created', f'{config.LOGS_DIR}/files-created/{current_date}.log', log.INFO)
error_logger = extendable_logger('error', f'{config.LOGS_DIR}/errors.log', log.WARNING)


@app.post("/uploadfile")
async def create_upload_file(files: List[UploadFile]):
    try:
        if not os.path.exists(config.IMAGES_DIR):
            os.mkdir(config.IMAGES_DIR)
        await create_single_file(sort_files(files))
    except Exception as e:
        error_logger.error(f'the files {files[0].filename}, {files[1].filename} were not combined due to: {e}')


def sort_files(files: List[UploadFile]):
    if "_a" in files[0].filename:
        return files
    else:
        return [files[1], files[0]]


async def create_single_file(files: List[UploadFile]):
    name = files[0].filename.split('_')[0]
    file_name = f'{name}.jpg'
    path = os.path.join(config.IMAGES_DIR, file_name)
    with open(path, 'ab') as file:
        for f in files:
            file.write(await f.read())
    digital_sign(path)
    created_logger.info(f'the file {name} was created successfully')
