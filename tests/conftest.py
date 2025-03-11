import pytest


@pytest.fixture
def mock_api_response(mocker):
    response = mocker.MagicMock()
    response.body = {}
    return response


@pytest.fixture
def mock_api_instance(mocker):
    instance = mocker.MagicMock()
    return instance


@pytest.fixture
def access_token():
    return "test-access-token"


@pytest.fixture
def test_host():
    return "http://test-host:3080"
