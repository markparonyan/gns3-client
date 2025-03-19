import pytest

from gns3client.api.users import UsersApi, UsersAPI
from gns3client.openapi_client.configuration import Configuration
from gns3client.openapi_client.api_client import ApiClient
from gns3client.openapi_client.exceptions import ApiException


@pytest.fixture
def api():
    return UsersAPI(host="http://test-host:3080")


@pytest.fixture
def access_token():
    return "test-token"


@pytest.fixture
def user_id():
    return "test-user-id"


def test_login(api, mocker):
    mock_api_client = mocker.patch('gns3client.api.users.ApiClient')
    mock_client_instance = mocker.MagicMock()
    mock_api_client.return_value.__enter__.return_value = mock_client_instance
    
    mock_users_api = mocker.patch('gns3client.api.users.UsersApi')
    mock_api_instance = mocker.MagicMock()
    mock_users_api.return_value = mock_api_instance
    mock_api_instance.authenticate_v3_access_users_authenticate_post.return_value.body = {
        "access_token": "new-token-123"
    }
    
    mock_config = mocker.patch('gns3client.api.users.Configuration')
    
    result = api.login(None, "testuser", "password123")
    
    assert result["access_token"] == "new-token-123"
    mock_config.assert_called_once_with(host="http://test-host:3080")
    mock_api_client.assert_called_once()
    mock_users_api.assert_called_once_with(mock_client_instance)
    mock_api_instance.authenticate_v3_access_users_authenticate_post.assert_called_once_with(
        body={"username": "testuser", "password": "password123"}
    )


def test_login_error(api, mocker):
    mock_api_client = mocker.patch('gns3client.api.users.ApiClient')
    mock_client_instance = mocker.MagicMock()
    mock_api_client.return_value.__enter__.return_value = mock_client_instance
    
    mock_users_api = mocker.patch('gns3client.api.users.UsersApi')
    mock_api_instance = mocker.MagicMock()
    mock_users_api.return_value = mock_api_instance
    mock_api_instance.authenticate_v3_access_users_authenticate_post.side_effect = ApiException(status=401, reason="Unauthorized")
    
    mock_handle_exception = mocker.patch.object(api, '_handle_api_exception')
    mock_handle_exception.return_value = {"error": "Authentication failed"}
    
    result = api.login(None, "testuser", "password123")
    
    assert result["error"] == "Authentication failed"
    mock_handle_exception.assert_called_once()


def test_authenticate(api, access_token, mocker):
    mock_users_api = mocker.patch('gns3client.api.users.UsersApi')
    mock_api_instance = mocker.MagicMock()
    mock_users_api.return_value = mock_api_instance
    mock_api_instance.authenticate_v3_access_users_authenticate_post.return_value.body = {
        "authenticated": True,
        "user_id": "user-123"
    }
    
    result = api.authenticate(access_token)
    
    assert result["authenticated"] is True
    assert result["user_id"] == "user-123"
    mock_api_instance.authenticate_v3_access_users_authenticate_post.assert_called_once()


def test_me(api, access_token, mocker):
    mock_users_api = mocker.patch('gns3client.api.users.UsersApi')
    mock_api_instance = mocker.MagicMock()
    mock_users_api.return_value = mock_api_instance
    mock_api_instance.get_logged_in_user_v3_access_users_me_get.return_value.body = {
        "id": "user-123",
        "username": "testuser",
        "email": "test@example.com"
    }
    
    result = api.me(access_token)
    
    assert result["id"] == "user-123"
    assert result["username"] == "testuser"
    mock_api_instance.get_logged_in_user_v3_access_users_me_get.assert_called_once()


def test_list(api, access_token, mocker):
    mock_users_api = mocker.patch('gns3client.api.users.UsersApi')
    mock_api_instance = mocker.MagicMock()
    mock_users_api.return_value = mock_api_instance
    mock_api_instance.get_users_v3_access_users_get.return_value.body = [
        {"id": "user-1", "username": "user1"},
        {"id": "user-2", "username": "user2"}
    ]
    
    result = api.list(access_token)
    
    assert len(result) == 2
    assert result[0]["username"] == "user1"
    assert result[1]["id"] == "user-2"
    mock_api_instance.get_users_v3_access_users_get.assert_called_once()


