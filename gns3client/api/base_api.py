import os
import sys
import importlib.util
import importlib.machinery

parent_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(parent_dir)

openapi_client_dir = os.path.join(parent_dir, 'client', 'openapi_client')
sys.path.append(openapi_client_dir)

from configuration import Configuration
from api_client import ApiClient
from exceptions import ApiException


class BaseAPI:
    """Base class for all API wrappers."""
    
    def __init__(self, host="http://localhost:3080"):
        """Initialize the API with the GNS3 server host.
        
        Args:
            host (str): The GNS3 server host URL 
        """
        self.host = host
    
    def _get_api_client(self, access_token):
        """Get an API client with proper authentication.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            
        Returns:
            tuple: (api_client, configuration) - The API client and configuration objects
        """
        # NOTE: Lost quite a bit of time figuring out why the Authorization header was not being set
        # Apparentely, the ApiClient doesn't set the Authorization header automatically
        # so we need to do it manually and now i dont understand whats the point to pass
        # the access_token in the Configuration constructor.
        configuration = Configuration(host=self.host, access_token=access_token)
        api_client = ApiClient(configuration)
        api_client.set_default_header("Authorization", f"Bearer {access_token}")
        return api_client, configuration
    
    def _handle_api_exception(self, e, operation_name):
        """Handle API exceptions in a consistent way.
        
        Args:
            e (ApiException): The exception that was raised
            operation_name (str): The name of the operation that failed
            
        Returns:
            None: This method prints the error and returns None
        """
        print(f"Exception when calling {operation_name}: {e}")
        return None
        
    def _call_api(self, access_token, api_class, method_name, operation_name, *args, **kwargs):
        """Generic method to call an API endpoint.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            api_class: The API class to instantiate (e.g., projects_api.ProjectsApi)
            method_name (str): The name of the method to call on the API instance
            operation_name (str): The name of the operation for error reporting
            *args: Positional arguments to pass to the API method
            **kwargs: Keyword arguments to pass to the API method
            
        Returns:
            The response body from the API call, or None if an error occurred
        """
        try:
            api_client, _ = self._get_api_client(access_token)
            with api_client:
                api_instance = api_class(api_client)
                method = getattr(api_instance, method_name)
                api_response = method(*args, **kwargs)
                return api_response.body
        except ApiException as e:
            return self._handle_api_exception(e, operation_name) 
