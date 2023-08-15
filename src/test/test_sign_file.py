from unittest.mock import patch, mock_open

from Crypto.Random import get_random_bytes


def test_sign_should_call_create_encrypted_hash_once(sign_fixture, mock_create_encrypted_hash_fixture):
    mock_file = mock_open()
    with patch('sign_file.open', mock_file):
        sign_fixture.sign('file.jpg')
    mock_create_encrypted_hash_fixture.assert_called_once()


def test_create_encrypted_hash_should_call_create_sha512_once(sign_fixture, mock_create_sha512_fixture):
    iv = get_random_bytes(16)
    with patch('sign_file.open'), patch('sign_file.AES.new'):
        sign_fixture.create_encrypted_hash('file.jpg', iv)
    mock_create_sha512_fixture.assert_called_once()