def test_get(api, access_token, user_id, mocker):
    mock_users_api = mocker.patch('gns3client.api.users.UsersApi')
    mock_api_instance = mocker.MagicMock()
    mock_users_api.return_value = mock_api_instance
    mock_api_instance.get_user_v3_access_users_user_id_get.return_value.body = {
        "id": user_id,
        "username": "testuser",
        "email": "test@example.com"
    }
    
    result = api.get(access_token, user_id)
    
    assert result["id"] == user_id
    assert result["username"] == "testuser"
    mock_api_instance.get_user_v3_access_users_user_id_get.assert_called_once_with(
        path_params={"user_id": user_id}
    )


def test_get_memberships(api, access_token, user_id, mocker):
    mock_users_api = mocker.patch('gns3client.api.users.UsersApi')
    mock_api_instance = mocker.MagicMock()
    mock_users_api.return_value = mock_api_instance
    mock_api_instance.get_user_memberships_v3_access_users_user_id_groups_get.return_value.body = [
        {"group_id": "group-1", "name": "Admins"},
        {"group_id": "group-2", "name": "Users"}
    ]
    
    result = api.get_memberships(access_token, user_id)
    
    assert len(result) == 2
    assert result[0]["name"] == "Admins"
    assert result[1]["group_id"] == "group-2"
    mock_api_instance.get_user_memberships_v3_access_users_user_id_groups_get.assert_called_once_with(
        path_params={"user_id": user_id}
    )


def test_create(api, access_token, mocker):
    mock_users_api = mocker.patch('gns3client.api.users.UsersApi')
    mock_api_instance = mocker.MagicMock()
    mock_users_api.return_value = mock_api_instance
    mock_api_instance.create_user_v3_access_users_post.return_value.body = {
        "id": "new-user-id",
        "username": "newuser",
        "email": "new@example.com"
    }
    
    result = api.create(access_token, "newuser", "password123", email="new@example.com")
    
    assert result["id"] == "new-user-id"
    assert result["username"] == "newuser"
    mock_api_instance.create_user_v3_access_users_post.assert_called_once_with(
        body={
            "username": "newuser",
            "password": "password123",
            "email": "new@example.com"
        }
    )


def test_create_with_full_info(api, access_token, mocker):
    mock_users_api = mocker.patch('gns3client.api.users.UsersApi')
    mock_api_instance = mocker.MagicMock()
    mock_users_api.return_value = mock_api_instance
    mock_api_instance.create_user_v3_access_users_post.return_value.body = {
        "id": "new-user-id",
        "username": "newuser",
        "email": "new@example.com",
        "full_name": "New Test User"
    }
    
    result = api.create(
        access_token, 
        "newuser", 
        "password123", 
        email="new@example.com", 
        full_name="New Test User"
    )
    
    assert result["id"] == "new-user-id"
    assert result["full_name"] == "New Test User"
    mock_api_instance.create_user_v3_access_users_post.assert_called_once_with(
        body={
            "username": "newuser",
            "password": "password123",
            "email": "new@example.com",
            "full_name": "New Test User"
        }
    )


def test_update(api, access_token, user_id, mocker):
    mock_users_api = mocker.patch('gns3client.api.users.UsersApi')
    mock_api_instance = mocker.MagicMock()
    mock_users_api.return_value = mock_api_instance
    mock_api_instance.update_user_v3_access_users_user_id_put.return_value.body = {
        "id": user_id,
        "email": "updated@example.com"
    }
    
    result = api.update(access_token, user_id, email="updated@example.com")
    
    assert result["id"] == user_id
    assert result["email"] == "updated@example.com"
    mock_api_instance.update_user_v3_access_users_user_id_put.assert_called_once_with(
        path_params={"user_id": user_id},
        body={"email": "updated@example.com"}
    )


