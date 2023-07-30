import logging as log
import os
from typing import List
import config
from fastapi import FastAPI, UploadFile

from sign_file import execute

app = FastAPI()
log.basicConfig(filename='files_created.log', filemode='a', level=log.INFO,
                format='{"@timestamp":"%(asctime)s","log.level":"%(levelname)s","message":"%(message)s"}')


@app.post("/uploadfile")
async def create_upload_file(files: List[UploadFile]):
    path_variable = os.environ.get('PATH')
    print(path_variable)
    if not os.path.exists(config.images_dir):
        os.mkdir(config.images_dir)
    await create_single_file(sort_files(files))


def sort_files(files: List[UploadFile]):
    if "_a" in files[0].filename:
        return files
    else:
        return [files[1], files[0]]


# add conf - done
async def create_single_file(files: List[UploadFile]):
    name = files[0].filename.split('_')[0]
    file_name = f'{name}.jpg'
    path = os.path.join(config.images_dir, file_name)
    with open(path, 'ab') as file:
        for f in files:
            file.write(await f.read())
    execute(path)
    log.info(f'{name} created successfully')
