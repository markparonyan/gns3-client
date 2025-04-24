from gns3client.openapi_client.apis.tags.drawings_api import DrawingsApi
from gns3client.api.base_api import BaseAPI


class DrawingsAPI(BaseAPI):
    """API wrapper for GNS3 Drawings API."""

    def get_drawings(self, access_token, project_id):
        """Get all drawings in a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            
        Returns:
            list: The list of drawings in the project
        """
        return self._call_api(
            access_token,
            DrawingsApi,
            "get_drawings_v3_projects_project_id_drawings_get",
            "DrawingsApi->get_drawings_v3_projects_project_id_drawings_get",
            project_id
        )
            
    def get_drawing(self, access_token, project_id, drawing_id):
        """Get a specific drawing in a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            drawing_id (str): The ID of the drawing
            
        Returns:
            dict: The drawing details
        """
        return self._call_api(
            access_token,
            DrawingsApi,
            "get_drawing_v3_projects_project_id_drawings_drawing_id_get",
            "DrawingsApi->get_drawing_v3_projects_project_id_drawings_drawing_id_get",
            project_id,
            drawing_id
        )
            
    def create_drawing(self, access_token, project_id, drawing_data):
        """Create a new drawing in a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            drawing_data (dict): The drawing configuration data
            
        Returns:
            dict: The created drawing details
        """
        return self._call_api(
            access_token,
            DrawingsApi,
            "create_drawing_v3_projects_project_id_drawings_post",
            "DrawingsApi->create_drawing_v3_projects_project_id_drawings_post",
            project_id,
            body=drawing_data
        )
            
    def update_drawing(self, access_token, project_id, drawing_id, drawing_data):
        """Update a drawing in a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            drawing_id (str): The ID of the drawing to update
            drawing_data (dict): The updated drawing configuration data
            
        Returns:
            dict: The updated drawing details
        """
        return self._call_api(
            access_token,
            DrawingsApi,
            "update_drawing_v3_projects_project_id_drawings_drawing_id_put",
            "DrawingsApi->update_drawing_v3_projects_project_id_drawings_drawing_id_put",
            project_id,
            drawing_id,
            body=drawing_data
        )
            
    def delete_drawing(self, access_token, project_id, drawing_id):
        """Delete a drawing from a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            drawing_id (str): The ID of the drawing to delete
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            DrawingsApi,
            "delete_drawing_v3_projects_project_id_drawings_drawing_id_delete",
            "DrawingsApi->delete_drawing_v3_projects_project_id_drawings_drawing_id_delete",
            project_id,
            drawing_id
        ) 