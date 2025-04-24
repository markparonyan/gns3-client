import pytest

from gns3client.api.snapshots import SnapshotsAPI


@pytest.fixture
def api():
    return SnapshotsAPI(host="http://test-host:3080")


@pytest.fixture
def access_token():
    return "test-token"


@pytest.fixture
def project_id():
    return "test-project-id"


@pytest.fixture
def snapshot_id():
    return "test-snapshot-id"


def test_list(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.snapshots.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.get_snapshots_v3_projects_project_id_snapshots_get.return_value.body = [
        {"id": "snapshot1", "name": "Snapshot 1", "created_at": "2023-01-01T00:00:00Z"},
        {"id": "snapshot2", "name": "Snapshot 2", "created_at": "2023-01-02T00:00:00Z"}
    ]

    result = api.list(access_token, project_id)

    assert len(result) == 2
    assert result[0]["name"] == "Snapshot 1"
    assert result[1]["created_at"] == "2023-01-02T00:00:00Z"
    mock_api_instance.get_snapshots_v3_projects_project_id_snapshots_get.assert_called_once_with(
        path_params={"project_id": project_id}
    )


def test_get(api, access_token, project_id, snapshot_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.snapshots.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.get_snapshot_v3_projects_project_id_snapshots_snapshot_id_get.return_value.body = {
        "id": snapshot_id,
        "name": "Test Snapshot",
        "created_at": "2023-01-01T00:00:00Z"
    }

    result = api.get(access_token, project_id, snapshot_id)

    assert result["id"] == snapshot_id
    assert result["name"] == "Test Snapshot"
    mock_api_instance.get_snapshot_v3_projects_project_id_snapshots_snapshot_id_get.assert_called_once_with(
        path_params={"project_id": project_id, "snapshot_id": snapshot_id}
    )


def test_create(api, access_token, project_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.snapshots.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.create_snapshot_v3_projects_project_id_snapshots_post.return_value.body = {
        "id": "new-snapshot-id",
        "name": "New Snapshot",
        "created_at": "2023-01-03T00:00:00Z"
    }

    result = api.create(access_token, project_id, "New Snapshot")

    assert result["id"] == "new-snapshot-id"
    assert result["name"] == "New Snapshot"
    mock_api_instance.create_snapshot_v3_projects_project_id_snapshots_post.assert_called_once_with(
        path_params={"project_id": project_id},
        body={"name": "New Snapshot"}
    )


def test_update(api, access_token, project_id, snapshot_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.snapshots.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.update_snapshot_v3_projects_project_id_snapshots_snapshot_id_put.return_value.body = {
        "id": snapshot_id,
        "name": "Updated Snapshot",
        "created_at": "2023-01-01T00:00:00Z"
    }

    result = api.update(access_token, project_id, snapshot_id, "Updated Snapshot")

    assert result["id"] == snapshot_id
    assert result["name"] == "Updated Snapshot"
    mock_api_instance.update_snapshot_v3_projects_project_id_snapshots_snapshot_id_put.assert_called_once_with(
        path_params={"project_id": project_id, "snapshot_id": snapshot_id},
        body={"name": "Updated Snapshot"}
    )


def test_delete(api, access_token, project_id, snapshot_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.snapshots.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.delete_snapshot_v3_projects_project_id_snapshots_snapshot_id_delete.return_value.body = {
        "message": "Snapshot deleted"
    }

    result = api.delete(access_token, project_id, snapshot_id)

    assert result["message"] == "Snapshot deleted"
    mock_api_instance.delete_snapshot_v3_projects_project_id_snapshots_snapshot_id_delete.assert_called_once_with(
        path_params={"project_id": project_id, "snapshot_id": snapshot_id}
    )


def test_restore(api, access_token, project_id, snapshot_id, mocker):
    mock_projects_api = mocker.patch('gns3client.api.snapshots.ProjectsApi')
    mock_api_instance = mocker.MagicMock()
    mock_projects_api.return_value = mock_api_instance
    mock_api_instance.restore_snapshot_v3_projects_project_id_snapshots_snapshot_id_restore_post.return_value.body = {
        "message": "Snapshot restored"
    }

    result = api.restore(access_token, project_id, snapshot_id)

    assert result["message"] == "Snapshot restored"
    mock_api_instance.restore_snapshot_v3_projects_project_id_snapshots_snapshot_id_restore_post.assert_called_once_with(
        path_params={"project_id": project_id, "snapshot_id": snapshot_id}
    ) 