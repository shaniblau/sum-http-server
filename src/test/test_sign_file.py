from unittest.mock import patch, mock_open


def test_sign_should_call_create_encrypted_hash_once(sign_fixture, mock_create_encrypted_hash_fixture):
    mock_file = mock_open()
    with patch('sign_file.open', mock_file):
        sign_fixture.sign('file.jpg')
    mock_create_encrypted_hash_fixture.assert_called_once()