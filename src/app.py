import logging as log
import os
from typing import List
from configuration import config
from fastapi import FastAPI, UploadFile
from datetime import datetime
from sign_file import sign

app = FastAPI()
date = datetime.now().strftime("%d_%m_%Y")
log.basicConfig(filename=f'files-created{date}.log', filemode='a', level=log.INFO,
                format='{"@timestamp":"%(asctime)s","log.level":"%(levelname)s","message":"%(message)s"}')


@app.post("/uploadfile")
async def create_upload_file(files: List[UploadFile]):
    if not os.path.exists(config.IMAGES_DIR):
        os.mkdir(config.IMAGES_DIR)
    await create_single_file(sort_files(files))


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
    sign(path)
    log.info(f'{name} created successfully')