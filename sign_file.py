from Crypto.Hash import SHA512
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES


# move to different location - done
def execute(file_path):
    iv = get_random_bytes(16)
    encrypted_hash = create_encrypted_hash(file_path, iv)
    with open(file_path, 'ab') as file:
        file.write(iv)
        file.write(encrypted_hash)


def create_encrypted_hash(file_path, iv):
    sha512hash = create_sha512(file_path)
    with open("tornado.key", "rb") as file:
        key = file.read() + b"    "
    aes = AES.new(key, AES.MODE_CFB, iv)
    return aes.encrypt(sha512hash)


def create_sha512(file_name):
    with open(file_name, 'rb') as f:
        return SHA512.new(f.read()).digest()
