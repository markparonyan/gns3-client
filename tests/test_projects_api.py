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

    result = api.import_project(access_token, project_file, name="Imported Project")

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

    result = api.import_project(access_token, project_file)

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