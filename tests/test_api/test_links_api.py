import pytest

from gns3client.api.links import LinksAPI


@pytest.fixture
def api():
    return LinksAPI(host="http://test-host:3080")


@pytest.fixture
def access_token():
    return "test-token"


@pytest.fixture
def project_id():
    return "test-project-id"


@pytest.fixture
def link_id():
    return "test-link-id"


def test_list(api, access_token, project_id, mocker):
    mock_links_api = mocker.patch('gns3client.api.links.LinksApi')
    mock_api_instance = mocker.MagicMock()
    mock_links_api.return_value = mock_api_instance
    mock_api_instance.get_links_v3_projects_project_id_links_get.return_value.body = [
        {"id": "link1", "type": "ethernet"},
        {"id": "link2", "type": "ethernet"}
    ]

    result = api.list(access_token, project_id)

    assert len(result) == 2
    assert result[0]["id"] == "link1"
    assert result[1]["type"] == "ethernet"
    mock_api_instance.get_links_v3_projects_project_id_links_get.assert_called_once_with(
        path_params={"project_id": project_id}
    )


def test_get(api, access_token, project_id, link_id, mocker):
    mock_links_api = mocker.patch('gns3client.api.links.LinksApi')
    mock_api_instance = mocker.MagicMock()
    mock_links_api.return_value = mock_api_instance
    mock_api_instance.get_link_v3_projects_project_id_links_link_id_get.return_value.body = {
        "id": link_id,
        "type": "ethernet",
        "nodes": [
            {"node_id": "node1", "adapter_number": 0, "port_number": 0},
            {"node_id": "node2", "adapter_number": 0, "port_number": 0}
        ]
    }

    result = api.get(access_token, project_id, link_id)

    assert result["id"] == link_id
    assert result["type"] == "ethernet"
    assert len(result["nodes"]) == 2
    mock_api_instance.get_link_v3_projects_project_id_links_link_id_get.assert_called_once_with(
        path_params={"project_id": project_id, "link_id": link_id}
    )


def test_create(api, access_token, project_id, mocker):
    mock_links_api = mocker.patch('gns3client.api.links.LinksApi')
    mock_api_instance = mocker.MagicMock()
    mock_links_api.return_value = mock_api_instance
    mock_api_instance.create_link_v3_projects_project_id_links_post.return_value.body = {
        "id": "new-link-id",
        "type": "ethernet",
        "nodes": [
            {"node_id": "node1", "adapter_number": 0, "port_number": 0},
            {"node_id": "node2", "adapter_number": 0, "port_number": 0}
        ]
    }
    
    link_data = {
        "nodes": [
            {"node_id": "node1", "adapter_number": 0, "port_number": 0},
            {"node_id": "node2", "adapter_number": 0, "port_number": 0}
        ]
    }

    result = api.create(access_token, project_id, link_data)

    assert result["id"] == "new-link-id"
    assert result["type"] == "ethernet"
    assert len(result["nodes"]) == 2
    mock_api_instance.create_link_v3_projects_project_id_links_post.assert_called_once_with(
        path_params={"project_id": project_id},
        body=link_data
    )


def test_update(api, access_token, project_id, link_id, mocker):
    mock_links_api = mocker.patch('gns3client.api.links.LinksApi')
    mock_api_instance = mocker.MagicMock()
    mock_links_api.return_value = mock_api_instance
    mock_api_instance.update_link_v3_projects_project_id_links_link_id_put.return_value.body = {
        "id": link_id,
        "type": "ethernet",
        "suspend": True
    }
    
    link_data = {"suspend": True}

    result = api.update(access_token, project_id, link_id, link_data)

    assert result["id"] == link_id
    assert result["suspend"] is True
    mock_api_instance.update_link_v3_projects_project_id_links_link_id_put.assert_called_once_with(
        path_params={"project_id": project_id, "link_id": link_id},
        body=link_data
    )


def test_delete(api, access_token, project_id, link_id, mocker):
    mock_links_api = mocker.patch('gns3client.api.links.LinksApi')
    mock_api_instance = mocker.MagicMock()
    mock_links_api.return_value = mock_api_instance
    mock_api_instance.delete_link_v3_projects_project_id_links_link_id_delete.return_value.body = {
        "message": "Link deleted"
    }

    result = api.delete(access_token, project_id, link_id)

    assert result["message"] == "Link deleted"
    mock_api_instance.delete_link_v3_projects_project_id_links_link_id_delete.assert_called_once_with(
        path_params={"project_id": project_id, "link_id": link_id}
    )


