"""
Tests for the Node resource class.
"""
import pytest
from unittest.mock import MagicMock, patch
from gns3client.resources.node import Node
from gns3client.api.nodes import NodesAPI


class TestNode:
    """Tests for the Node class."""

    def test_properties(self, mock_client, node_data):
        """Test node properties."""
        node = Node(mock_client, "test-project-id", node_data)
        
        assert node.id == "test-node-id"
        assert node.name == "Test Node"
        assert node.node_type == "vpcs"
        assert node.compute_id == "local"
        assert node.status == "started"
        assert node.console == 5000
        assert node.console_host == "127.0.0.1"
    
    @patch('gns3client.resources.node.NodesAPI')
    def test_refresh(self, mock_nodes_api_class, mock_client, node_data):
        """Test refresh method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_nodes_api_class.return_value = mock_api_instance
        mock_api_instance.get.return_value = {"node_id": "test-node-id", "name": "Updated Node"}
        
        # Create the node and call refresh
        node = Node(mock_client, "test-project-id", node_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = node.refresh()
        
        # Verify the API call
        mock_nodes_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.get.assert_called_once_with("test-access-token", "test-project-id", "test-node-id")
        
        # Verify the result
        assert result is node
        assert node._data["name"] == "Updated Node"
    
    @patch('gns3client.resources.node.NodesAPI')
    def test_update(self, mock_nodes_api_class, mock_client, node_data):
        """Test update method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_nodes_api_class.return_value = mock_api_instance
        mock_api_instance.update.return_value = {"node_id": "test-node-id", "name": "Updated Node"}
        
        # Create the node and call update
        node = Node(mock_client, "test-project-id", node_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = node.update(name="Updated Node")
        
        # Verify the API call
        mock_nodes_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.update.assert_called_once_with(
            "test-access-token", "test-project-id", "test-node-id", name="Updated Node"
        )
        
        # Verify the result
        assert result is node
        assert node._data["name"] == "Updated Node"
    
    @patch('gns3client.resources.node.NodesAPI')
    def test_delete(self, mock_nodes_api_class, mock_client, node_data):
        """Test delete method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_nodes_api_class.return_value = mock_api_instance
        
        # Create the node and call delete
        node = Node(mock_client, "test-project-id", node_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        node.delete()
        
        # Verify the API call
        mock_nodes_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.delete.assert_called_once_with("test-access-token", "test-project-id", "test-node-id")
    
    @patch('gns3client.resources.node.NodesAPI')
    def test_start(self, mock_nodes_api_class, mock_client, node_data):
        """Test start method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_nodes_api_class.return_value = mock_api_instance
        mock_api_instance.start.return_value = {"node_id": "test-node-id", "status": "started"}
        
        # Create the node and call start
        node = Node(mock_client, "test-project-id", node_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = node.start()
        
        # Verify the API call
        mock_nodes_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.start.assert_called_once_with("test-access-token", "test-project-id", "test-node-id")
        
        # Verify the result
        assert result is node
        assert node._data["status"] == "started"
    
    @patch('gns3client.resources.node.NodesAPI')
    def test_stop(self, mock_nodes_api_class, mock_client, node_data):
        """Test stop method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_nodes_api_class.return_value = mock_api_instance
        mock_api_instance.stop.return_value = {"node_id": "test-node-id", "status": "stopped"}
        
        # Create the node and call stop
        node = Node(mock_client, "test-project-id", node_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = node.stop()
        
        # Verify the API call
        mock_nodes_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.stop.assert_called_once_with("test-access-token", "test-project-id", "test-node-id")
        
        # Verify the result
        assert result is node
        assert node._data["status"] == "stopped"
    
    @patch('gns3client.resources.node.NodesAPI')
    def test_suspend(self, mock_nodes_api_class, mock_client, node_data):
        """Test suspend method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_nodes_api_class.return_value = mock_api_instance
        mock_api_instance.suspend.return_value = {"node_id": "test-node-id", "status": "suspended"}
        
        # Create the node and call suspend
        node = Node(mock_client, "test-project-id", node_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = node.suspend()
        
        # Verify the API call
        mock_nodes_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.suspend.assert_called_once_with("test-access-token", "test-project-id", "test-node-id")
        
        # Verify the result
        assert result is node
        assert node._data["status"] == "suspended"
    
    @patch('gns3client.resources.node.NodesAPI')
    def test_reload(self, mock_nodes_api_class, mock_client, node_data):
        """Test reload method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_nodes_api_class.return_value = mock_api_instance
        mock_api_instance.reload.return_value = {"node_id": "test-node-id", "status": "started"}
        
        # Create the node and call reload
        node = Node(mock_client, "test-project-id", node_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = node.reload()
        
        # Verify the API call
        mock_nodes_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.reload.assert_called_once_with("test-access-token", "test-project-id", "test-node-id")
        
        # Verify the result
        assert result is node
        assert node._data["status"] == "started"
    
    @patch('gns3client.resources.node.NodesAPI')
    def test_get_file(self, mock_nodes_api_class, mock_client, node_data):
        """Test get_file method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_nodes_api_class.return_value = mock_api_instance
        mock_api_instance.get_file.return_value = "file content"
        
        # Create the node and call get_file
        node = Node(mock_client, "test-project-id", node_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = node.get_file("/path/to/file")
        
        # Verify the API call
        mock_nodes_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.get_file.assert_called_once_with(
            "test-access-token", "test-project-id", "test-node-id", "/path/to/file"
        )
        
        # Verify the result
        assert result == "file content"
    
    @patch('gns3client.resources.node.NodesAPI')
    def test_post_file(self, mock_nodes_api_class, mock_client, node_data):
        """Test post_file method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_nodes_api_class.return_value = mock_api_instance
        
        # Create the node and call post_file
        node = Node(mock_client, "test-project-id", node_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        node.post_file("/path/to/file", "file content")
        
        # Verify the API call
        mock_nodes_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.post_file.assert_called_once_with(
            "test-access-token", "test-project-id", "test-node-id", "/path/to/file", "file content"
        )
    
    @patch('gns3client.resources.node.NodesAPI')
    def test_console_reset(self, mock_nodes_api_class, mock_client, node_data):
        """Test console_reset method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_nodes_api_class.return_value = mock_api_instance
        mock_api_instance.console_reset.return_value = {"node_id": "test-node-id", "console": 5001}
        
        # Create the node and call console_reset
        node = Node(mock_client, "test-project-id", node_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = node.console_reset()
        
        # Verify the API call
        mock_nodes_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.console_reset.assert_called_once_with("test-access-token", "test-project-id", "test-node-id")
        
        # Verify the result
        assert result is node
        assert node._data["console"] == 5001

    @patch('gns3client.resources.node.NodesAPI')
    def test_duplicate(self, mock_nodes_api_class, mock_client, node_data):
        """Test duplicate method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_nodes_api_class.return_value = mock_api_instance
        duplicated_node_data = node_data.copy()
        duplicated_node_data["node_id"] = "duplicated-node-id"
        mock_api_instance.duplicate.return_value = duplicated_node_data
        
        # Create the node and call duplicate
        node = Node(mock_client, "test-project-id", node_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = node.duplicate()
        
        # Verify the API call
        mock_nodes_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.duplicate.assert_called_once_with(
            "test-access-token", "test-project-id", "test-node-id"
        )
        
        # Verify the result
        assert result.id == "duplicated-node-id"
        assert result.name == "Test Node"
        assert result.node_type == "vpcs"

    @patch('gns3client.resources.node.NodesAPI')
    def test_isolate(self, mock_nodes_api_class, mock_client, node_data):
        """Test isolate method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_nodes_api_class.return_value = mock_api_instance
        isolated_node_data = node_data.copy()
        isolated_node_data["status"] = "isolated"
        mock_api_instance.isolate.return_value = isolated_node_data
        
        # Create the node and call isolate
        node = Node(mock_client, "test-project-id", node_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = node.isolate()
        
        # Verify the API call
        mock_nodes_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.isolate.assert_called_once_with(
            "test-access-token", "test-project-id", "test-node-id"
        )
        
        # Verify the result
        assert result is node
        assert node._data["status"] == "isolated"

    @patch('gns3client.resources.node.NodesAPI')
    def test_unisolate(self, mock_nodes_api_class, mock_client, node_data):
        """Test unisolate method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_nodes_api_class.return_value = mock_api_instance
        # First make the node isolated
        isolated_node_data = node_data.copy()
        isolated_node_data["status"] = "isolated"
        node = Node(mock_client, "test-project-id", isolated_node_data)
        
        # Setup the mock return value
        unisolated_node_data = node_data.copy()  # restore original status
        mock_api_instance.unisolate.return_value = unisolated_node_data
        
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = node.unisolate()
        
        # Verify the API call
        mock_nodes_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.unisolate.assert_called_once_with(
            "test-access-token", "test-project-id", "test-node-id"
        )
        
        # Verify the result
        assert result is node
        assert node._data["status"] == "started"

    @patch('gns3client.resources.node.NodesAPI')
    def test_links(self, mock_nodes_api_class, mock_client, node_data):
        """Test links method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_nodes_api_class.return_value = mock_api_instance
        links_data = [
            {"link_id": "link1", "nodes": [{"node_id": "test-node-id"}, {"node_id": "other-node"}]},
            {"link_id": "link2", "nodes": [{"node_id": "test-node-id"}, {"node_id": "another-node"}]}
        ]
        mock_api_instance.links.return_value = links_data
        
        # Create the node and call links
        node = Node(mock_client, "test-project-id", node_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = node.links()
        
        # Verify the API call
        mock_nodes_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.links.assert_called_once_with(
            "test-access-token", "test-project-id", "test-node-id"
        )
        
        # Verify the result
        assert result == links_data
        assert len(result) == 2
        assert result[0]["link_id"] == "link1"
        assert result[1]["link_id"] == "link2"

    @patch('gns3client.resources.node.NodesAPI')
    def test_auto_idlepc(self, mock_nodes_api_class, mock_client, node_data):
        """Test auto_idlepc method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_nodes_api_class.return_value = mock_api_instance
        idlepc_data = {"idlepc": "0x12345678"}
        mock_api_instance.auto_idlepc.return_value = idlepc_data
        
        # Create the node and call auto_idlepc
        node = Node(mock_client, "test-project-id", node_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = node.auto_idlepc()
        
        # Verify the API call
        mock_nodes_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.auto_idlepc.assert_called_once_with(
            "test-access-token", "test-project-id", "test-node-id"
        )
        
        # Verify the result
        assert result == idlepc_data
        assert result["idlepc"] == "0x12345678"

    @patch('gns3client.resources.node.NodesAPI')
    def test_idlepc_proposals(self, mock_nodes_api_class, mock_client, node_data):
        """Test idlepc_proposals method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_nodes_api_class.return_value = mock_api_instance
        proposals = ["0x12345678", "0x87654321", "0x11111111"]
        mock_api_instance.idlepc_proposals.return_value = proposals
        
        # Create the node and call idlepc_proposals
        node = Node(mock_client, "test-project-id", node_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = node.idlepc_proposals()
        
        # Verify the API call
        mock_nodes_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.idlepc_proposals.assert_called_once_with(
            "test-access-token", "test-project-id", "test-node-id"
        )
        
        # Verify the result
        assert result == proposals
        assert len(result) == 3
        assert "0x12345678" in result

    @patch('gns3client.resources.node.NodesAPI')
    def test_create_disk_image(self, mock_nodes_api_class, mock_client, node_data):
        """Test create_disk_image method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_nodes_api_class.return_value = mock_api_instance
        disk_image_data = {"path": "/path/to/disk.qcow2", "created": True}
        mock_api_instance.create_disk_image.return_value = disk_image_data
        
        # Create the node and call create_disk_image
        node = Node(mock_client, "test-project-id", node_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = node.create_disk_image("/path/to/disk.qcow2", disk_type="qcow2")
        
        # Verify the API call
        mock_nodes_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.create_disk_image.assert_called_once_with(
            "test-access-token", "test-project-id", "test-node-id", "/path/to/disk.qcow2", disk_type="qcow2"
        )
        
        # Verify the result
        assert result == disk_image_data
        assert result["path"] == "/path/to/disk.qcow2"
        assert result["created"] is True

    @patch('gns3client.resources.node.NodesAPI')
    def test_delete_disk_image(self, mock_nodes_api_class, mock_client, node_data):
        """Test delete_disk_image method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_nodes_api_class.return_value = mock_api_instance
        
        # Create the node and call delete_disk_image
        node = Node(mock_client, "test-project-id", node_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = node.delete_disk_image("/path/to/disk.qcow2")
        
        mock_nodes_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.delete_disk_image.assert_called_once_with(
            "test-access-token", "test-project-id", "test-node-id", "/path/to/disk.qcow2"
        )
        
        assert result is None

    def test_repr(self, mock_client, node_data):
        """Test __repr__ method."""
        node = Node(mock_client, "test-project-id", node_data)
        
        representation = repr(node)
        
        # Verify the representation string
        assert "Node id=test-node-id" in representation
        assert "name=Test Node" in representation
        assert "type=vpcs" in representation
        assert "status=started" in representation 