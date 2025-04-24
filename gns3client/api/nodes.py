from gns3client.openapi_client.apis.tags.nodes_api import NodesApi
from gns3client.api.base_api import BaseAPI


class NodesAPI(BaseAPI):
    """API wrapper for GNS3 Nodes API."""

    def list(self, access_token, project_id):
        """Get all nodes in a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            
        Returns:
            list: The list of nodes in the project
        """
        return self._call_api(
            access_token,
            NodesApi,
            "get_nodes_v3_projects_project_id_nodes_get",
            "NodesApi->get_nodes_v3_projects_project_id_nodes_get",
            path_params={"project_id": project_id}
        )
            
    def get(self, access_token, project_id, node_id):
        """Get a specific node in a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            node_id (str): The ID of the node
            
        Returns:
            dict: The node details
        """
        return self._call_api(
            access_token,
            NodesApi,
            "get_node_v3_projects_project_id_nodes_node_id_get",
            "NodesApi->get_node_v3_projects_project_id_nodes_node_id_get",
            path_params={"project_id": project_id, "node_id": node_id}
        )
            
    def create(self, access_token, project_id, node_data):
        """Create a new node in a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            node_data (dict): The node configuration data
            
        Returns:
            dict: The created node details
        """
        return self._call_api(
            access_token,
            NodesApi,
            "create_node_v3_projects_project_id_nodes_post",
            "NodesApi->create_node_v3_projects_project_id_nodes_post",
            path_params={"project_id": project_id},
            body=node_data
        )
            
    def update(self, access_token, project_id, node_id, node_data):
        """Update a node in a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            node_id (str): The ID of the node to update
            node_data (dict): The updated node configuration data
            
        Returns:
            dict: The updated node details
        """
        return self._call_api(
            access_token,
            NodesApi,
            "update_node_v3_projects_project_id_nodes_node_id_put",
            "NodesApi->update_node_v3_projects_project_id_nodes_node_id_put",
            path_params={"project_id": project_id, "node_id": node_id},
            body=node_data
        )
            
    def delete(self, access_token, project_id, node_id):
        """Delete a node from a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            node_id (str): The ID of the node to delete
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            NodesApi,
            "delete_node_v3_projects_project_id_nodes_node_id_delete",
            "NodesApi->delete_node_v3_projects_project_id_nodes_node_id_delete",
            path_params={"project_id": project_id, "node_id": node_id}
        )
            
    def start(self, access_token, project_id, node_id):
        """Start a node.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            node_id (str): The ID of the node to start
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            NodesApi,
            "start_node_v3_projects_project_id_nodes_node_id_start_post",
            "NodesApi->start_node_v3_projects_project_id_nodes_node_id_start_post",
            path_params={"project_id": project_id, "node_id": node_id}
        )
            
    def stop(self, access_token, project_id, node_id):
        """Stop a node.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            node_id (str): The ID of the node to stop
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            NodesApi,
            "stop_node_v3_projects_project_id_nodes_node_id_stop_post",
            "NodesApi->stop_node_v3_projects_project_id_nodes_node_id_stop_post",
            path_params={"project_id": project_id, "node_id": node_id}
        )
            
    def suspend(self, access_token, project_id, node_id):
        """Suspend a node.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            node_id (str): The ID of the node to suspend
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            NodesApi,
            "suspend_node_v3_projects_project_id_nodes_node_id_suspend_post",
            "NodesApi->suspend_node_v3_projects_project_id_nodes_node_id_suspend_post",
            path_params={"project_id": project_id, "node_id": node_id}
        )
            
    def reload(self, access_token, project_id, node_id):
        """Reload a node.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            node_id (str): The ID of the node to reload
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            NodesApi,
            "reload_node_v3_projects_project_id_nodes_node_id_reload_post",
            "NodesApi->reload_node_v3_projects_project_id_nodes_node_id_reload_post",
            path_params={"project_id": project_id, "node_id": node_id}
        )
            
    def duplicate(self, access_token, project_id, node_id, **kwargs):
        """Duplicate a node.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            node_id (str): The ID of the node to duplicate
            **kwargs: Additional parameters for the duplicated node
            
        Returns:
            dict: The duplicated node details
        """
        return self._call_api(
            access_token,
            NodesApi,
            "duplicate_node_v3_projects_project_id_nodes_node_id_duplicate_post",
            "NodesApi->duplicate_node_v3_projects_project_id_nodes_node_id_duplicate_post",
            path_params={"project_id": project_id, "node_id": node_id},
            body=kwargs
        )
            
    def start_all(self, access_token, project_id):
        """Start all nodes in a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            NodesApi,
            "start_all_nodes_v3_projects_project_id_nodes_start_post",
            "NodesApi->start_all_nodes_v3_projects_project_id_nodes_start_post",
            path_params={"project_id": project_id}
        )
            
    def stop_all(self, access_token, project_id):
        """Stop all nodes in a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            NodesApi,
            "stop_all_nodes_v3_projects_project_id_nodes_stop_post",
            "NodesApi->stop_all_nodes_v3_projects_project_id_nodes_stop_post",
            path_params={"project_id": project_id}
        )
            
    def suspend_all(self, access_token, project_id):
        """Suspend all nodes in a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            NodesApi,
            "suspend_all_nodes_v3_projects_project_id_nodes_suspend_post",
            "NodesApi->suspend_all_nodes_v3_projects_project_id_nodes_suspend_post",
            path_params={"project_id": project_id}
        )
            
    def reload_all(self, access_token, project_id):
        """Reload all nodes in a project.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            project_id (str): The ID of the project
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            NodesApi,
            "reload_all_nodes_v3_projects_project_id_nodes_reload_post",
            "NodesApi->reload_all_nodes_v3_projects_project_id_nodes_reload_post",
            path_params={"project_id": project_id}
        )
        
    def isolate(self, access_token, project_id, node_id):
        return self._call_api(
            access_token,
            NodesApi,
            "isolate_node_v3_projects_project_id_nodes_node_id_isolate_post",
            "NodesApi->isolate_node_v3_projects_project_id_nodes_node_id_isolate_post",
            path_params={"project_id": project_id, "node_id": node_id}
        )
        
    def unisolate(self, access_token, project_id, node_id):
        return self._call_api(
            access_token,
            NodesApi,
            "unisolate_node_v3_projects_project_id_nodes_node_id_unisolate_post",
            "NodesApi->unisolate_node_v3_projects_project_id_nodes_node_id_unisolate_post",
            path_params={"project_id": project_id, "node_id": node_id}
        )
        
    def links(self, access_token, project_id, node_id):
        return self._call_api(
            access_token,
            NodesApi,
            "get_node_links_v3_projects_project_id_nodes_node_id_links_get",
            "NodesApi->get_node_links_v3_projects_project_id_nodes_node_id_links_get",
            path_params={"project_id": project_id, "node_id": node_id}
        )
        
    def get_file(self, access_token, project_id, node_id, file_path):
        return self._call_api(
            access_token,
            NodesApi,
            "get_file_v3_projects_project_id_nodes_node_id_files_file_path_get",
            "NodesApi->get_file_v3_projects_project_id_nodes_node_id_files_file_path_get",
            path_params={"project_id": project_id, "node_id": node_id, "file_path": file_path}
        )
        
    def post_file(self, access_token, project_id, node_id, file_path, body):
        return self._call_api(
            access_token,
            NodesApi,
            "post_file_v3_projects_project_id_nodes_node_id_files_file_path_post",
            "NodesApi->post_file_v3_projects_project_id_nodes_node_id_files_file_path_post",
            path_params={"project_id": project_id, "node_id": node_id, "file_path": file_path},
            body=body
        )
        
    def reset_console_all(self, access_token, project_id):
        return self._call_api(
            access_token,
            NodesApi,
            "reset_console_all_nodes_v3_projects_project_id_nodes_console_reset_post",
            "NodesApi->reset_console_all_nodes_v3_projects_project_id_nodes_console_reset_post",
            path_params={"project_id": project_id}
        )
        
    def console_reset(self, access_token, project_id, node_id):
        return self._call_api(
            access_token,
            NodesApi,
            "console_reset_v3_projects_project_id_nodes_node_id_console_reset_post",
            "NodesApi->console_reset_v3_projects_project_id_nodes_node_id_console_reset_post",
            path_params={"project_id": project_id, "node_id": node_id}
        )
        
    def auto_idlepc(self, access_token, project_id, node_id):
        return self._call_api(
            access_token,
            NodesApi,
            "auto_idlepc_v3_projects_project_id_nodes_node_id_dynamips_auto_idlepc_get",
            "NodesApi->auto_idlepc_v3_projects_project_id_nodes_node_id_dynamips_auto_idlepc_get",
            path_params={"project_id": project_id, "node_id": node_id}
        )
        
    def idlepc_proposals(self, access_token, project_id, node_id):
        return self._call_api(
            access_token,
            NodesApi,
            "idlepc_proposals_v3_projects_project_id_nodes_node_id_dynamips_idlepc_proposals_get",
            "NodesApi->idlepc_proposals_v3_projects_project_id_nodes_node_id_dynamips_idlepc_proposals_get",
            path_params={"project_id": project_id, "node_id": node_id}
        )
        
    def create_disk_image(self, access_token, project_id, node_id, disk_name, body=None):
        return self._call_api(
            access_token,
            NodesApi,
            "create_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_post",
            "NodesApi->create_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_post",
            path_params={"project_id": project_id, "node_id": node_id, "disk_name": disk_name},
            body=body
        )
        
    def update_disk_image(self, access_token, project_id, node_id, disk_name, body):
        return self._call_api(
            access_token,
            NodesApi,
            "update_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_put",
            "NodesApi->update_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_put",
            path_params={"project_id": project_id, "node_id": node_id, "disk_name": disk_name},
            body=body
        )
        
    def delete_disk_image(self, access_token, project_id, node_id, disk_name):
        return self._call_api(
            access_token,
            NodesApi,
            "delete_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_delete",
            "NodesApi->delete_disk_image_v3_projects_project_id_nodes_node_id_qemu_disk_image_disk_name_delete",
            path_params={"project_id": project_id, "node_id": node_id, "disk_name": disk_name}
        ) 
