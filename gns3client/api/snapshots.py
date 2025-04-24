from gns3client.openapi_client.apis.tags.projects_api import ProjectsApi
from gns3client.api.base_api import BaseAPI


class SnapshotsAPI(BaseAPI):
    """API wrapper for GNS3 Snapshots API."""

    def list(self, access_token, project_id):
        """Get all snapshots for a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            
        Returns:
            list: The list of snapshots
        """
        return self._call_api(
            access_token,
            ProjectsApi,
            "get_snapshots_v3_projects_project_id_snapshots_get",
            "ProjectsApi->get_snapshots_v3_projects_project_id_snapshots_get",
            path_params={"project_id": project_id}
        )
            
            
    def create(self, access_token, project_id, name):
        """Create a new snapshot.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            name (str): The name of the snapshot
            
        Returns:
            dict: The created snapshot details
        """
        return self._call_api(
            access_token,
            ProjectsApi,
            "create_snapshot_v3_projects_project_id_snapshots_post",
            "ProjectsApi->create_snapshot_v3_projects_project_id_snapshots_post",
            path_params={"project_id": project_id},
            body={"name": name}
        )
            
    def delete(self, access_token, project_id, snapshot_id):
        """Delete a snapshot.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            snapshot_id (str): The ID of the snapshot to delete
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            ProjectsApi,
            "delete_snapshot_v3_projects_project_id_snapshots_snapshot_id_delete",
            "ProjectsApi->delete_snapshot_v3_projects_project_id_snapshots_snapshot_id_delete",
            path_params={"project_id": project_id, "snapshot_id": snapshot_id}
        )
            
    def restore(self, access_token, project_id, snapshot_id):
        """Restore a snapshot.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            snapshot_id (str): The ID of the snapshot to restore
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            ProjectsApi,
            "restore_snapshot_v3_projects_project_id_snapshots_snapshot_id_restore_post",
            "ProjectsApi->restore_snapshot_v3_projects_project_id_snapshots_snapshot_id_restore_post",
            path_params={"project_id": project_id, "snapshot_id": snapshot_id}
        ) 
