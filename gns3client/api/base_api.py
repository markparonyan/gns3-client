from __future__ import annotations
from typing import Any
import json

from gns3client.openapi_client.configuration import Configuration
from gns3client.openapi_client.api_client import ApiClient
from gns3client.openapi_client.exceptions import ApiException


class BaseAPI:
    """Base class for all API wrappers."""
    
    def __init__(self, host="http://localhost:3080"):
        """Initialize the API with the GNS3 server host.
        
        Args:
            host (str): The GNS3 server host URL 
        """
        self.host = host
    
    def _get_api_client(self, access_token: str) -> tuple[ApiClient, Configuration]:
        """Get an API client with proper authentication.
        
        Args:
            access_token: The OAuth2 access token for authentication
            
        Returns:
            tuple: (api_client, configuration) - The API client and configuration objects
        """
        # NOTE: Lost quite a bit of time figuring out why the Authorization header was not being set
        # Apparentely, the ApiClient doesn't set the Authorization header automatically
        # so we need to do it manually and now i dont understand whats the point to pass
        # the access_token in the Configuration constructor.
        configuration = Configuration(host=self.host, access_token=access_token)
        api_client = ApiClient(configuration)
        api_client.default_headers["Authorization"] = f"Bearer {access_token}"
        return api_client, configuration
    
    def _handle_api_exception(self, e: ApiException, operation_name: str) -> dict:
        """Handle API exceptions in a consistent way.
        
        Args:
            e: The exception that was raised
            operation_name: The name of the operation that failed
            
        Returns:
            dict: A dictionary with error information
        """
        error_info = {
            "error": f"API Error: {operation_name}",
            "status": getattr(e, "status", None),
            "reason": getattr(e, "reason", str(e))
        }
        
        if hasattr(e, "body") and e.body:
            try:
                error_detail = json.loads(e.body)
                if isinstance(error_detail, dict):
                    error_info["detail"] = error_detail.get("detail", error_detail)
                else:
                    error_info["detail"] = error_detail
            except json.JSONDecodeError:
                error_info["body"] = e.body
        
        print(f"Exception when calling {operation_name}: {e}")
        return error_info
        
    def _call_api(self, access_token: str, api_class: BaseAPI, method_name: str, operation_name: str, *args: Any, **kwargs: Any) -> dict | list | Any:
        """Generic method to call an API endpoint.
        
        Args:
            access_token: The OAuth2 access token for authentication
            api_class: The API class to instantiate (e.g., projects_api.ProjectsApi)
            method_name: The name of the method to call on the API instance
            operation_name: The name of the operation for error reporting
            *args: Positional arguments to pass to the API method
            **kwargs: Keyword arguments to pass to the API method
            
        Returns:
            dict, list, or primitive type: The response data from the API call, 
            converted to Python native types, or None if an error occurred
        """
        try:
            api_client, _ = self._get_api_client(access_token)
            with api_client:
                api_client.default_headers["Authorization"] = f"Bearer {access_token}"
                api_instance = api_class(api_client)
                method = getattr(api_instance, method_name)
                api_response = method(*args, **kwargs)
                
                return api_response.body
        except ApiException as e:
            return self._handle_api_exception(e, operation_name) 
