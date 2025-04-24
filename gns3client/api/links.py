from gns3client.openapi_client.apis.tags.links_api import LinksApi
from gns3client.api.base_api import BaseAPI


class LinksAPI(BaseAPI):
    """API wrapper for GNS3 Links API."""

    def list(self, access_token, project_id):
        """Get all links in a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            
        Returns:
            list: The list of links in the project
        """
        return self._call_api(
            access_token,
            LinksApi,
            "get_links_v3_projects_project_id_links_get",
            "LinksApi->get_links_v3_projects_project_id_links_get",
            path_params={"project_id": project_id}
        )
            
    def get(self, access_token, project_id, link_id):
        """Get a specific link in a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            link_id (str): The ID of the link
            
        Returns:
            dict: The link details
        """
        return self._call_api(
            access_token,
            LinksApi,
            "get_link_v3_projects_project_id_links_link_id_get",
            "LinksApi->get_link_v3_projects_project_id_links_link_id_get",
            path_params={"project_id": project_id, "link_id": link_id}
        )
            
    def create(self, access_token, project_id, link_data):
        """Create a new link in a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            link_data (dict): The link configuration data
            
        Returns:
            dict: The created link details
        """
        return self._call_api(
            access_token,
            LinksApi,
            "create_link_v3_projects_project_id_links_post",
            "LinksApi->create_link_v3_projects_project_id_links_post",
            path_params={"project_id": project_id},
            body=link_data
        )
            
    def update(self, access_token, project_id, link_id, link_data):
        """Update a link in a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            link_id (str): The ID of the link to update
            link_data (dict): The updated link configuration data
            
        Returns:
            dict: The updated link details
        """
        return self._call_api(
            access_token,
            LinksApi,
            "update_link_v3_projects_project_id_links_link_id_put",
            "LinksApi->update_link_v3_projects_project_id_links_link_id_put",
            path_params={"project_id": project_id, "link_id": link_id},
            body=link_data
        )
            
    def delete(self, access_token, project_id, link_id):
        """Delete a link from a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            link_id (str): The ID of the link to delete
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            LinksApi,
            "delete_link_v3_projects_project_id_links_link_id_delete",
            "LinksApi->delete_link_v3_projects_project_id_links_link_id_delete",
            path_params={"project_id": project_id, "link_id": link_id}
        )
    
    def reset(self, access_token, project_id, link_id):
        """Reset a link.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            link_id (str): The ID of the link to reset
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            LinksApi,
            "reset_link_v3_projects_project_id_links_link_id_reset_post",
            "LinksApi->reset_link_v3_projects_project_id_links_link_id_reset_post",
            path_params={"project_id": project_id, "link_id": link_id}
        ) 
            
    def start_capture(self, access_token, project_id, link_id, capture_data=None):
        """Start packet capture on a link.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            link_id (str): The ID of the link
            capture_data (dict, optional): Capture configuration data
            
        Returns:
            dict: The response data
        """
        body = capture_data if capture_data else {}
        
        return self._call_api(
            access_token,
            LinksApi,
            "start_capture_on_link_v3_projects_project_id_links_link_id_capture_start_post",
            "LinksApi->start_capture_on_link_v3_projects_project_id_links_link_id_capture_start_post",
            path_params={"project_id": project_id, "link_id": link_id},
            body=body
        )
            
    def stop_capture(self, access_token, project_id, link_id):
        """Stop packet capture on a link.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            link_id (str): The ID of the link
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            LinksApi,
            "stop_capture_on_link_v3_projects_project_id_links_link_id_capture_stop_post",
            "LinksApi->stop_capture_on_link_v3_projects_project_id_links_link_id_capture_stop_post",
            path_params={"project_id": project_id, "link_id": link_id}
        )
            
    def get_capture_stream(self, access_token, project_id, link_id):
        """Get the packet capture stream from a link.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            link_id (str): The ID of the link
            
        Returns:
            bytes: The capture stream data
        """
        return self._call_api(
            access_token,
            LinksApi,
            "get_link_capture_stream_v3_projects_project_id_links_link_id_capture_stream_get",
            "LinksApi->get_link_capture_stream_v3_projects_project_id_links_link_id_capture_stream_get",
            path_params={"project_id": project_id, "link_id": link_id}
        )
            
    def get_available_filters(self, access_token, project_id, link_id):
        """Get available packet filters for a link.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            link_id (str): The ID of the link
            
        Returns:
            list: The available filters
        """
        return self._call_api(
            access_token,
            LinksApi,
            "get_link_available_filters_v3_projects_project_id_links_link_id_available_filters_get",
            "LinksApi->get_link_available_filters_v3_projects_project_id_links_link_id_available_filters_get",
            path_params={"project_id": project_id, "link_id": link_id}
        )
            
