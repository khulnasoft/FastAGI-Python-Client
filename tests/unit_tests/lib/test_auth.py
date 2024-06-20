import pytest
from unittest.mock import patch
from fastagi_client.lib.auth import validate_api_key
from fastagi_client.exceptions import UnauthorizedException


@patch("requests.get")
def test_validate_api_key_success(mock_get):
    mock_get.return_value.status_code = 200
    validate_api_key("http://test.com", "test_key")


@patch("requests.get")
def test_validate_api_key_failure(mock_get):
    mock_get.return_value.status_code = 401
    with pytest.raises(UnauthorizedException):
        validate_api_key("http://test.com", "test_key")
