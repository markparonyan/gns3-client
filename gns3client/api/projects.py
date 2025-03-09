from gns3client.openapi_client.apis.tags.projects_api import ProjectsApi
from gns3client.api.base_api import BaseAPI



class ProjectsAPI(BaseAPI):
    """API wrapper for GNS3 Projects API."""

    def list(self, access_token):
        """Get all GNS3 projects.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            
        Returns:
            dict: The list of projects
        """
        return self._call_api(
            access_token,
            ProjectsApi,
            "get_projects_v3_projects_get",
            "ProjectsApi->get_projects_v3_projects_get"
        )

    def get(self, access_token, project_id):
        """Get a specific GNS3 project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project to retrieve
            
        Returns:
            dict: The project details
        """
        return self._call_api(
            access_token,
            ProjectsApi,
            "get_project_v3_projects_project_id_get",
            "ProjectsApi->get_project_v3_projects_project_id_get",
            path_params={"project_id": project_id}
        )
            
    def create(self, access_token, name, **kwargs):
        """Create a new GNS3 project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            name (str): The name of the project
            **kwargs: Additional project parameters
            
        Returns:
            dict: The created project details
        """
        # Prepare the project data
        project_data = {"name": name}
        project_data.update(kwargs)
        
        return self._call_api(
            access_token,
            ProjectsApi,
            "create_project_v3_projects_post",
            "ProjectsApi->create_project_v3_projects_post",
            body=project_data
        )
            
    def delete(self, access_token, project_id):
        """Delete a GNS3 project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project to delete
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            ProjectsApi,
            "delete_project_v3_projects_project_id_delete",
            "ProjectsApi->delete_project_v3_projects_project_id_delete",
            path_params={"project_id": project_id}
        )
            
    def update(self, access_token, project_id, **kwargs):
        """Update a GNS3 project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project to update
            **kwargs: Project attributes to update
            
        Returns:
            dict: The updated project details
        """
        return self._call_api(
            access_token,
            ProjectsApi,
            "update_project_v3_projects_project_id_put",
            "ProjectsApi->update_project_v3_projects_project_id_put",
            path_params={"project_id": project_id},
            body=kwargs
        )
            
    def open(self, access_token, project_id):
        """Open a GNS3 project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project to open
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            ProjectsApi,
            "open_project_v3_projects_project_id_open_post",
            "ProjectsApi->open_project_v3_projects_project_id_open_post",
            path_params={"project_id": project_id}
        )
            
    def close(self, access_token, project_id):
        """Close a GNS3 project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project to close
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            ProjectsApi,
            "close_project_v3_projects_project_id_close_post",
            "ProjectsApi->close_project_v3_projects_project_id_close_post",
            path_params={"project_id": project_id}
        )
            
    def duplicate(self, access_token, project_id, name=None):
        """Duplicate a GNS3 project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project to duplicate
            name (str, optional): The name for the duplicated project
            
        Returns:
            dict: The duplicated project details
        """
        body = {"name": name} if name else {}
        return self._call_api(
            access_token,
            ProjectsApi,
            "duplicate_project_v3_projects_project_id_duplicate_post",
            "ProjectsApi->duplicate_project_v3_projects_project_id_duplicate_post",
            path_params={"project_id": project_id},
            body=body
        )
            
    def export(self, access_token, project_id):
        """Export a GNS3 project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project to export
            
        Returns:
            bytes: The exported project file content
        """
        return self._call_api(
            access_token,
            ProjectsApi,
            "export_project_v3_projects_project_id_export_get",
            "ProjectsApi->export_project_v3_projects_project_id_export_get",
            path_params={"project_id": project_id}
        )
            
    def import_project(self, access_token, project_file, name=None):
        """Import a GNS3 project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_file (bytes): The project file content to import
            name (str, optional): The name for the imported project
            
        Returns:
            dict: The imported project details
        """
        body = {"project": project_file}
        if name:
            body["name"] = name
            
        return self._call_api(
            access_token,
            ProjectsApi,
            "import_project_v3_projects_import_post",
            "ProjectsApi->import_project_v3_projects_import_post",
            body=body
        )
            
    def stats(self, access_token, project_id):
        """Get statistics for a GNS3 project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            
        Returns:
            dict: The project statistics
        """
        return self._call_api(
            access_token,
            ProjectsApi,
            "get_project_stats_v3_projects_project_id_stats_get",
            "ProjectsApi->get_project_stats_v3_projects_project_id_stats_get",
            path_params={"project_id": project_id}
        )

