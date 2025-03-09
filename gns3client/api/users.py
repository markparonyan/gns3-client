from gns3client.openapi_client.apis.tags.users_api import UsersApi
from gns3client.openapi_client.configuration import Configuration
from gns3client.openapi_client.api_client import ApiClient
from gns3client.openapi_client.exceptions import ApiException
from gns3client.api.base_api import BaseAPI

class UsersAPI(BaseAPI):
    """API wrapper for GNS3 Users API."""

    def login(self, access_token, username, password):
        """Login to the GNS3 server and get an access token.
        
        Args:
            username (str): The username
            password (str): The password
            
        Returns:
            dict: The response containing the access token if successful
        """
        try:
            configuration = Configuration(host=self.host)
            with ApiClient(configuration) as api_client:
                api_instance = UsersApi(api_client)
                api_response = api_instance.authenticate_v3_access_users_authenticate_post(
                    body={"username": username, "password": password}
                )
                return api_response.body
        except ApiException as e:
            return self._handle_api_exception(e, "UsersApi->authenticate_v3_access_users_authenticate_post")
    
    def authenticate(self, access_token):
        """Verify if an access token is valid.
        
        Args:
            access_token (str): The OAuth2 access token to verify
            
        Returns:
            dict: The response data if successful
        """
        return self._call_api(
            access_token,
            UsersApi,
            "authenticate_v3_access_users_authenticate_post",
            "UsersApi->authenticate_v3_access_users_authenticate_post"
        )
    
    def me(self, access_token):
        """Get information about the currently logged in user.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            
        Returns:
            dict: The user information
        """
        return self._call_api(
            access_token,
            UsersApi,
            "get_logged_in_user_v3_access_users_me_get",
            "UsersApi->get_logged_in_user_v3_access_users_me_get"
        )
    
    def list(self, access_token):
        """Get a list of all users.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            
        Returns:
            list: The list of users
        """
        return self._call_api(
            access_token,
            UsersApi,
            "get_users_v3_access_users_get",
            "UsersApi->get_users_v3_access_users_get"
        )
    
    def get(self, access_token, user_id):
        """Get information about a specific user.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            user_id (str): The ID of the user to get
            
        Returns:
            dict: The user information
        """
        return self._call_api(
            access_token,
            UsersApi,
            "get_user_v3_access_users_user_id_get",
            "UsersApi->get_user_v3_access_users_user_id_get",
            path_params={"user_id": user_id}
        )
    
    def get_memberships(self, access_token, user_id):
        """Get the group memberships for a specific user.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            user_id (str): The ID of the user to get memberships for
            
        Returns:
            list: The list of group memberships
        """
        return self._call_api(
            access_token,
            UsersApi,
            "get_user_memberships_v3_access_users_user_id_groups_get",
            "UsersApi->get_user_memberships_v3_access_users_user_id_groups_get",
            path_params={"user_id": user_id}
        )
    
    def create(self, access_token, username, password, email=None, full_name=None):
        """Create a new user.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            username (str): The username for the new user
            password (str): The password for the new user
            email (str, optional): The email address for the new user
            full_name (str, optional): The full name for the new user
            
        Returns:
            dict: The created user information
        """
        user_data = {
            "username": username,
            "password": password
        }
        if email:
            user_data["email"] = email
        if full_name:
            user_data["full_name"] = full_name
            
        return self._call_api(
            access_token,
            UsersApi,
            "create_user_v3_access_users_post",
            "UsersApi->create_user_v3_access_users_post",
            body=user_data
        )
    
    def update(self, access_token, user_id, email=None, full_name=None, password=None):
        """Update a user's information.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            user_id (str): The ID of the user to update
            email (str, optional): The new email address
            full_name (str, optional): The new full name
            password (str, optional): The new password
            
        Returns:
            dict: The updated user information
        """
        user_data = {}
        if email is not None:
            user_data["email"] = email
        if full_name is not None:
            user_data["full_name"] = full_name
        if password is not None:
            user_data["password"] = password
            
        return self._call_api(
            access_token,
            UsersApi,
            "update_user_v3_access_users_user_id_put",
            "UsersApi->update_user_v3_access_users_user_id_put",
            path_params={"user_id": user_id},
            body=user_data
        )
    
    def update_me(self, access_token, email=None, full_name=None, password=None):
        """Update the currently logged in user's information.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            email (str, optional): The new email address
            full_name (str, optional): The new full name
            password (str, optional): The new password
            
        Returns:
            dict: The updated user information
        """
        user_data = {}
        if email is not None:
            user_data["email"] = email
        if full_name is not None:
            user_data["full_name"] = full_name
        if password is not None:
            user_data["password"] = password
            
        return self._call_api(
            access_token,
            UsersApi,
            "update_logged_in_user_v3_access_users_me_put",
            "UsersApi->update_logged_in_user_v3_access_users_me_put",
            body=user_data
        )
    
    def delete(self, access_token, user_id):
        """Delete a user.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            user_id (str): The ID of the user to delete
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            UsersApi,
            "delete_user_v3_access_users_user_id_delete",
            "UsersApi->delete_user_v3_access_users_user_id_delete",
            path_params={"user_id": user_id}
        )


