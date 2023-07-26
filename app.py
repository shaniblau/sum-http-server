import logging as log
import os
from typing import List
from config import images_dir
from fastapi import FastAPI, UploadFile
from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES

app = FastAPI()
log.basicConfig(filename='../../sum-http-server/files_created.log', filemode='a', level=log.INFO,
                format='{"@timestamp":"%(asctime)s","log.level":"%(levelname)s","message":"%(message)s"}')


@app.post("/uploadfile")
async def create_upload_file(files: List[UploadFile]):
    if not os.path.exists(images_dir):
        os.mkdir(images_dir)
    await create_single_file(sort_files(files))


def sort_files(files: List[UploadFile]):
    if "_a" in files[0].filename:
        return files
    else:
        return [files[1], files[0]]


async def create_single_file(files: List[UploadFile]):
    name = files[0].filename.split('_')[0]
    file_name = f'{name}.jpg'
    path = os.path.join(images_dir, file_name)
    with open(path, 'ab') as file:
        for f in files:
            file.write(await f.read())
    sign_file(path)
    log.info(f'{name} created successfully')


def sign_file(file_path):
    iv = get_random_bytes(16)
    sha512hash = create_signatures(file_path, iv)
    with open(file_path, 'ab') as file:
        file.write(iv)
        file.write(sha512hash)


def create_signatures(file_path, iv):
    sha512hash = sha512_sign(file_path)
    with open("tornado.key", "rb") as file:
        key = file.read() + b"    "  # [:16]
    aes = AES.new(key, AES.MODE_CFB, iv)
    return aes.encrypt(sha512hash)


def sha512_sign(file_name):
    with open(file_name, 'rb') as f:
        return SHA512.new(f.read()).digest()
