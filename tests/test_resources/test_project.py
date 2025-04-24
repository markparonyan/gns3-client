"""
Tests for the Project resource class.
"""
import pytest
from unittest.mock import MagicMock
from gns3client.resources.project import Project
from gns3client.api.projects import ProjectsAPI
from gns3client.api.nodes import NodesAPI
from gns3client.api.links import LinksAPI
from gns3client.api.drawings import DrawingsAPI
from gns3client.api.snapshots import SnapshotsAPI


class TestProject:
    """Tests for the Project class."""

    def test_properties(self, mock_client, project_data):
        """Test project properties."""
        project = Project(mock_client, project_data)
        
        assert project.id == "test-project-id"
        assert project.name == "Test Project"
        assert project.status == "opened"
        assert project.path == "/path/to/project"
    
    def test_refresh(self, mock_client, project_data):
        """Test refresh method."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        api_mock.get.return_value = {"project_id": "test-project-id", "name": "Updated Project"}
        
        result = project.refresh()
        
        mock_client._get_api.assert_called_once_with(ProjectsAPI)
        api_mock.get.assert_called_once_with("test-project-id")
        assert result is project
        assert project.name == "Updated Project"
    
    def test_open(self, mock_client, project_data):
        """Test open method."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        api_mock.get.return_value = {"project_id": "test-project-id", "status": "opened"}
        
        result = project.open()
        
        mock_client._get_api.assert_called_with(ProjectsAPI)
        api_mock.open.assert_called_once_with("test-project-id")
        assert result is project
        assert project.status == "opened"
    
    def test_close(self, mock_client, project_data):
        """Test close method."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        api_mock.get.return_value = {"project_id": "test-project-id", "status": "closed"}
        
        result = project.close()
        
        mock_client._get_api.assert_called_with(ProjectsAPI)
        api_mock.close.assert_called_once_with("test-project-id")
        assert result is project
        assert project.status == "closed"
    
    def test_delete(self, mock_client, project_data):
        """Test delete method."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        
        project.delete()
        
        mock_client._get_api.assert_called_once_with(ProjectsAPI)
        api_mock.delete.assert_called_once_with("test-project-id")
    
    def test_update(self, mock_client, project_data):
        """Test update method."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        api_mock.update.return_value = {"project_id": "test-project-id", "name": "Updated Project"}
        
        result = project.update(name="Updated Project")
        
        mock_client._get_api.assert_called_once_with(ProjectsAPI)
        api_mock.update.assert_called_once_with("test-project-id", name="Updated Project")
        assert result is project
        assert project.name == "Updated Project"
    
    def test_list_nodes(self, mock_client, project_data, node_data):
        """Test list_nodes method."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        api_mock.list.return_value = [node_data]
        
        result = project.list_nodes()
        
        mock_client._get_api.assert_called_with(NodesAPI)
        api_mock.list.assert_called_once_with("test-project-id")
        assert len(result) == 1
        assert result[0].id == "test-node-id"
        assert result[0].name == "Test Node"
    
    def test_get_node(self, mock_client, project_data, node_data):
        """Test get_node method."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        api_mock.get.return_value = node_data
        
        result = project.get_node("test-node-id")
        
        mock_client._get_api.assert_called_with(NodesAPI)
        api_mock.get.assert_called_once_with("test-project-id", "test-node-id")
        assert result.id == "test-node-id"
        assert result.name == "Test Node"
    
    def test_create_node(self, mock_client, project_data, node_data):
        """Test create_node method."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        api_mock.create.return_value = node_data
        
        result = project.create_node("Test Node", "vpcs")
        
        mock_client._get_api.assert_called_with(NodesAPI)
        api_mock.create.assert_called_once_with("test-project-id", {
            "name": "Test Node",
            "node_type": "vpcs",
            "compute_id": "local"
        })
        assert result.id == "test-node-id"
        assert result.name == "Test Node"
    
    def test_node_control_methods(self, mock_client, project_data):
        """Test node control methods (start_all, stop_all, etc.)."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        
        # Test all node control methods
        project.start_all()
        api_mock.start_all.assert_called_once_with("test-project-id")
        
        project.stop_all()
        api_mock.stop_all.assert_called_once_with("test-project-id")
        
        project.suspend_all()
        api_mock.suspend_all.assert_called_once_with("test-project-id")
        
        project.reload_all()
        api_mock.reload_all.assert_called_once_with("test-project-id")
        
        project.reset_console_all()
        api_mock.reset_console_all.assert_called_once_with("test-project-id")
    
    def test_delete_node(self, mock_client, project_data):
        """Test delete_node method."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        
        project.delete_node("test-node-id")
        
        mock_client._get_api.assert_called_with(NodesAPI)
        api_mock.delete.assert_called_once_with("test-project-id", "test-node-id")
    
    def test_list_links(self, mock_client, project_data, link_data):
        """Test list_links method."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        api_mock.list.return_value = [link_data]
        
        result = project.list_links()
        
        mock_client._get_api.assert_called_with(LinksAPI)
        api_mock.list.assert_called_once_with("test-project-id")
        assert len(result) == 1
        assert result[0].id == "test-link-id"
    
    def test_get_link(self, mock_client, project_data, link_data):
        """Test get_link method."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        api_mock.get.return_value = link_data
        
        result = project.get_link("test-link-id")
        
        mock_client._get_api.assert_called_with(LinksAPI)
        api_mock.get.assert_called_once_with("test-project-id", "test-link-id")
        assert result.id == "test-link-id"
    
    def test_create_link(self, mock_client, project_data, link_data):
        """Test create_link method."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        api_mock.create.return_value = link_data
        
        nodes = [
            {"node_id": "node1", "adapter_number": 0, "port_number": 0},
            {"node_id": "node2", "adapter_number": 0, "port_number": 0},
        ]
        
        result = project.create_link(nodes)
        
        mock_client._get_api.assert_called_with(LinksAPI)
        api_mock.create.assert_called_once_with("test-project-id", {"nodes": nodes})
        assert result.id == "test-link-id"
    
    def test_delete_link(self, mock_client, project_data):
        """Test delete_link method."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        
        project.delete_link("test-link-id")
        
        mock_client._get_api.assert_called_with(LinksAPI)
        api_mock.delete.assert_called_once_with("test-project-id", "test-link-id")
    
    def test_drawings_methods(self, mock_client, project_data):
        """Test drawing-related methods."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        drawing_data = {"drawing_id": "test-drawing-id", "svg": "<svg>...</svg>"}
        
        # Test list_drawings
        api_mock.list.return_value = [drawing_data]
        drawings = project.list_drawings()
        mock_client._get_api.assert_called_with(DrawingsAPI)
        api_mock.list.assert_called_with("test-project-id")
        assert len(drawings) == 1
        assert drawings[0]["drawing_id"] == "test-drawing-id"
        
        # Test get_drawing
        api_mock.get.return_value = drawing_data
        drawing = project.get_drawing("test-drawing-id")
        api_mock.get.assert_called_with("test-project-id", "test-drawing-id")
        assert drawing["drawing_id"] == "test-drawing-id"
    
    def test_delete_drawing(self, mock_client, project_data):
        """Test delete_drawing method."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        api_mock.delete.return_value = {"result": "success"}
        
        mock_client._get_api.return_value = api_mock
        result = project.delete_drawing("test-drawing-id")
        
        mock_client._get_api.assert_called_with(DrawingsAPI)
        api_mock.delete.assert_called_with("test-project-id", "test-drawing-id")
        assert result["result"] == "success"
    
    def test_snapshots_methods(self, mock_client, project_data):
        """Test snapshot-related methods."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        snapshot_data = {"snapshot_id": "test-snapshot-id", "name": "Test Snapshot"}
        
        # Test list_snapshots
        api_mock.list.return_value = [snapshot_data]
        snapshots = project.list_snapshots()
        mock_client._get_api.assert_called_with(SnapshotsAPI)
        api_mock.list.assert_called_with("test-project-id")
        assert len(snapshots) == 1
        assert snapshots[0]["snapshot_id"] == "test-snapshot-id"
        
        # Test get_snapshot
        api_mock.get.return_value = snapshot_data
        snapshot = project.get_snapshot("test-snapshot-id")
        api_mock.get.assert_called_with("test-project-id", "test-snapshot-id")
        assert snapshot["snapshot_id"] == "test-snapshot-id"
    
    def test_create_snapshot(self, mock_client, project_data):
        """Test create_snapshot method."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        snapshot_data = {"snapshot_id": "test-snapshot-id", "name": "Test Snapshot"}
        api_mock.create.return_value = snapshot_data
        
        # Make sure we get the SnapshotsAPI
        mock_client._get_api.return_value = api_mock
        
        result = project.create_snapshot("Test Snapshot")
        
        # Verify we got the right API
        mock_client._get_api.assert_called_with(SnapshotsAPI)
        # Verify the create call was made with correct parameters
        api_mock.create.assert_called_with("test-project-id", "Test Snapshot")
        # Verify the result contains the expected data
        assert result["snapshot_id"] == "test-snapshot-id"
        assert result["name"] == "Test Snapshot"
    
    def test_restore_snapshot(self, mock_client, project_data):
        """Test restore_snapshot method."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        api_mock.restore.return_value = {"result": "success"}
        
        result = project.restore_snapshot("test-snapshot-id")
        
        mock_client._get_api.assert_called_with(SnapshotsAPI)
        api_mock.restore.assert_called_with("test-project-id", "test-snapshot-id")
        assert result["result"] == "success"
    
    def test_delete_snapshot(self, mock_client, project_data):
        """Test delete_snapshot method."""
        project = Project(mock_client, project_data)
        api_mock = mock_client._get_api.return_value
        api_mock.delete.return_value = {"result": "success"}
        
        result = project.delete_snapshot("test-snapshot-id")
        
        mock_client._get_api.assert_called_with(SnapshotsAPI)
        api_mock.delete.assert_called_with("test-project-id", "test-snapshot-id")
        assert result["result"] == "success"
    
    def test_repr(self, mock_client, project_data):
        """Test __repr__ method."""
        project = Project(mock_client, project_data)
        
        representation = repr(project)
        
        assert "Project id=test-project-id" in representation
        assert "name=Test Project" in representation 