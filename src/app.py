import logging as log
import os
from typing import List
from datetime import datetime

from fastapi import FastAPI, UploadFile

from configuration import config
from sign_file import sign
from set_logger import extendable_logger

app = FastAPI()
date = datetime.now().strftime("%d_%m_%Y")


@app.post("/uploadfile")
async def create_upload_file(files: List[UploadFile]):
    created_logger = extendable_logger(f'../logs/files-created/{date}.log', log.INFO)
    error_logger = extendable_logger('../logs/errors.log', log.WARNING)
    try:
        if not os.path.exists(config.IMAGES_DIR):
            os.mkdir(config.IMAGES_DIR)
        await create_single_file(sort_files(files), created_logger)
    except Exception:
        error_logger.error(f'the files {files[0].filename}, {files[1].filename} were not combined')


def sort_files(files: List[UploadFile]):
    if "_a" in files[0].filename:
        return files
    else:
        return [files[1], files[0]]


async def create_single_file(files: List[UploadFile], created_logger):
    name = files[0].filename.split('_')[0]
    file_name = f'{name}.jpg'
    path = os.path.join(config.IMAGES_DIR, file_name)
    with open(path, 'ab') as file:
        for f in files:
            file.write(await f.read())
    sign(path)
    created_logger.info(f'the file {name} was created successfully')
