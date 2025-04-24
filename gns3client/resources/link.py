from typing import Dict, Any, List
from gns3client.api.links import LinksAPI


class Link:
    """Represents a GNS3 link between nodes.
    
    This class provides methods for working with a GNS3 link.
    """
    
    def __init__(self, client, project_id: str, data: Dict[str, Any]):
        """Initialize a Link instance.
        
        Args:
            client: The GNS3Client instance
            project_id: The project ID this link belongs to
            data: The link data dictionary
        """
        self._client = client
        self._project_id = project_id
        self._data = data
        self._id = data.get('link_id')
    
    @property
    def id(self) -> str:
        """Get the link ID.
        
        Returns:
            str: The link ID
        """
        return self._id
    
    @property
    def nodes(self) -> List[Dict[str, Any]]:
        """Get the nodes connected by this link.
        
        Returns:
            List[Dict[str, Any]]: List of node connection information
        """
        return self._data.get('nodes', [])
    
    @property
    def capturing(self) -> bool:
        """Check if packet capturing is enabled on this link.
        
        Returns:
            bool: True if packet capturing is enabled
        """
        return self._data.get('capturing', False)
    
    @property
    def capture_file_path(self) -> str:
        """Get the path to the packet capture file.
        
        Returns:
            str: The path to the packet capture file
        """
        return self._data.get('capture_file_path', '')
    
    @property
    def capture_file_name(self) -> str:
        """Get the name of the packet capture file.
        
        Returns:
            str: The name of the packet capture file
        """
        return self._data.get('capture_file_name', '')
    
    def refresh(self) -> 'Link':
        """Refresh the link data from the server.
        
        Returns:
            Link: The updated link instance
        """
        self._data = self._client._get_api(LinksAPI).get(self._project_id, self.id)
        return self
    
    def update(self, **kwargs) -> 'Link':
        """Update the link properties.
        
        Args:
            **kwargs: Link attributes to update
            
        Returns:
            Link: The updated link instance
        """
        self._data = self._client._get_api(LinksAPI).update(self._project_id, self.id, kwargs)
        return self
    
    def reset(self) -> 'Link':
        """Reset the link.
        
        Returns:
            Link: The updated link instance
        """
        self._data = self._client._get_api(LinksAPI).reset(self._project_id, self.id)
        return self
    
    def start_capture(self, capture_file_name: str = None, data_link_type: str = "DLT_EN10MB") -> 'Link':
        """Start packet capturing on the link.
        
        Args:
            capture_file_name: Optional name for the capture file
            data_link_type: The data link type (default: DLT_EN10MB)
            
        Returns:
            Link: The updated link instance
        """
        capture_data = {
            "data_link_type": data_link_type
        }
        
        if capture_file_name:
            capture_data["capture_file_name"] = capture_file_name
            
        self._data = self._client._get_api(LinksAPI).start_capture(self._project_id, self.id, capture_data)
        return self
    
    def stop_capture(self) -> 'Link':
        """Stop packet capturing on the link.
        
        Returns:
            Link: The updated link instance
        """
        self._data = self._client._get_api(LinksAPI).stop_capture(self._project_id, self.id)
        return self
    
    def get_capture_stream(self) -> bytes:
        """Get the packet capture stream.
        
        Returns:
            bytes: The packet capture stream data
        """
        return self._client._get_api(LinksAPI).get_capture_stream(self._project_id, self.id)
    
    def get_available_filters(self) -> List[str]:
        """Get available packet filters for the link.
        
        Returns:
            List[str]: List of available packet filters
        """
        return self._client._get_api(LinksAPI).get_available_filters(self._project_id, self.id)
    
    def __repr__(self) -> str:
        """String representation of the link.
        
        Returns:
            str: String representation
        """
        node_info = ""
        if len(self.nodes) >= 2:
            node_info = f"{self.nodes[0].get('node_id', '')} -> {self.nodes[1].get('node_id', '')}"
        
        return f"<Link id={self.id} nodes={node_info} capturing={self.capturing}>" 