def test_start_capture(api, access_token, project_id, link_id, mocker):
    mock_links_api = mocker.patch('gns3client.api.links.LinksApi')
    mock_api_instance = mocker.MagicMock()
    mock_links_api.return_value = mock_api_instance
    mock_api_instance.start_capture_on_link_v3_projects_project_id_links_link_id_capture_start_post.return_value.body = {
        "message": "Capture started"
    }
    
    capture_data = {"capture_file_name": "test.pcap"}

    result = api.start_capture(access_token, project_id, link_id, capture_data)

    assert result["message"] == "Capture started"
    mock_api_instance.start_capture_on_link_v3_projects_project_id_links_link_id_capture_start_post.assert_called_once_with(
        path_params={"project_id": project_id, "link_id": link_id},
        body=capture_data
    )


def test_start_capture_without_data(api, access_token, project_id, link_id, mocker):
    mock_links_api = mocker.patch('gns3client.api.links.LinksApi')
    mock_api_instance = mocker.MagicMock()
    mock_links_api.return_value = mock_api_instance
    mock_api_instance.start_capture_on_link_v3_projects_project_id_links_link_id_capture_start_post.return_value.body = {
        "message": "Capture started"
    }

    result = api.start_capture(access_token, project_id, link_id)

    assert result["message"] == "Capture started"
    mock_api_instance.start_capture_on_link_v3_projects_project_id_links_link_id_capture_start_post.assert_called_once_with(
        path_params={"project_id": project_id, "link_id": link_id},
        body={}
    )


def test_stop_capture(api, access_token, project_id, link_id, mocker):
    mock_links_api = mocker.patch('gns3client.api.links.LinksApi')
    mock_api_instance = mocker.MagicMock()
    mock_links_api.return_value = mock_api_instance
    mock_api_instance.stop_capture_on_link_v3_projects_project_id_links_link_id_capture_stop_post.return_value.body = {
        "message": "Capture stopped"
    }

    result = api.stop_capture(access_token, project_id, link_id)

    assert result["message"] == "Capture stopped"
    mock_api_instance.stop_capture_on_link_v3_projects_project_id_links_link_id_capture_stop_post.assert_called_once_with(
        path_params={"project_id": project_id, "link_id": link_id}
    )


def test_get_capture_stream(api, access_token, project_id, link_id, mocker):
    mock_links_api = mocker.patch('gns3client.api.links.LinksApi')
    mock_api_instance = mocker.MagicMock()
    mock_links_api.return_value = mock_api_instance
    mock_api_instance.get_link_capture_stream_v3_projects_project_id_links_link_id_capture_stream_get.return_value.body = b'packet_data'

    result = api.get_capture_stream(access_token, project_id, link_id)

    assert result == b'packet_data'
    mock_api_instance.get_link_capture_stream_v3_projects_project_id_links_link_id_capture_stream_get.assert_called_once_with(
        path_params={"project_id": project_id, "link_id": link_id}
    )


def test_get_available_filters(api, access_token, project_id, link_id, mocker):
    mock_links_api = mocker.patch('gns3client.api.links.LinksApi')
    mock_api_instance = mocker.MagicMock()
    mock_links_api.return_value = mock_api_instance
    mock_api_instance.get_link_available_filters_v3_projects_project_id_links_link_id_available_filters_get.return_value.body = [
        {"name": "filter1", "description": "Test filter 1"},
        {"name": "filter2", "description": "Test filter 2"}
    ]

    result = api.get_available_filters(access_token, project_id, link_id)

    assert len(result) == 2
    assert result[0]["name"] == "filter1"
    assert result[1]["description"] == "Test filter 2"
    mock_api_instance.get_link_available_filters_v3_projects_project_id_links_link_id_available_filters_get.assert_called_once_with(
        path_params={"project_id": project_id, "link_id": link_id}
    )


def test_reset(api, access_token, project_id, link_id, mocker):
    mock_links_api = mocker.patch('gns3client.api.links.LinksApi')
    mock_api_instance = mocker.MagicMock()
    mock_links_api.return_value = mock_api_instance
    mock_api_instance.reset_link_v3_projects_project_id_links_link_id_reset_post.return_value.body = {
        "message": "Link reset"
    }

    result = api.reset(access_token, project_id, link_id)

    assert result["message"] == "Link reset"
    mock_api_instance.reset_link_v3_projects_project_id_links_link_id_reset_post.assert_called_once_with(
        path_params={"project_id": project_id, "link_id": link_id}
    ) 
