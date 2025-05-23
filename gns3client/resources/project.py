from typing import Dict, Any, List
from gns3client.api.projects import ProjectsAPI
from gns3client.api.nodes import NodesAPI
from gns3client.api.links import LinksAPI
from gns3client.api.drawings import DrawingsAPI
from gns3client.api.snapshots import SnapshotsAPI
from gns3client.api.templates import TemplatesAPI


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
        self._data = self._client._get_api(ProjectsAPI).get(self.id)
        return self
    
    def open(self) -> 'Project':
        """Open the project.
        
        Returns:
            Project: The updated project instance
        """
        self._client._get_api(ProjectsAPI).open(self.id)
        return self.refresh()
    
    def close(self) -> 'Project':
        """Close the project.
        
        Returns:
            Project: The updated project instance
        """
        self._client._get_api(ProjectsAPI).close(self.id)
        return self.refresh()
    
    def delete(self) -> None:
        """Delete the project."""
        self._client._get_api(ProjectsAPI).delete(self.id)
    
    def update(self, **kwargs) -> 'Project':
        """Update the project properties.
        
        Args:
            **kwargs: Project attributes to update
            
        Returns:
            Project: The updated project instance
        """
        self._data = self._client._get_api(ProjectsAPI).update(self.id, **kwargs)
        return self
    
    def list_nodes(self) -> List['Node']:
        """List all nodes in the project.
        
        Returns:
            List[Node]: List of Node objects
        """
        from gns3client.resources.node import Node
        
        nodes_data = self._client._get_api(NodesAPI).list(self.id)
        
        return [Node(self._client, self.id, node_data) for node_data in nodes_data]
    
    def get_node(self, node_id: str) -> 'Node':
        """Get a specific node in the project.
        
        Args:
            node_id: The ID of the node
            
        Returns:
            Node: The Node object
        """
        from gns3client.resources.node import Node
        
        node_data = self._client._get_api(NodesAPI).get(self.id, node_id)
        
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
        
        node_data = {
            "name": name,
            "node_type": node_type,
            "compute_id": compute_id
        }
        node_data.update(kwargs)
        
        node_data = self._client._get_api(NodesAPI).create(self.id, node_data)
        
        return Node(self._client, self.id, node_data)
    
    def start_all(self) -> None:
        """Start all nodes in the project."""
        self._client._get_api(NodesAPI).start_all(self.id)
        
    def stop_all(self) -> None:
        """Stop all nodes in the project."""
        self._client._get_api(NodesAPI).stop_all(self.id)
        
    def suspend_all(self) -> None:
        """Suspend all nodes in the project."""
        self._client._get_api(NodesAPI).suspend_all(self.id)
        
    def reload_all(self) -> None:
        """Reload all nodes in the project."""
        self._client._get_api(NodesAPI).reload_all(self.id)
        
    def reset_console_all(self) -> None:
        """Reset console for all nodes in the project."""
        self._client._get_api(NodesAPI).reset_console_all(self.id)
    
    def delete_node(self, node_id: str) -> None:
        """Delete a node from the project.
        
        Args:
            node_id: The ID of the node
        """
        self._client._get_api(NodesAPI).delete(self.id, node_id)
    
    def list_links(self) -> List['Link']:
        """List all links in the project.
        
        Returns:
            List[Link]: List of Link objects
        """
        from gns3client.resources.link import Link
        
        links_data = self._client._get_api(LinksAPI).list(self.id)
        
        return [Link(self._client, self.id, link_data) for link_data in links_data]
    
    def get_link(self, link_id: str) -> 'Link':
        """Get a specific link in the project.
        
        Args:
            link_id: The ID of the link
            
        Returns:
            Link: The Link object
        """
        from gns3client.resources.link import Link
        
        link_data = self._client._get_api(LinksAPI).get(self.id, link_id)
        
        return Link(self._client, self.id, link_data)
    
    def create_link(self, nodes: List[Dict[str, Any]]) -> 'Link':
        """Create a new link in the project.
        
        Args:
            nodes: List of node connection information
            
        Returns:
            Link: The created Link object
        """
        from gns3client.resources.link import Link
        
        link_data = {
            "nodes": nodes
        }
        
        link_data = self._client._get_api(LinksAPI).create(self.id, link_data)
        
        return Link(self._client, self.id, link_data)
    
    def delete_link(self, link_id: str) -> None:
        """Delete a link from the project.
        
        Args:
            link_id: The ID of the link
        """
        self._client._get_api(LinksAPI).delete(self.id, link_id)
    
    def list_drawings(self) -> List[Dict[str, Any]]:
        """List all drawings in the project.
        
        Returns:
            List[Dict[str, Any]]: List of drawing data dictionaries
        """
        return self._client._get_api(DrawingsAPI).list(self.id)
    
    def get_drawing(self, drawing_id: str) -> Dict[str, Any]:
        """Get a specific drawing in the project.
        
        Args:
            drawing_id: The ID of the drawing
            
        Returns:
            Dict[str, Any]: The drawing data dictionary
        """
        return self._client._get_api(DrawingsAPI).get(self.id, drawing_id)
    
    def create_drawing(self, drawing_data: Dict[str, Any]) -> Dict[str, Any]:
        """Create a new drawing in the project.
        
        Args:
            drawing_data: The drawing configuration data
            
        Returns:
            Dict[str, Any]: The created drawing data dictionary
        """
        return self._client._get_api(DrawingsAPI).create(self.id, drawing_data)
    
    def update_drawing(self, drawing_id: str, drawing_data: Dict[str, Any]) -> Dict[str, Any]:
        """Update a drawing in the project.
        
        Args:
            drawing_id: The ID of the drawing to update
            drawing_data: The drawing configuration data
            
        Returns:
            Dict[str, Any]: The updated drawing data dictionary
        """
        return self._client._get_api(DrawingsAPI).update(self.id, drawing_id, drawing_data)
    
    def delete_drawing(self, drawing_id: str) -> Dict[str, Any]:
        """Delete a drawing from the project.
        
        Args:
            drawing_id: The drawing ID
            
        Returns:
            Dict[str, Any]: The response data
        """
        return self._client._get_api(DrawingsAPI).delete(self.id, drawing_id)
    
    def list_snapshots(self) -> List['Snapshot']:
        """List all snapshots for the project.
        
        Returns:
            List[Snapshot]: List of Snapshot objects
        """
        from gns3client.resources.snapshot import Snapshot
        
        snapshots_data = self._client._get_api(SnapshotsAPI).list(self._client.access_token, self.id)
        
        return [Snapshot(self._client, self.id, snapshot_data) for snapshot_data in snapshots_data]
    
    def get_snapshot_by_id(self, snapshot_id: str) -> 'Snapshot':
        """Get a snapshot by its ID.
        
        Args:
            snapshot_id: The ID of the snapshot
            
        Returns:
            Snapshot: The Snapshot object, or None if not found
        """
        from gns3client.resources.snapshot import Snapshot
        
        snapshots_data = self._client._get_api(SnapshotsAPI).list(self._client.access_token, self.id)
        
        for snapshot_data in snapshots_data:
            if snapshot_data.get('snapshot_id') == snapshot_id:
                return Snapshot(self._client, self.id, snapshot_data)
        
        return None
    
    def get_snapshot_by_name(self, name: str) -> 'Snapshot':
        """Get a snapshot by its name.
        
        Args:
            name: The name of the snapshot
            
        Returns:
            Snapshot: The Snapshot object, or None if not found
        """
        from gns3client.resources.snapshot import Snapshot
        
        snapshots_data = self._client._get_api(SnapshotsAPI).list(self._client.access_token, self.id)
        
        for snapshot_data in snapshots_data:
            if snapshot_data.get('name') == name:
                return Snapshot(self._client, self.id, snapshot_data)
        
        return None
    
    def create_snapshot(self, name: str) -> 'Snapshot':
        """Create a new snapshot of the current project state.
        
        Args:
            name: The name of the snapshot
            
        Returns:
            Snapshot: The created Snapshot object
        """
        from gns3client.resources.snapshot import Snapshot
        
        snapshot_data = self._client._get_api(SnapshotsAPI).create(self._client.access_token, self.id, name)
        
        return Snapshot(self._client, self.id, snapshot_data)
    
    def restore_snapshot(self, snapshot_id: str) -> Dict[str, Any]:
        """Restore the project to a snapshot state.
        
        Args:
            snapshot_id: The ID of the snapshot to restore
            
        Returns:
            Dict[str, Any]: The response data
        """
        snapshot = self.get_snapshot_by_id(snapshot_id)
        if not snapshot:
            raise ValueError(f"No snapshot found with ID: {snapshot_id}")
        
        result = snapshot.restore()
        # Refresh project data after restore
        self.refresh()
        return result
    
    def delete_snapshot(self, snapshot_id: str) -> Dict[str, Any]:
        """Delete a snapshot.
        
        Args:
            snapshot_id: The ID of the snapshot to delete
            
        Returns:
            Dict[str, Any]: The response data
        """
        snapshot = self.get_snapshot_by_id(snapshot_id)
        if not snapshot:
            raise ValueError(f"No snapshot found with ID: {snapshot_id}")
        
        return snapshot.delete()
    
    def list_templates(self) -> List['Template']:
        """List all templates available on the server.
        
        Returns:
            List[Template]: List of Template objects
        """
        from gns3client.resources.template import Template
        
        templates_data = self._client._get_api(TemplatesAPI).list(self._client.access_token)
        
        return [Template(self._client, template_data) for template_data in templates_data]
    
    def get_template(self, template_id: str) -> 'Template':
        """Get a specific template.
        
        Args:
            template_id: The ID of the template
            
        Returns:
            Template: The Template object
        """
        from gns3client.resources.template import Template
        
        template_data = self._client._get_api(TemplatesAPI).get(self._client.access_token, template_id)
        
        return Template(self._client, template_data)
    
    def create_template(self, name: str, **kwargs) -> 'Template':
        """Create a new template.
        
        Args:
            name: The name of the template
            **kwargs: Additional template parameters
            
        Returns:
            Template: The created Template object
        """
        from gns3client.resources.template import Template
        
        template_data = self._client._get_api(TemplatesAPI).create(self._client.access_token, name, **kwargs)
        
        return Template(self._client, template_data)
    
    def delete_template(self, template_id: str) -> None:
        """Delete a template.
        
        Args:
            template_id: The ID of the template to delete
        """
        self._client._get_api(TemplatesAPI).delete(self._client.access_token, template_id)
    
    def __repr__(self) -> str:
        """String representation of the project.
        
        Returns:
            str: String representation
        """
        return f"<Project id={self.id} name={self.name}>"
