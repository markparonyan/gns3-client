import pytest

from gns3client.api.nodes import NodesAPI


@pytest.fixture
def api():
    return NodesAPI(host="http://test-host:3080")


@pytest.fixture
def access_token():
    return "test-token"


@pytest.fixture
def project_id():
    return "test-project-id"


@pytest.fixture
def node_id():
    return "test-node-id"


def test_list(api, access_token, project_id, mocker):
    mock_nodes_api = mocker.patch('gns3client.api.nodes.NodesApi')
    mock_api_instance = mocker.MagicMock()
    mock_nodes_api.return_value = mock_api_instance
    mock_api_instance.get_nodes_v3_projects_project_id_nodes_get.return_value.body = [
        {"id": "node1", "name": "Node 1", "node_type": "vpcs"},
        {"id": "node2", "name": "Node 2", "node_type": "qemu"}
    ]

    result = api.list(access_token, project_id)

    assert len(result) == 2
    assert result[0]["name"] == "Node 1"
    assert result[1]["node_type"] == "qemu"
    mock_api_instance.get_nodes_v3_projects_project_id_nodes_get.assert_called_once_with(
        path_params={"project_id": project_id}
    )


def test_get(api, access_token, project_id, node_id, mocker):
    mock_nodes_api = mocker.patch('gns3client.api.nodes.NodesApi')
    mock_api_instance = mocker.MagicMock()
    mock_nodes_api.return_value = mock_api_instance
    mock_api_instance.get_node_v3_projects_project_id_nodes_node_id_get.return_value.body = {
        "id": node_id,
        "name": "Test Node",
        "node_type": "vpcs",
        "status": "started"
    }

    result = api.get(access_token, project_id, node_id)

    assert result["id"] == node_id
    assert result["name"] == "Test Node"
    assert result["status"] == "started"
    mock_api_instance.get_node_v3_projects_project_id_nodes_node_id_get.assert_called_once_with(
        path_params={"project_id": project_id, "node_id": node_id}
    )


def test_create(api, access_token, project_id, mocker):
    mock_nodes_api = mocker.patch('gns3client.api.nodes.NodesApi')
    mock_api_instance = mocker.MagicMock()
    mock_nodes_api.return_value = mock_api_instance
    mock_api_instance.create_node_v3_projects_project_id_nodes_post.return_value.body = {
        "id": "new-node-id",
        "name": "New Node",
        "node_type": "vpcs",
        "status": "stopped"
    }
    
    node_data = {
        "name": "New Node",
        "node_type": "vpcs"
    }

    result = api.create(access_token, project_id, node_data)

    assert result["id"] == "new-node-id"
    assert result["name"] == "New Node"
    assert result["node_type"] == "vpcs"
    mock_api_instance.create_node_v3_projects_project_id_nodes_post.assert_called_once_with(
        path_params={"project_id": project_id},
        body=node_data
    )


def test_update(api, access_token, project_id, node_id, mocker):
    mock_nodes_api = mocker.patch('gns3client.api.nodes.NodesApi')
    mock_api_instance = mocker.MagicMock()
    mock_nodes_api.return_value = mock_api_instance
    mock_api_instance.update_node_v3_projects_project_id_nodes_node_id_put.return_value.body = {
        "id": node_id,
        "name": "Updated Node",
        "node_type": "vpcs"
    }
    
    node_data = {"name": "Updated Node"}

    result = api.update(access_token, project_id, node_id, node_data)

    assert result["id"] == node_id
    assert result["name"] == "Updated Node"
    mock_api_instance.update_node_v3_projects_project_id_nodes_node_id_put.assert_called_once_with(
        path_params={"project_id": project_id, "node_id": node_id},
        body=node_data
    )


def test_delete(api, access_token, project_id, node_id, mocker):
    mock_nodes_api = mocker.patch('gns3client.api.nodes.NodesApi')
    mock_api_instance = mocker.MagicMock()
    mock_nodes_api.return_value = mock_api_instance
    mock_api_instance.delete_node_v3_projects_project_id_nodes_node_id_delete.return_value.body = {
        "message": "Node deleted"
    }

    result = api.delete(access_token, project_id, node_id)

    assert result["message"] == "Node deleted"
    mock_api_instance.delete_node_v3_projects_project_id_nodes_node_id_delete.assert_called_once_with(
        path_params={"project_id": project_id, "node_id": node_id}
    )


def test_start(api, access_token, project_id, node_id, mocker):
    mock_nodes_api = mocker.patch('gns3client.api.nodes.NodesApi')
    mock_api_instance = mocker.MagicMock()
    mock_nodes_api.return_value = mock_api_instance
    mock_api_instance.start_node_v3_projects_project_id_nodes_node_id_start_post.return_value.body = {
        "id": node_id,
        "name": "Test Node",
        "status": "started"
    }

    result = api.start(access_token, project_id, node_id)

    assert result["id"] == node_id
    assert result["status"] == "started"
    mock_api_instance.start_node_v3_projects_project_id_nodes_node_id_start_post.assert_called_once_with(
        path_params={"project_id": project_id, "node_id": node_id}
    )


def test_stop(api, access_token, project_id, node_id, mocker):
    mock_nodes_api = mocker.patch('gns3client.api.nodes.NodesApi')
    mock_api_instance = mocker.MagicMock()
    mock_nodes_api.return_value = mock_api_instance
    mock_api_instance.stop_node_v3_projects_project_id_nodes_node_id_stop_post.return_value.body = {
        "id": node_id,
        "name": "Test Node",
        "status": "stopped"
    }

    result = api.stop(access_token, project_id, node_id)

    assert result["id"] == node_id
    assert result["status"] == "stopped"
    mock_api_instance.stop_node_v3_projects_project_id_nodes_node_id_stop_post.assert_called_once_with(
        path_params={"project_id": project_id, "node_id": node_id}
    )


