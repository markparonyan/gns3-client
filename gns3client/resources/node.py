from typing import Dict, Any, List
from gns3client.api.nodes import NodesAPI


class Node:
    """Represents a GNS3 node.
    
    This class provides methods for working with a GNS3 node.
    """
    
    def __init__(self, client, project_id: str, data: Dict[str, Any]):
        """Initialize a Node instance.
        
        Args:
            client: The GNS3Client instance
            project_id: The project ID this node belongs to
            data: The node data dictionary
        """
        self._client = client
        self._project_id = project_id
        self._data = data
        self._id = data.get('node_id')
    
    @property
    def id(self) -> str:
        """Get the node ID.
        
        Returns:
            str: The node ID
        """
        return self._id
    
    @property
    def name(self) -> str:
        """Get the node name.
        
        Returns:
            str: The node name
        """
        return self._data.get('name', '')
    
    @property
    def node_type(self) -> str:
        """Get the node type.
        
        Returns:
            str: The node type
        """
        return self._data.get('node_type', '')
    
    @property
    def compute_id(self) -> str:
        """Get the compute ID.
        
        Returns:
            str: The compute ID
        """
        return self._data.get('compute_id', 'local')
    
    @property
    def status(self) -> str:
        """Get the node status.
        
        Returns:
            str: The node status
        """
        return self._data.get('status', '')
    
    @property
    def console(self) -> int:
        """Get the console port.
        
        Returns:
            int: The console port
        """
        return self._data.get('console', 0)
    
    @property
    def console_host(self) -> str:
        """Get the console host.
        
        Returns:
            str: The console host
        """
        return self._data.get('console_host', '')
    
    def refresh(self) -> 'Node':
        """Refresh the node data from the server.
        
        Returns:
            Node: The updated node instance
        """
        nodes_api = NodesAPI(self._client.host)
        self._data = nodes_api.get(self._client.access_token, self._project_id, self.id)
        return self
    
    def update(self, **kwargs) -> 'Node':
        """Update the node properties.
        
        Args:
            **kwargs: Node attributes to update
            
        Returns:
            Node: The updated node instance
        """
        nodes_api = NodesAPI(self._client.host)
        self._data = nodes_api.update(self._client.access_token, self._project_id, self.id, **kwargs)
        return self
    
    def delete(self) -> None:
        """Delete the node."""
        nodes_api = NodesAPI(self._client.host)
        nodes_api.delete(self._client.access_token, self._project_id, self.id)
    
    def start(self) -> 'Node':
        """Start the node.
        
        Returns:
            Node: The updated node instance
        """
        nodes_api = NodesAPI(self._client.host)
        self._data = nodes_api.start(self._client.access_token, self._project_id, self.id)
        return self
    
    def stop(self) -> 'Node':
        """Stop the node.
        
        Returns:
            Node: The updated node instance
        """
        nodes_api = NodesAPI(self._client.host)
        self._data = nodes_api.stop(self._client.access_token, self._project_id, self.id)
        return self
    
    def suspend(self) -> 'Node':
        """Suspend the node.
        
        Returns:
            Node: The updated node instance
        """
        nodes_api = NodesAPI(self._client.host)
        self._data = nodes_api.suspend(self._client.access_token, self._project_id, self.id)
        return self
    
    def reload(self) -> 'Node':
        """Reload the node.
        
        Returns:
            Node: The updated node instance
        """
        nodes_api = NodesAPI(self._client.host)
        self._data = nodes_api.reload(self._client.access_token, self._project_id, self.id)
        return self
    
    def get_file(self, path: str) -> str:
        """Get the contents of a file from the node.
        
        Args:
            path: The path to the file
            
        Returns:
            str: The file contents
        """
        nodes_api = NodesAPI(self._client.host)
        return nodes_api.get_file(self._client.access_token, self._project_id, self.id, path)
    
    def write_file(self, path: str, data: str) -> None:
        """Write data to a file on the node.
        
        Args:
            path: The path to the file
            data: The data to write
        """
        nodes_api = NodesAPI(self._client.host)
        nodes_api.write_file(self._client.access_token, self._project_id, self.id, path, data)
    
    def __repr__(self) -> str:
        """String representation of the node.
        
        Returns:
            str: String representation
        """
        return f"<Node id={self.id} name={self.name} type={self.node_type} status={self.status}>" 