from typing import Dict, Any
from gns3client.api.templates import TemplatesAPI


class Template:
    """Represents a GNS3 node template.
    
    This class provides methods for working with a GNS3 node template.
    """
    
    def __init__(self, client, data: Dict[str, Any]):
        """Initialize a Template instance.
        
        Args:
            client: The GNS3Client instance
            data: The template data dictionary
        """
        self._client = client
        self._data = data
        self._id = data.get('template_id')
    
    @property
    def id(self) -> str:
        """Get the template ID.
        
        Returns:
            str: The template ID
        """
        return self._id
    
    @property
    def name(self) -> str:
        """Get the template name.
        
        Returns:
            str: The template name
        """
        return self._data.get('name', '')
    
    @property
    def template_type(self) -> str:
        """Get the template type.
        
        Returns:
            str: The template type
        """
        return self._data.get('template_type', '')
    
    @property
    def compute_id(self) -> str:
        """Get the compute ID.
        
        Returns:
            str: The compute ID
        """
        return self._data.get('compute_id', 'local')
    
    def refresh(self) -> 'Template':
        """Refresh the template data from the server.
        
        Returns:
            Template: The updated template instance
        """
        templates_api = TemplatesAPI(self._client.host)
        self._data = templates_api.get(self._client.access_token, self.id)
        return self
    
    def update(self, **kwargs) -> 'Template':
        """Update the template properties.
        
        Args:
            **kwargs: Template attributes to update
            
        Returns:
            Template: The updated template instance
        """
        templates_api = TemplatesAPI(self._client.host)
        self._data = templates_api.update(self._client.access_token, self.id, kwargs)
        return self
    
    def duplicate(self, name: str = None) -> Dict[str, Any]:
        """Duplicate the template.
        
        Args:
            name: Optional name for the duplicated template
            
        Returns:
            Dict[str, Any]: The duplicated template data dictionary
        """
        templates_api = TemplatesAPI(self._client.host)
        
        return templates_api.duplicate_template(self._client.access_token, self.id, name)
    
    def __repr__(self) -> str:
        """String representation of the template.
        
        Returns:
            str: String representation
        """
        return f"<Template id={self.id} name={self.name} type={self.template_type}>" 