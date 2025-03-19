"""
Tests for the Link resource class.
"""
import pytest
from unittest.mock import MagicMock
from gns3client.resources.link import Link
from gns3client.api.links import LinksAPI


class TestLink:
    """Tests for the Link class."""

    def test_properties(self, mock_client, link_data):
        """Test link properties."""
        link = Link(mock_client, "test-project-id", link_data)
        
        assert link.id == "test-link-id"
        assert len(link.nodes) == 2
        assert link.nodes[0]["node_id"] == "node1"
        assert link.nodes[1]["node_id"] == "node2"
        assert not link.capturing
        assert link.capture_file_path == ""
        assert link.capture_file_name == ""
    
    def test_refresh(self, mock_client, link_data):
        """Test refresh method."""
        link = Link(mock_client, "test-project-id", link_data)
        api_mock = mock_client._get_api.return_value
        api_mock.get.return_value = {
            "link_id": "test-link-id",
            "nodes": link_data["nodes"],
            "capturing": True
        }
        
        result = link.refresh()
        
        mock_client._get_api.assert_called_once_with(LinksAPI)
        api_mock.get.assert_called_once_with("test-project-id", "test-link-id")
        assert result is link
        assert link.capturing is True
    
    def test_delete(self, mock_client, link_data):
        """Test delete method."""
        link = Link(mock_client, "test-project-id", link_data)
        api_mock = mock_client._get_api.return_value
        
        link.delete()
        
        mock_client._get_api.assert_called_once_with(LinksAPI)
        api_mock.delete.assert_called_once_with("test-project-id", "test-link-id")
    
    def test_update(self, mock_client, link_data):
        """Test update method."""
        link = Link(mock_client, "test-project-id", link_data)
        api_mock = mock_client._get_api.return_value
        api_mock.update.return_value = {
            "link_id": "test-link-id",
            "nodes": link_data["nodes"],
            "filters": {"latency": 10}
        }
        
        result = link.update(filters={"latency": 10})
        
        mock_client._get_api.assert_called_once_with(LinksAPI)
        api_mock.update.assert_called_once_with("test-project-id", "test-link-id", {"filters": {"latency": 10}})
        assert result is link
        assert link._data["filters"] == {"latency": 10}
    
    def test_reset(self, mock_client, link_data):
        """Test reset method."""
        link = Link(mock_client, "test-project-id", link_data)
        api_mock = mock_client._get_api.return_value
        api_mock.reset.return_value = link_data
        
        result = link.reset()
        
        mock_client._get_api.assert_called_once_with(LinksAPI)
        api_mock.reset.assert_called_once_with("test-project-id", "test-link-id")
        assert result is link
    
    def test_start_capture(self, mock_client, link_data):
        """Test start_capture method."""
        link = Link(mock_client, "test-project-id", link_data)
        api_mock = mock_client._get_api.return_value
        
        updated_data = link_data.copy()
        updated_data["capturing"] = True
        updated_data["capture_file_name"] = "capture.pcap"
        api_mock.start_capture.return_value = updated_data
        
        result = link.start_capture(capture_file_name="capture.pcap")
        
        mock_client._get_api.assert_called_once_with(LinksAPI)
        api_mock.start_capture.assert_called_once_with(
            "test-project-id", 
            "test-link-id", 
            {"data_link_type": "DLT_EN10MB", "capture_file_name": "capture.pcap"}
        )
        assert result is link
        assert link.capturing is True
        assert link.capture_file_name == "capture.pcap"
    
    def test_stop_capture(self, mock_client, link_data):
        """Test stop_capture method."""
        # Create a link that is capturing
        capturing_link_data = link_data.copy()
        capturing_link_data["capturing"] = True
        capturing_link_data["capture_file_name"] = "capture.pcap"
        link = Link(mock_client, "test-project-id", capturing_link_data)
        
        api_mock = mock_client._get_api.return_value
        
        # The API will return a link that is no longer capturing
        updated_data = capturing_link_data.copy()
        updated_data["capturing"] = False
        api_mock.stop_capture.return_value = updated_data
        
        result = link.stop_capture()
        
        mock_client._get_api.assert_called_once_with(LinksAPI)
        api_mock.stop_capture.assert_called_once_with("test-project-id", "test-link-id")
        assert result is link
        assert link.capturing is False
    
    def test_get_capture_stream(self, mock_client, link_data):
        """Test get_capture_stream method."""
        link = Link(mock_client, "test-project-id", link_data)
        api_mock = mock_client._get_api.return_value
        api_mock.get_capture_stream.return_value = b"packet data"
        
        result = link.get_capture_stream()
        
        mock_client._get_api.assert_called_once_with(LinksAPI)
        api_mock.get_capture_stream.assert_called_once_with("test-project-id", "test-link-id")
        assert result == b"packet data"
    
    def test_get_available_filters(self, mock_client, link_data):
        """Test get_available_filters method."""
        link = Link(mock_client, "test-project-id", link_data)
        api_mock = mock_client._get_api.return_value
        api_mock.get_available_filters.return_value = ["latency", "packet_loss"]
        
        result = link.get_available_filters()
        
        mock_client._get_api.assert_called_once_with(LinksAPI)
        api_mock.get_available_filters.assert_called_once_with("test-project-id", "test-link-id")
        assert result == ["latency", "packet_loss"]
    
    def test_repr(self, mock_client, link_data):
        """Test __repr__ method."""
        link = Link(mock_client, "test-project-id", link_data)
        
        representation = repr(link)
        
        assert "test-link-id" in representation
        assert "node1 -> node2" in representation
        assert "capturing=False" in representation 