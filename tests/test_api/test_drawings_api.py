import pytest

from gns3client.api.drawings import DrawingsAPI


@pytest.fixture
def api():
    return DrawingsAPI(host="http://test-host:3080")


@pytest.fixture
def access_token():
    return "test-token"


@pytest.fixture
def project_id():
    return "test-project-id"


@pytest.fixture
def drawing_id():
    return "test-drawing-id"


def test_get_drawings(api, access_token, project_id, mocker):
    mock_drawings_api = mocker.patch('gns3client.api.drawings.DrawingsApi')
    mock_api_instance = mocker.MagicMock()
    mock_drawings_api.return_value = mock_api_instance
    mock_api_instance.get_drawings_v3_projects_project_id_drawings_get.return_value.body = [
        {"id": "drawing1", "svg": "<svg>drawing1</svg>"},
        {"id": "drawing2", "svg": "<svg>drawing2</svg>"}
    ]

    result = api.get_drawings(access_token, project_id)

    assert len(result) == 2
    assert result[0]["id"] == "drawing1"
    assert result[1]["svg"] == "<svg>drawing2</svg>"
    mock_api_instance.get_drawings_v3_projects_project_id_drawings_get.assert_called_once_with(project_id)


def test_get_drawing(api, access_token, project_id, drawing_id, mocker):
    mock_drawings_api = mocker.patch('gns3client.api.drawings.DrawingsApi')
    mock_api_instance = mocker.MagicMock()
    mock_drawings_api.return_value = mock_api_instance
    mock_api_instance.get_drawing_v3_projects_project_id_drawings_drawing_id_get.return_value.body = {
        "id": drawing_id,
        "svg": "<svg>test drawing</svg>",
        "z": 0
    }

    result = api.get_drawing(access_token, project_id, drawing_id)

    assert result["id"] == drawing_id
    assert result["svg"] == "<svg>test drawing</svg>"
    mock_api_instance.get_drawing_v3_projects_project_id_drawings_drawing_id_get.assert_called_once_with(
        project_id, drawing_id
    )


def test_create_drawing(api, access_token, project_id, mocker):
    mock_drawings_api = mocker.patch('gns3client.api.drawings.DrawingsApi')
    mock_api_instance = mocker.MagicMock()
    mock_drawings_api.return_value = mock_api_instance
    mock_api_instance.create_drawing_v3_projects_project_id_drawings_post.return_value.body = {
        "id": "new-drawing-id",
        "svg": "<svg>new drawing</svg>",
        "x": 100,
        "y": 150,
        "z": 0
    }
    
    drawing_data = {
        "svg": "<svg>new drawing</svg>",
        "x": 100,
        "y": 150,
        "z": 0
    }

    result = api.create_drawing(access_token, project_id, drawing_data)

    assert result["id"] == "new-drawing-id"
    assert result["svg"] == "<svg>new drawing</svg>"
    assert result["x"] == 100
    assert result["y"] == 150
    mock_api_instance.create_drawing_v3_projects_project_id_drawings_post.assert_called_once_with(
        project_id, body=drawing_data
    )


def test_update_drawing(api, access_token, project_id, drawing_id, mocker):
    mock_drawings_api = mocker.patch('gns3client.api.drawings.DrawingsApi')
    mock_api_instance = mocker.MagicMock()
    mock_drawings_api.return_value = mock_api_instance
    mock_api_instance.update_drawing_v3_projects_project_id_drawings_drawing_id_put.return_value.body = {
        "id": drawing_id,
        "svg": "<svg>updated drawing</svg>",
        "x": 200,
        "y": 250,
        "z": 1
    }
    
    drawing_data = {
        "svg": "<svg>updated drawing</svg>",
        "x": 200,
        "y": 250,
        "z": 1
    }

    result = api.update_drawing(access_token, project_id, drawing_id, drawing_data)

    assert result["id"] == drawing_id
    assert result["svg"] == "<svg>updated drawing</svg>"
    assert result["x"] == 200
    assert result["y"] == 250
    mock_api_instance.update_drawing_v3_projects_project_id_drawings_drawing_id_put.assert_called_once_with(
        project_id, drawing_id, body=drawing_data
    )


def test_delete_drawing(api, access_token, project_id, drawing_id, mocker):
    mock_drawings_api = mocker.patch('gns3client.api.drawings.DrawingsApi')
    mock_api_instance = mocker.MagicMock()
    mock_drawings_api.return_value = mock_api_instance
    mock_api_instance.delete_drawing_v3_projects_project_id_drawings_drawing_id_delete.return_value.body = {
        "message": "Drawing deleted"
    }

    result = api.delete_drawing(access_token, project_id, drawing_id)

    assert result["message"] == "Drawing deleted"
    mock_api_instance.delete_drawing_v3_projects_project_id_drawings_drawing_id_delete.assert_called_once_with(
        project_id, drawing_id
    ) 