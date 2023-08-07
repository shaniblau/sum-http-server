from unittest.mock import patch, mock_open

from Crypto.Random import get_random_bytes


def test_sign_should_call_create_encrypted_hash_once(sign_fixture, mock_create_encrypted_hash_fixture):
    mock_file = mock_open()
    with patch('sign_file.open', mock_file):
        sign_fixture.sign('file.jpg')
    mock_create_encrypted_hash_fixture.assert_called_once()


def test_create_encrypted_hash_should_call_create_sha512_once(sign_fixture, mock_create_sha512_fixture):
    iv = get_random_bytes(16)
    mock_file = mock_open()
    with patch('sign_file.open', mock_file):
        sign_fixture.create_encrypted_hash('file.jpg', iv)
    mock_create_sha512_fixture.assert_called_once()


# def test_create_sha512(sign_fixture):
#     # Test creating a SHA-512 hash
#     hash_value = sign_fixture.create_sha512('test_file.txt')
#     assert len(hash_value) == 64  # SHA-512 produces a 64-byte hash
#
#
# def test_create_encrypted_hash(sign_fixture):
#     # Test creating an encrypted hash
#     file_path = 'test_file.txt'
#     iv = b'\x00' * 16  # Replace with a valid IV
#     encrypted_hash = sign_fixture.create_encrypted_hash(file_path, iv)
#     assert len(encrypted_hash) == 64  # Assuming AES encryption produces a 64-byte output
#
#
# def test_sign(tmp_path, sign_fixture):
#     # Test signing a file
#     file_path = os.path.join(tmp_path, 'test_file.txt')
#     with open(file_path, 'wb') as f:
#         f.write(b'This is a test file content')
#     # Perform the signing operation
#     sign_fixture.sign(file_path)
#     # Assert that the file now contains the expected content
#     with open(file_path, 'rb') as f:
#         content = f.read()
#         assert len(content) >= 16 + 64  # IV + encrypted hash
