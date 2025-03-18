from typing import Dict, Any, List
from gns3client.api.projects import ProjectsAPI
from gns3client.api.nodes import NodesAPI
from gns3client.api.links import LinksAPI
from gns3client.api.drawings import DrawingsAPI
from gns3client.api.snapshots import SnapshotsAPI


class Project:
    """Represents a GNS3 project.
    
    This class provides methods for working with a GNS3 project and its resources.
    """
    
    def __init__(self, client, data: dict[str, Any] = None):
        """Initialize a Project instance.
        
        Args:
            client: The GNS3Client instance
            data: The project data dictionary
        """
        self._client = client
        self._data = data
        self._id = data.get('project_id')
    # TODO: checkout this properites
    @property
    def id(self) -> str:
        """Get the project ID.
        
        Returns:
            str: The project ID
        """
        return self._id
    
    @property
    def name(self) -> str:
        """Get the project name.
        
        Returns:
            str: The project name
        """
        return self._data.get('name', '')
    
    @property
    def status(self) -> str:
        """Get the project status.
        
        Returns:
            str: The project status
        """
        return self._data.get('status', '')
    
    @property
    def path(self) -> str:
        """Get the project file path.
        
        Returns:
            str: The project file path
        """
        return self._data.get('path', '')
    
    def refresh(self) -> 'Project':
        """Refresh the project data from the server.
        
        Returns:
            Project: The updated project instance
        """
        projects_api = ProjectsAPI(self._client.host)
        self._data = projects_api.get(self._client.access_token, self.id)
        return self
    
    def open(self) -> 'Project':
        """Open the project.
        
        Returns:
            Project: The updated project instance
        """
        projects_api = ProjectsAPI(self._client.host)
        projects_api.open(self._client.access_token, self.id)
        return self.refresh()
    
    def close(self) -> 'Project':
        """Close the project.
        
        Returns:
            Project: The updated project instance
        """
        projects_api = ProjectsAPI(self._client.host)
        projects_api.close(self._client.access_token, self.id)
        return self.refresh()
    
    def delete(self) -> None:
        """Delete the project."""
        projects_api = ProjectsAPI(self._client.host)
        projects_api.delete(self._client.access_token, self.id)
    
    def update(self, **kwargs) -> 'Project':
        """Update the project properties.
        
        Args:
            **kwargs: Project attributes to update
            
        Returns:
            Project: The updated project instance
        """
        projects_api = ProjectsAPI(self._client.host)
        self._data = projects_api.update(self._client.access_token, self.id, **kwargs)
        return self
    
    def list_nodes(self) -> List['Node']:
        """List all nodes in the project.
        
        Returns:
            List[Node]: List of Node objects
        """
        from gns3client.resources.node import Node
        
        nodes_api = NodesAPI(self._client.host)
        nodes_data = nodes_api.list(self._client.access_token, self.id)
        
        return [Node(self._client, self.id, node_data) for node_data in nodes_data]
    
    def get_node(self, node_id: str) -> 'Node':
        """Get a specific node in the project.
        
        Args:
            node_id: The ID of the node
            
        Returns:
            Node: The Node object
        """
        from gns3client.resources.node import Node
        
        nodes_api = NodesAPI(self._client.host)
        node_data = nodes_api.get(self._client.access_token, self.id, node_id)
        
        return Node(self._client, self.id, node_data)
    
    def create_node(self, name: str, node_type: str, compute_id: str = "local", **kwargs) -> 'Node':
        """Create a new node in the project.
        
        Args:
            name: The name of the node
            node_type: The type of the node
            compute_id: The compute ID (default: "local")
            **kwargs: Additional node parameters
            
        Returns:
            Node: The created Node object
        """
        from gns3client.resources.node import Node
        
        nodes_api = NodesAPI(self._client.host)
        
        node_data = {
            "name": name,
            "node_type": node_type,
            "compute_id": compute_id
        }
        node_data.update(kwargs)
        
        node_data = nodes_api.create(self._client.access_token, self.id, node_data)
        
        return Node(self._client, self.id, node_data)
    
    def update_node(self, node_id: str, **kwargs) -> 'Node':
        """Update a node in the project.
        
        Args:
            node_id: The ID of the node
            **kwargs: Node attributes to update
            
        Returns:
            Node: The updated Node object
        """
        from gns3client.resources.node import Node
        
        nodes_api = NodesAPI(self._client.host)
        node_data = nodes_api.update(self._client.access_token, self.id, node_id, **kwargs)
        
        return Node(self._client, self.id, node_data)
    
    def delete_node(self, node_id: str) -> None:
        """Delete a node from the project.
        
        Args:
            node_id: The ID of the node
        """
        nodes_api = NodesAPI(self._client.host)
        nodes_api.delete(self._client.access_token, self.id, node_id)
    
    def start_node(self, node_id: str) -> 'Node':
        """Start a node in the project.
        
        Args:
            node_id: The ID of the node
            
        Returns:
            Node: The updated Node object
        """
        from gns3client.resources.node import Node
        
        nodes_api = NodesAPI(self._client.host)
        node_data = nodes_api.start(self._client.access_token, self.id, node_id)
        
        return Node(self._client, self.id, node_data)
    
    def stop_node(self, node_id: str) -> 'Node':
        """Stop a node in the project.
        
        Args:
            node_id: The ID of the node
            
        Returns:
            Node: The updated Node object
        """
        from gns3client.resources.node import Node
        
        nodes_api = NodesAPI(self._client.host)
        node_data = nodes_api.stop(self._client.access_token, self.id, node_id)
        
        return Node(self._client, self.id, node_data)
    
    def suspend_node(self, node_id: str) -> 'Node':
        """Suspend a node in the project.
        
        Args:
            node_id: The ID of the node
            
        Returns:
            Node: The updated Node object
        """
        from gns3client.resources.node import Node
        
        nodes_api = NodesAPI(self._client.host)
        node_data = nodes_api.suspend(self._client.access_token, self.id, node_id)
        
        return Node(self._client, self.id, node_data)
    
    def reload_node(self, node_id: str) -> 'Node':
        """Reload a node in the project.
        
        Args:
            node_id: The ID of the node
            
        Returns:
            Node: The updated Node object
        """
        from gns3client.resources.node import Node
        
        nodes_api = NodesAPI(self._client.host)
        node_data = nodes_api.reload(self._client.access_token, self.id, node_id)
        
        return Node(self._client, self.id, node_data)
    
    def list_links(self) -> List['Link']:
        """List all links in the project.
        
        Returns:
            List[Link]: List of Link objects
        """
        from gns3client.resources.link import Link
        
        links_api = LinksAPI(self._client.host)
        links_data = links_api.list(self._client.access_token, self.id)
        
        return [Link(self._client, self.id, link_data) for link_data in links_data]
    
    def get_link(self, link_id: str) -> 'Link':
        """Get a specific link in the project.
        
        Args:
            link_id: The ID of the link
            
        Returns:
            Link: The Link object
        """
        from gns3client.resources.link import Link
        
        links_api = LinksAPI(self._client.host)
        link_data = links_api.get(self._client.access_token, self.id, link_id)
        
        return Link(self._client, self.id, link_data)
    
    def create_link(self, nodes: List[Dict[str, Any]]) -> 'Link':
        """Create a new link in the project.
        
        Args:
            nodes: List of node connection information
            
        Returns:
            Link: The created Link object
        """
        from gns3client.resources.link import Link
        
        links_api = LinksAPI(self._client.host)
        
        link_data = {
            "nodes": nodes
        }
        
        link_data = links_api.create(self._client.access_token, self.id, link_data)
        
        return Link(self._client, self.id, link_data)
    
    def delete_link(self, link_id: str) -> None:
        """Delete a link from the project.
        
        Args:
            link_id: The ID of the link
        """
        links_api = LinksAPI(self._client.host)
        links_api.delete(self._client.access_token, self.id, link_id)
    
    def list_drawings(self) -> List[Dict[str, Any]]:
        """List all drawings in the project.
        
        Returns:
            List[Dict[str, Any]]: List of drawing data dictionaries
        """
        drawings_api = DrawingsAPI(self._client.host)
        return drawings_api.list(self._client.access_token, self.id)
    
    def get_drawing(self, drawing_id: str) -> Dict[str, Any]:
        """Get a specific drawing in the project.
        
        Args:
            drawing_id: The ID of the drawing
            
        Returns:
            Dict[str, Any]: The drawing data dictionary
        """
        drawings_api = DrawingsAPI(self._client.host)
        return drawings_api.get(self._client.access_token, self.id, drawing_id)
    
    def create_drawing(self, drawing_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new drawing in the project.
        
        Args:
            drawing_data: The drawing configuration data
            
        Returns:
            Dict[str, Any]: The created drawing data dictionary
        """
        drawings_api = DrawingsAPI(self._client.host)
        return drawings_api.create(self._client.access_token, self.id, drawing_data)
    
    def update_drawing(self, drawing_id: str, drawing_data: Dict[str, Any]) -> Dict[str, Any]:
        """Update a drawing in the project.
        
        Args:
            drawing_id: The ID of the drawing to update
            drawing_data: The drawing configuration data
            
        Returns:
            Dict[str, Any]: The updated drawing data dictionary
        """
        drawings_api = DrawingsAPI(self._client.host)
        return drawings_api.update(self._client.access_token, self.id, drawing_id, drawing_data)
    
    def delete_drawing(self, drawing_id: str) -> Dict[str, Any]:
        """Delete a drawing from the project.
        
        Args:
            drawing_id: The drawing ID
            
        Returns:
            Dict[str, Any]: The response data
        """
        drawings_api = DrawingsAPI(self._client.host)
        return drawings_api.delete(self._client.access_token, self.id, drawing_id)
    
    def list_snapshots(self) -> List[Dict[str, Any]]:
        """List all snapshots for the project.
        
        Returns:
            List[Dict[str, Any]]: List of snapshot data dictionaries
        """
        snapshots_api = SnapshotsAPI(self._client.host)
        return snapshots_api.list(self._client.access_token, self.id)
    
    def get_snapshot(self, snapshot_id: str) -> Dict[str, Any]:
        """Get a specific snapshot.
        
        Args:
            snapshot_id: The ID of the snapshot
            
        Returns:
            Dict[str, Any]: The snapshot data dictionary
        """
        snapshots_api = SnapshotsAPI(self._client.host)
        return snapshots_api.get(self._client.access_token, self.id, snapshot_id)
    
    def create_snapshot(self, name: str) -> Dict[str, Any]:
        """Create a new snapshot.
        
        Args:
            name: The name of the snapshot
            
        Returns:
            Dict[str, Any]: The created snapshot data dictionary
        """
        snapshots_api = SnapshotsAPI(self._client.host)
        return snapshots_api.create(self._client.access_token, self.id, name)
    
    def restore_snapshot(self, snapshot_id: str) -> Dict[str, Any]:
        """Restore a snapshot.
        
        Args:
            snapshot_id: The ID of the snapshot to restore
            
        Returns:
            Dict[str, Any]: The response data
        """
        snapshots_api = SnapshotsAPI(self._client.host)
        return snapshots_api.restore(self._client.access_token, self.id, snapshot_id)
    
    def delete_snapshot(self, snapshot_id: str) -> Dict[str, Any]:
        """Delete a snapshot.
        
        Args:
            snapshot_id: The ID of the snapshot to delete
            
        Returns:
            Dict[str, Any]: The response data
        """
        snapshots_api = SnapshotsAPI(self._client.host)
        return snapshots_api.delete(self._client.access_token, self.id, snapshot_id)
    
    def __repr__(self) -> str:
        """String representation of the project.
        
        Returns:
            str: String representation
        """
        return f"<Project id={self.id} name={self.name}>" 