def test_suspend(api, access_token, project_id, node_id, mocker):
    mock_nodes_api = mocker.patch('gns3client.api.nodes.NodesApi')
    mock_api_instance = mocker.MagicMock()
    mock_nodes_api.return_value = mock_api_instance
    mock_api_instance.suspend_node_v3_projects_project_id_nodes_node_id_suspend_post.return_value.body = {
        "id": node_id,
        "name": "Test Node",
        "status": "suspended"
    }

    result = api.suspend(access_token, project_id, node_id)

    assert result["id"] == node_id
    assert result["status"] == "suspended"
    mock_api_instance.suspend_node_v3_projects_project_id_nodes_node_id_suspend_post.assert_called_once_with(
        path_params={"project_id": project_id, "node_id": node_id}
    )


def test_reload(api, access_token, project_id, node_id, mocker):
    mock_nodes_api = mocker.patch('gns3client.api.nodes.NodesApi')
    mock_api_instance = mocker.MagicMock()
    mock_nodes_api.return_value = mock_api_instance
    mock_api_instance.reload_node_v3_projects_project_id_nodes_node_id_reload_post.return_value.body = {
        "id": node_id,
        "name": "Test Node",
        "status": "started"
    }

    result = api.reload(access_token, project_id, node_id)

    assert result["id"] == node_id
    assert result["status"] == "started"
    mock_api_instance.reload_node_v3_projects_project_id_nodes_node_id_reload_post.assert_called_once_with(
        path_params={"project_id": project_id, "node_id": node_id}
    )


def test_duplicate(api, access_token, project_id, node_id, mocker):
    mock_nodes_api = mocker.patch('gns3client.api.nodes.NodesApi')
    mock_api_instance = mocker.MagicMock()
    mock_nodes_api.return_value = mock_api_instance
    mock_api_instance.duplicate_node_v3_projects_project_id_nodes_node_id_duplicate_post.return_value.body = {
        "id": "duplicated-node-id",
        "name": "Test Node Clone",
        "node_type": "vpcs",
        "status": "stopped"
    }

    result = api.duplicate(access_token, project_id, node_id, name="Test Node Clone")

    assert result["id"] == "duplicated-node-id"
    assert result["name"] == "Test Node Clone"
    mock_api_instance.duplicate_node_v3_projects_project_id_nodes_node_id_duplicate_post.assert_called_once_with(
        path_params={"project_id": project_id, "node_id": node_id},
        body={"name": "Test Node Clone"}
    )


def test_start_all(api, access_token, project_id, mocker):
    mock_nodes_api = mocker.patch('gns3client.api.nodes.NodesApi')
    mock_api_instance = mocker.MagicMock()
    mock_nodes_api.return_value = mock_api_instance
    mock_api_instance.start_all_nodes_v3_projects_project_id_nodes_start_post.return_value.body = {
        "message": "All nodes started"
    }

    result = api.start_all(access_token, project_id)

    assert result["message"] == "All nodes started"
    mock_api_instance.start_all_nodes_v3_projects_project_id_nodes_start_post.assert_called_once_with(
        path_params={"project_id": project_id}
    )


def test_stop_all(api, access_token, project_id, mocker):
    mock_nodes_api = mocker.patch('gns3client.api.nodes.NodesApi')
    mock_api_instance = mocker.MagicMock()
    mock_nodes_api.return_value = mock_api_instance
    mock_api_instance.stop_all_nodes_v3_projects_project_id_nodes_stop_post.return_value.body = {
        "message": "All nodes stopped"
    }

    result = api.stop_all(access_token, project_id)

    assert result["message"] == "All nodes stopped"
    mock_api_instance.stop_all_nodes_v3_projects_project_id_nodes_stop_post.assert_called_once_with(
        path_params={"project_id": project_id}
    )


def test_suspend_all(api, access_token, project_id, mocker):
    mock_nodes_api = mocker.patch('gns3client.api.nodes.NodesApi')
    mock_api_instance = mocker.MagicMock()
    mock_nodes_api.return_value = mock_api_instance
    mock_api_instance.suspend_all_nodes_v3_projects_project_id_nodes_suspend_post.return_value.body = {
        "message": "All nodes suspended"
    }

    result = api.suspend_all(access_token, project_id)

    assert result["message"] == "All nodes suspended"
    mock_api_instance.suspend_all_nodes_v3_projects_project_id_nodes_suspend_post.assert_called_once_with(
        path_params={"project_id": project_id}
    )


def test_reload_all(api, access_token, project_id, mocker):
    mock_nodes_api = mocker.patch('gns3client.api.nodes.NodesApi')
    mock_api_instance = mocker.MagicMock()
    mock_nodes_api.return_value = mock_api_instance
    mock_api_instance.reload_all_nodes_v3_projects_project_id_nodes_reload_post.return_value.body = {
        "message": "All nodes reloaded"
    }

    result = api.reload_all(access_token, project_id)

    assert result["message"] == "All nodes reloaded"
    mock_api_instance.reload_all_nodes_v3_projects_project_id_nodes_reload_post.assert_called_once_with(
        path_params={"project_id": project_id}
    ) 