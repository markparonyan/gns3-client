import json
import pytest

from gns3client.api.base_api import BaseAPI


@pytest.fixture
def api():
    return BaseAPI(host="http://test-host:3080")


@pytest.fixture
def access_token():
    return "test-token"


def test_init(api):
    assert api.host == "http://test-host:3080"


def test_get_api_client(api, access_token, mocker):
    mock_config = mocker.patch('gns3client.api.base_api.Configuration')
    mock_config_instance = mocker.MagicMock()
    mock_config.return_value = mock_config_instance
    
    mock_api_client = mocker.patch('gns3client.api.base_api.ApiClient')
    mock_client_instance = mocker.MagicMock()
    mock_client_instance.default_headers = {}
    mock_api_client.return_value = mock_client_instance
    
    client, config = api._get_api_client(access_token)
    
    mock_config.assert_called_once_with(
        host="http://test-host:3080", 
        access_token=access_token
    )
    mock_api_client.assert_called_once_with(mock_config_instance)
    assert mock_client_instance.default_headers["Authorization"] == f"Bearer {access_token}"
    assert client == mock_client_instance
    assert config == mock_config_instance


def test_handle_api_exception_with_json_body(api, mocker):
    e = mocker.MagicMock()
    e.status = 404
    e.reason = "Not Found"
    e.body = json.dumps({"detail": "Project not found"})
    
    result = api._handle_api_exception(e, "test_operation")
    
    assert result["error"] == "API Error: test_operation"
    assert result["status"] == 404
    assert result["reason"] == "Not Found"
    assert result["detail"] == "Project not found"


def test_handle_api_exception_with_non_json_body(api, mocker):
    e = mocker.MagicMock()
    e.status = 500
    e.reason = "Server Error"
    e.body = "Internal server error occurred"
    
    result = api._handle_api_exception(e, "test_operation")
    
    assert result["error"] == "API Error: test_operation"
    assert result["status"] == 500
    assert result["reason"] == "Server Error"
    assert result["body"] == "Internal server error occurred"