def test_update_multiple_fields(api, access_token, user_id, mocker):
    mock_users_api = mocker.patch('gns3client.api.users.UsersApi')
    mock_api_instance = mocker.MagicMock()
    mock_users_api.return_value = mock_api_instance
    mock_api_instance.update_user_v3_access_users_user_id_put.return_value.body = {
        "id": user_id,
        "email": "updated@example.com",
        "full_name": "Updated User"
    }
    
    result = api.update(
        access_token, 
        user_id, 
        email="updated@example.com", 
        full_name="Updated User", 
        password="newpass123"
    )
    
    assert result["email"] == "updated@example.com"
    assert result["full_name"] == "Updated User"
    mock_api_instance.update_user_v3_access_users_user_id_put.assert_called_once_with(
        path_params={"user_id": user_id},
        body={
            "email": "updated@example.com",
            "full_name": "Updated User",
            "password": "newpass123"
        }
    )


def test_update_me(api, access_token, mocker):
    mock_users_api = mocker.patch('gns3client.api.users.UsersApi')
    mock_api_instance = mocker.MagicMock()
    mock_users_api.return_value = mock_api_instance
    mock_api_instance.update_logged_in_user_v3_access_users_me_put.return_value.body = {
        "id": "my-user-id",
        "email": "me@example.com",
        "full_name": "My New Name"
    }
    
    result = api.update_me(access_token, full_name="My New Name")
    
    assert result["id"] == "my-user-id"
    assert result["full_name"] == "My New Name"
    mock_api_instance.update_logged_in_user_v3_access_users_me_put.assert_called_once_with(
        body={"full_name": "My New Name"}
    )


def test_update_me_email(api, access_token, mocker):
    mock_users_api = mocker.patch('gns3client.api.users.UsersApi')
    mock_api_instance = mocker.MagicMock()
    mock_users_api.return_value = mock_api_instance
    mock_api_instance.update_logged_in_user_v3_access_users_me_put.return_value.body = {
        "id": "my-user-id",
        "email": "newemail@example.com"
    }
    
    result = api.update_me(access_token, email="newemail@example.com")
    
    assert result["id"] == "my-user-id"
    assert result["email"] == "newemail@example.com"
    mock_api_instance.update_logged_in_user_v3_access_users_me_put.assert_called_once_with(
        body={"email": "newemail@example.com"}
    )


def test_update_me_password(api, access_token, mocker):
    mock_users_api = mocker.patch('gns3client.api.users.UsersApi')
    mock_api_instance = mocker.MagicMock()
    mock_users_api.return_value = mock_api_instance
    mock_api_instance.update_logged_in_user_v3_access_users_me_put.return_value.body = {
        "id": "my-user-id",
        "message": "Password updated successfully"
    }
    
    result = api.update_me(access_token, password="newSecurePassword123")
    
    assert result["id"] == "my-user-id"
    mock_api_instance.update_logged_in_user_v3_access_users_me_put.assert_called_once_with(
        body={"password": "newSecurePassword123"}
    )


def test_update_me_all_fields(api, access_token, mocker):
    mock_users_api = mocker.patch('gns3client.api.users.UsersApi')
    mock_api_instance = mocker.MagicMock()
    mock_users_api.return_value = mock_api_instance
    mock_api_instance.update_logged_in_user_v3_access_users_me_put.return_value.body = {
        "id": "my-user-id",
        "email": "complete@example.com",
        "full_name": "Complete Update User"
    }
    
    result = api.update_me(
        access_token, 
        email="complete@example.com", 
        full_name="Complete Update User", 
        password="completePassword123"
    )
    
    assert result["id"] == "my-user-id"
    assert result["email"] == "complete@example.com"
    assert result["full_name"] == "Complete Update User"
    mock_api_instance.update_logged_in_user_v3_access_users_me_put.assert_called_once_with(
        body={
            "email": "complete@example.com",
            "full_name": "Complete Update User",
            "password": "completePassword123"
        }
    )


def test_delete(api, access_token, user_id, mocker):
    mock_users_api = mocker.patch('gns3client.api.users.UsersApi')
    mock_api_instance = mocker.MagicMock()
    mock_users_api.return_value = mock_api_instance
    mock_api_instance.delete_user_v3_access_users_user_id_delete.return_value.body = {
        "message": "User deleted successfully"
    }
    
    result = api.delete(access_token, user_id)
    
    assert result["message"] == "User deleted successfully"
    mock_api_instance.delete_user_v3_access_users_user_id_delete.assert_called_once_with(
        path_params={"user_id": user_id}
    ) 