class File:
    def __init__(self, filename, content=''):
        self.filename = filename
        self.content = content


def create_files():
    with open('./file_a', 'wb') as file:
        file.write(b'a')
    with open('./file_b', 'wb') as file:
        file.write(b'b')