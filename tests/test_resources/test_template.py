"""
Tests for the Template resource class.
"""
import pytest
from unittest.mock import MagicMock, patch
from gns3client.resources.template import Template
from gns3client.api.templates import TemplatesAPI


class TestTemplate:
    """Tests for the Template class."""

    def test_properties(self, mock_client, template_data):
        """Test template properties."""
        template = Template(mock_client, template_data)
        
        assert template.id == "test-template-id"
        assert template.name == "Test Template"
        assert template.template_type == "vpcs"
        assert template.compute_id == "local"
    
    @patch('gns3client.resources.template.TemplatesAPI')
    def test_refresh(self, mock_templates_api_class, mock_client, template_data):
        """Test refresh method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_templates_api_class.return_value = mock_api_instance
        mock_api_instance.get.return_value = {"template_id": "test-template-id", "name": "Updated Template"}
        
        # Create the template and call refresh
        template = Template(mock_client, template_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = template.refresh()
        
        # Verify the API call
        mock_templates_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.get.assert_called_once_with("test-access-token", "test-template-id")
        
        # Verify the result
        assert result is template
        assert template._data["name"] == "Updated Template"
    
    @patch('gns3client.resources.template.TemplatesAPI')
    def test_update(self, mock_templates_api_class, mock_client, template_data):
        """Test update method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_templates_api_class.return_value = mock_api_instance
        mock_api_instance.update.return_value = {"template_id": "test-template-id", "name": "Updated Template"}
        
        # Create the template and call update
        template = Template(mock_client, template_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = template.update(name="Updated Template")
        
        # Verify the API call
        mock_templates_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.update.assert_called_once_with(
            "test-access-token", "test-template-id", {"name": "Updated Template"}
        )
        
        # Verify the result
        assert result is template
        assert template._data["name"] == "Updated Template"
    
    @patch('gns3client.resources.template.TemplatesAPI')
    def test_delete(self, mock_templates_api_class, mock_client, template_data):
        """Test delete method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_templates_api_class.return_value = mock_api_instance
        
        # Create the template and call delete
        template = Template(mock_client, template_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        template.delete()
        
        # Verify the API call
        mock_templates_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.delete.assert_called_once_with("test-access-token", "test-template-id")
    
    @patch('gns3client.resources.template.TemplatesAPI')
    def test_duplicate(self, mock_templates_api_class, mock_client, template_data):
        """Test duplicate method."""
        # Setup the mock API instance
        mock_api_instance = MagicMock()
        mock_templates_api_class.return_value = mock_api_instance
        duplicated_data = {"template_id": "new-template-id", "name": "Duplicated Template"}
        mock_api_instance.duplicate_template.return_value = duplicated_data
        
        # Create the template and call duplicate
        template = Template(mock_client, template_data)
        mock_client.host = "http://test-host:3080"
        mock_client.access_token = "test-access-token"
        
        result = template.duplicate(name="Duplicated Template")
        
        # Verify the API call
        mock_templates_api_class.assert_called_once_with("http://test-host:3080")
        mock_api_instance.duplicate_template.assert_called_once_with(
            "test-access-token", "test-template-id", {"name": "Duplicated Template"}
        )
        
        # Verify the result
        assert result == duplicated_data
        assert result["template_id"] == "new-template-id"
        assert result["name"] == "Duplicated Template"
    
    def test_repr(self, mock_client, template_data):
        """Test __repr__ method."""
        template = Template(mock_client, template_data)
        
        representation = repr(template)
        
        assert "test-template-id" in representation
        assert "Test Template" in representation
        assert "vpcs" in representation 