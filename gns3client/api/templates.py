from gns3client.openapi_client.apis.tags.templates_api import TemplatesApi
from gns3client.api.base_api import BaseAPI


class TemplatesAPI(BaseAPI):
    """API wrapper for templates endpoints."""
    
    def list(self, access_token: str) -> list:
        """Get all templates.
        
        Args:
            access_token: The OAuth2 access token
            
        Returns:
            list: List of templates
        """
        return self._call_api(
            access_token,
            TemplatesApi,
            "templates_get",
            "templates_get"
        )
    
    def get(self, access_token: str, template_id: str) -> dict:
        """Get a template by ID.
        
        Args:
            access_token: The OAuth2 access token
            template_id: The template ID
            
        Returns:
            dict: The template data
        """
        return self._call_api(
            access_token,
            TemplatesApi,
            "templates_template_id_get",
            "templates_template_id_get",
            template_id
        )
    
    def create(self, access_token: str, name: str, **kwargs) -> dict:
        """Create a new template.
        
        Args:
            access_token: The OAuth2 access token
            name: The template name
            **kwargs: Additional template attributes
            
        Returns:
            dict: The created template data
        """
        template_data = {
            "name": name,
            **kwargs
        }
        
        return self._call_api(
            access_token,
            TemplatesApi,
            "templates_post",
            "templates_post",
            template_data
        )
    
    def update(self, access_token: str, template_id: str, **kwargs) -> dict:
        """Update a template.
        
        Args:
            access_token: The OAuth2 access token
            template_id: The template ID
            **kwargs: Template attributes to update
            
        Returns:
            dict: The updated template data
        """
        return self._call_api(
            access_token,
            TemplatesApi,
            "templates_template_id_put",
            "templates_template_id_put",
            template_id,
            kwargs
        )
    
    def delete(self, access_token: str, template_id: str) -> dict:
        """Delete a template.
        
        Args:
            access_token: The OAuth2 access token
            template_id: The template ID
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            TemplatesApi,
            "templates_template_id_delete",
            "templates_template_id_delete",
            template_id
        )
            
    def duplicate_template(self, access_token, template_id, name=None):
        """Duplicate a template.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            template_id (str): The ID of the template to duplicate
            name (str, optional): The name for the duplicated template
            
        Returns:
            dict: The duplicated template details
        """
        body = {"name": name} if name else {}
        
        return self._call_api(
            access_token,
            TemplatesApi,
            "duplicate_template_v3_templates_template_id_duplicate_post",
            "TemplatesApi->duplicate_template_v3_templates_template_id_duplicate_post",
            template_id,
            body=body
        ) 