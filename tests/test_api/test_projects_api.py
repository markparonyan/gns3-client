import pytest

from gns3client.api.projects import ProjectsAPI


@pytest.fixture
def api():
    return ProjectsAPI(host="http://test-host:3080")


@pytest.fixture
def access_token():
    return "test-token"


@pytest.fixture
def project_id():
    return "test-project-id"


def test_list(api, access_token, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.get_projects_v3_projects_get.return_value.body = [
        {"id": "project1", "name": "Project 1"},
        {"id": "project2", "name": "Project 2"}
    ]

    result = api.list(access_token)

    assert len(result) == 2
    assert result[0]["name"] == "Project 1"
    assert result[1]["name"] == "Project 2"
    mock_api_instance.get_projects_v3_projects_get.assert_called_once()


def test_get(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.get_project_v3_projects_project_id_get.return_value.body = {
        "id": project_id,
        "name": "Test Project",
        "status": "opened"
    }

    result = api.get(access_token, project_id)

    assert result["id"] == project_id
    assert result["name"] == "Test Project"
    mock_api_instance.get_project_v3_projects_project_id_get.assert_called_once_with(
        path_params={"project_id": project_id}
    )


def test_create(api, access_token, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.create_project_v3_projects_post.return_value.body = {
        "id": "new-project-id",
        "name": "New Project",
        "status": "closed"
    }

    result = api.create(access_token, "New Project", status="closed")

    assert result["name"] == "New Project"
    assert result["status"] == "closed"
    mock_api_instance.create_project_v3_projects_post.assert_called_once_with(
        body={"name": "New Project", "status": "closed"}
    )


def test_delete(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.delete_project_v3_projects_project_id_delete.return_value.body = {}

    result = api.delete(access_token, project_id)

    assert result == {}
    mock_api_instance.delete_project_v3_projects_project_id_delete.assert_called_once_with(
        path_params={"project_id": project_id}
    )


def test_update(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.update_project_v3_projects_project_id_put.return_value.body = {
        "id": project_id,
        "name": "Updated Project",
        "status": "opened"
    }

    result = api.update(access_token, project_id, name="Updated Project")

    assert result["name"] == "Updated Project"
    mock_api_instance.update_project_v3_projects_project_id_put.assert_called_once_with(
        path_params={"project_id": project_id},
        body={"name": "Updated Project"}
    )


def test_open(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.open_project_v3_projects_project_id_open_post.return_value.body = {
        "id": project_id,
        "status": "opened"
    }

    result = api.open(access_token, project_id)

    assert result["status"] == "opened"
    mock_api_instance.open_project_v3_projects_project_id_open_post.assert_called_once_with(
        path_params={"project_id": project_id}
    )


def test_close(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.close_project_v3_projects_project_id_close_post.return_value.body = {
        "id": project_id,
        "status": "closed"
    }

    result = api.close(access_token, project_id)

    assert result["status"] == "closed"
    mock_api_instance.close_project_v3_projects_project_id_close_post.assert_called_once_with(
        path_params={"project_id": project_id}
    )


def test_duplicate(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.duplicate_project_v3_projects_project_id_duplicate_post.return_value.body = {
        "id": "duplicated-project-id",
        "name": "Duplicated Project",
        "status": "closed"
    }

    result = api.duplicate(access_token, project_id, name="Duplicated Project")

    assert result["name"] == "Duplicated Project"
    mock_api_instance.duplicate_project_v3_projects_project_id_duplicate_post.assert_called_once_with(
        path_params={"project_id": project_id},
        body={"name": "Duplicated Project"}
    )


def test_duplicate_without_name(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.duplicate_project_v3_projects_project_id_duplicate_post.return_value.body = {
        "id": "duplicated-project-id",
        "name": "Test Project Copy",
        "status": "closed"
    }

    result = api.duplicate(access_token, project_id)

    assert result["name"] == "Test Project Copy"
    mock_api_instance.duplicate_project_v3_projects_project_id_duplicate_post.assert_called_once_with(
        path_params={"project_id": project_id},
        body={}
    )


def test_export(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.export_project_v3_projects_project_id_export_get.return_value.body = b'project_file_content'

    result = api.export(access_token, project_id)

    assert result == b'project_file_content'
    mock_api_instance.export_project_v3_projects_project_id_export_get.assert_called_once_with(
        path_params={"project_id": project_id}
    )


def test_import_project(api, access_token, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.import_project_v3_projects_import_post.return_value.body = {
        "id": "imported-project-id",
        "name": "Imported Project",
        "status": "closed"
    }
    project_file = b'project_file_content'

    result = api.import_(access_token, project_file, name="Imported Project")

    assert result["name"] == "Imported Project"
    mock_api_instance.import_project_v3_projects_import_post.assert_called_once_with(
        body={"project": project_file, "name": "Imported Project"}
    )


def test_import_project_without_name(api, access_token, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.import_project_v3_projects_import_post.return_value.body = {
        "id": "imported-project-id",
        "name": "Default Name",
        "status": "closed"
    }
    project_file = b'project_file_content'

    result = api.import_(access_token, project_file)

    assert result["name"] == "Default Name"
    mock_api_instance.import_project_v3_projects_import_post.assert_called_once_with(
        body={"project": project_file}
    )


def test_stats(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.get_project_stats_v3_projects_project_id_stats_get.return_value.body = {
        "cpu_usage_percent": 15.2,
        "memory_usage_percent": 45.7
    }

    result = api.stats(access_token, project_id)

    assert result["cpu_usage_percent"] == 15.2
    assert result["memory_usage_percent"] == 45.7
    mock_api_instance.get_project_stats_v3_projects_project_id_stats_get.assert_called_once_with(
        path_params={"project_id": project_id}
    )


def test_load(api, access_token, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.load_project_v3_projects_load_post.return_value.body = {
        "id": "loaded-project-id",
        "name": "Loaded Project"
    }
    path = "/path/to/project"

    result = api.load(access_token, path)

    assert result["name"] == "Loaded Project"
    mock_api_instance.load_project_v3_projects_load_post.assert_called_once_with(
        body={"path": path}
    )


def test_notifications(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.project_http_notifications_v3_projects_project_id_notifications_get.return_value.body = [
        {"action": "node.created", "event": {"node_id": "node1"}},
        {"action": "link.created", "event": {"link_id": "link1"}}
    ]

    result = api.notifications(access_token, project_id)

    assert len(result) == 2
    assert result[0]["action"] == "node.created"
    mock_api_instance.project_http_notifications_v3_projects_project_id_notifications_get.assert_called_once_with(
        path_params={"project_id": project_id}
    )


def test_locked(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.locked_project_v3_projects_project_id_locked_get.return_value.body = {
        "locked": True,
        "user": "test-user"
    }

    result = api.locked(access_token, project_id)

    assert result["locked"] is True
    assert result["user"] == "test-user"
    mock_api_instance.locked_project_v3_projects_project_id_locked_get.assert_called_once_with(
        path_params={"project_id": project_id}
    )


def test_lock(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.lock_project_v3_projects_project_id_lock_post.return_value.body = {
        "project_id": project_id,
        "locked": True
    }

    result = api.lock(access_token, project_id)

    assert result["locked"] is True
    mock_api_instance.lock_project_v3_projects_project_id_lock_post.assert_called_once_with(
        path_params={"project_id": project_id}
    )


def test_unlock(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.unlock_project_v3_projects_project_id_unlock_post.return_value.body = {
        "project_id": project_id,
        "locked": False
    }

    result = api.unlock(access_token, project_id)

    assert result["locked"] is False
    mock_api_instance.unlock_project_v3_projects_project_id_unlock_post.assert_called_once_with(
        path_params={"project_id": project_id}
    )


def test_get_file(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_content = b"file content"
    mock_api_instance.get_file_v3_projects_project_id_files_file_path_get.return_value.body = mock_content
    file_path = "configs/router1.txt"

    result = api.get_file(access_token, project_id, file_path)

    assert result == mock_content
    mock_api_instance.get_file_v3_projects_project_id_files_file_path_get.assert_called_once_with(
        path_params={"project_id": project_id, "file_path": file_path}
    )


def test_write_file(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    file_path = "configs/router1.txt"
    body = "new content"
    mock_api_instance.write_file_v3_projects_project_id_files_file_path_post.return_value.body = {
        "path": file_path
    }

    result = api.write_file(access_token, project_id, file_path, body)

    assert result["path"] == file_path
    mock_api_instance.write_file_v3_projects_project_id_files_file_path_post.assert_called_once_with(
        path_params={"project_id": project_id, "file_path": file_path},
        body=body
    )


def test_create_node_from_template(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    template_id = "template-id-123"
    node_params = {
        "x": 100,
        "y": 100,
        "name": "Router1"
    }
    mock_api_instance.create_node_from_template_v3_projects_project_id_templates_template_id_post.return_value.body = {
        "node_id": "node-id-123",
        "name": "Router1"
    }

    result = api.create_node_from_template(access_token, project_id, template_id, **node_params)

    assert result["node_id"] == "node-id-123"
    assert result["name"] == "Router1"
    mock_api_instance.create_node_from_template_v3_projects_project_id_templates_template_id_post.assert_called_once_with(
        path_params={"project_id": project_id, "template_id": template_id},
        body=node_params
    )


def test_create_node_from_template_no_params(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.projects.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    template_id = "template-id-123"
    mock_api_instance.create_node_from_template_v3_projects_project_id_templates_template_id_post.return_value.body = {
        "node_id": "node-id-123",
        "name": "Router1"
    }

    result = api.create_node_from_template(access_token, project_id, template_id)

    assert result["node_id"] == "node-id-123"
    mock_api_instance.create_node_from_template_v3_projects_project_id_templates_template_id_post.assert_called_once_with(
        path_params={"project_id": project_id, "template_id": template_id},
        body=None
    )
