import pytest

from gns3client.api.controller import ControllerAPI


@pytest.fixture
def api():
    return ControllerAPI(host="http://test-host:3080")


@pytest.fixture
def access_token():
    return "test-token"


def test_version(api, mocker):
    mock_controller_api = mocker.patch('gns3client.api.controller.ControllerApi')
    mock_api_instance = mocker.MagicMock()
    mock_controller_api.return_value = mock_api_instance
    mock_api_instance.get_version_v3_version_get.return_value.body = {
        "version": "2.2.39",
        "local": True
    }

    result = api.version()

    assert result["version"] == "2.2.39"
    assert result["local"] is True
    mock_api_instance.get_version_v3_version_get.assert_called_once()


def test_version_with_access_token(api, access_token, mocker):
    mock_controller_api = mocker.patch('gns3client.api.controller.ControllerApi')
    mock_api_instance = mocker.MagicMock()
    mock_controller_api.return_value = mock_api_instance
    mock_api_instance.get_version_v3_version_get.return_value.body = {
        "version": "2.2.39",
        "local": True
    }

    result = api.version(access_token)

    assert result["version"] == "2.2.39"
    assert result["local"] is True
    mock_api_instance.get_version_v3_version_get.assert_called_once()


def test_stats(api, access_token, mocker):
    mock_controller_api = mocker.patch('gns3client.api.controller.ControllerApi')
    mock_api_instance = mocker.MagicMock()
    mock_controller_api.return_value = mock_api_instance
    mock_api_instance.get_statistics_v3_statistics_get.return_value.body = {
        "projects": 5,
        "drawings": 10,
        "nodes": 25,
        "links": 30
    }

    result = api.stats(access_token)

    assert result["projects"] == 5
    assert result["nodes"] == 25
    mock_api_instance.get_statistics_v3_statistics_get.assert_called_once()


def test_shutdown(api, access_token, mocker):
    mock_controller_api = mocker.patch('gns3client.api.controller.ControllerApi')
    mock_api_instance = mocker.MagicMock()
    mock_controller_api.return_value = mock_api_instance
    mock_api_instance.shutdown_v3_shutdown_post.return_value.body = {
        "message": "Controller is shutting down"
    }

    result = api.shutdown(access_token)

    assert result["message"] == "Controller is shutting down"
    mock_api_instance.shutdown_v3_shutdown_post.assert_called_once()


def test_reload(api, access_token, mocker):
    mock_controller_api = mocker.patch('gns3client.api.controller.ControllerApi')
    mock_api_instance = mocker.MagicMock()
    mock_controller_api.return_value = mock_api_instance
    mock_api_instance.reload_v3_reload_post.return_value.body = {
        "message": "Controller is reloading"
    }

    result = api.reload(access_token)

    assert result["message"] == "Controller is reloading"
    mock_api_instance.reload_v3_reload_post.assert_called_once()


def test_notifications(api, access_token, mocker):
    mock_controller_api = mocker.patch('gns3client.api.controller.ControllerApi')
    mock_api_instance = mocker.MagicMock()
    mock_controller_api.return_value = mock_api_instance
    mock_api_instance.get_notifications_v3_notifications_get.return_value.body = [
        {"id": "notification1", "message": "Test notification 1"},
        {"id": "notification2", "message": "Test notification 2"}
    ]

    result = api.notifications(access_token)

    assert len(result) == 2
    assert result[0]["id"] == "notification1"
    assert result[1]["message"] == "Test notification 2"
    mock_api_instance.get_notifications_v3_notifications_get.assert_called_once() 