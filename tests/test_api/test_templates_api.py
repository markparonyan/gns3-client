import pytest

from gns3client.api.templates import TemplatesAPI


@pytest.fixture
def api():
    return TemplatesAPI(host="http://test-host:3080")


@pytest.fixture
def access_token():
    return "test-token"


@pytest.fixture
def template_id():
    return "test-template-id"


def test_list(api, access_token, mocker):
    mock_templates_api = mocker.patch('gns3client.api.templates.TemplatesApi')
    mock_api_instance = mocker.MagicMock()
    mock_templates_api.return_value = mock_api_instance
    mock_api_instance.templates_get.return_value.body = [
        {"id": "template1", "name": "Template 1"},
        {"id": "template2", "name": "Template 2"}
    ]

    result = api.list(access_token)

    assert len(result) == 2
    assert result[0]["name"] == "Template 1"
    assert result[1]["id"] == "template2"
    mock_api_instance.templates_get.assert_called_once()


def test_get(api, access_token, template_id, mocker):
    mock_templates_api = mocker.patch('gns3client.api.templates.TemplatesApi')
    mock_api_instance = mocker.MagicMock()
    mock_templates_api.return_value = mock_api_instance
    mock_api_instance.templates_template_id_get.return_value.body = {
        "id": template_id,
        "name": "Test Template",
        "template_type": "qemu"
    }

    result = api.get(access_token, template_id)

    assert result["id"] == template_id
    assert result["name"] == "Test Template"
    assert result["template_type"] == "qemu"
    mock_api_instance.templates_template_id_get.assert_called_once_with(template_id)


def test_create(api, access_token, mocker):
    mock_templates_api = mocker.patch('gns3client.api.templates.TemplatesApi')
    mock_api_instance = mocker.MagicMock()
    mock_templates_api.return_value = mock_api_instance
    mock_api_instance.templates_post.return_value.body = {
        "id": "new-template-id",
        "name": "New Template",
        "template_type": "qemu",
        "image": "ubuntu.qcow2"
    }

    result = api.create(
        access_token, 
        "New Template", 
        template_type="qemu", 
        image="ubuntu.qcow2"
    )

    assert result["id"] == "new-template-id"
    assert result["name"] == "New Template"
    assert result["template_type"] == "qemu"
    mock_api_instance.templates_post.assert_called_once_with(
        {
            "name": "New Template",
            "template_type": "qemu",
            "image": "ubuntu.qcow2"
        }
    )


def test_update(api, access_token, template_id, mocker):
    mock_templates_api = mocker.patch('gns3client.api.templates.TemplatesApi')
    mock_api_instance = mocker.MagicMock()
    mock_templates_api.return_value = mock_api_instance
    mock_api_instance.templates_template_id_put.return_value.body = {
        "id": template_id,
        "name": "Updated Template",
        "memory": 512
    }

    result = api.update(access_token, template_id, name="Updated Template", memory=512)

    assert result["id"] == template_id
    assert result["name"] == "Updated Template"
    assert result["memory"] == 512
    mock_api_instance.templates_template_id_put.assert_called_once_with(
        template_id,
        {
            "name": "Updated Template",
            "memory": 512
        }
    )


def test_delete(api, access_token, template_id, mocker):
    mock_templates_api = mocker.patch('gns3client.api.templates.TemplatesApi')
    mock_api_instance = mocker.MagicMock()
    mock_templates_api.return_value = mock_api_instance
    mock_api_instance.templates_template_id_delete.return_value.body = {
        "message": "Template deleted"
    }

    result = api.delete(access_token, template_id)

    assert result["message"] == "Template deleted"
    mock_api_instance.templates_template_id_delete.assert_called_once_with(template_id)


def test_duplicate_template(api, access_token, template_id, mocker):
    mock_templates_api = mocker.patch('gns3client.api.templates.TemplatesApi')
    mock_api_instance = mocker.MagicMock()
    mock_templates_api.return_value = mock_api_instance
    mock_api_instance.duplicate_template_v3_templates_template_id_duplicate_post.return_value.body = {
        "id": "duplicated-template-id",
        "name": "Duplicated Template",
        "template_type": "qemu"
    }

    result = api.duplicate_template(access_token, template_id, name="Duplicated Template")

    assert result["id"] == "duplicated-template-id"
    assert result["name"] == "Duplicated Template"
    mock_api_instance.duplicate_template_v3_templates_template_id_duplicate_post.assert_called_once_with(
        template_id,
        body={"name": "Duplicated Template"}
    )


def test_duplicate_template_without_name(api, access_token, template_id, mocker):
    mock_templates_api = mocker.patch('gns3client.api.templates.TemplatesApi')
    mock_api_instance = mocker.MagicMock()
    mock_templates_api.return_value = mock_api_instance
    mock_api_instance.duplicate_template_v3_templates_template_id_duplicate_post.return_value.body = {
        "id": "duplicated-template-id",
        "name": "Test Template Copy",
        "template_type": "qemu"
    }

    result = api.duplicate_template(access_token, template_id)

    assert result["id"] == "duplicated-template-id"
    assert result["name"] == "Test Template Copy"
    mock_api_instance.duplicate_template_v3_templates_template_id_duplicate_post.assert_called_once_with(
        template_id,
        body={}
    ) 