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