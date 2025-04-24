from gns3client.openapi_client.apis.tags.controller_api import ControllerApi
from gns3client.api.base_api import BaseAPI


class ControllerAPI(BaseAPI):
    """API wrapper for GNS3 Controller API."""

    def version(self, access_token=None):
        """Get the GNS3 controller version.
        
        Args:
            access_token (str, optional): The OAuth2 access token for authentication
            
        Returns:
            dict: The version information
        """
        return self._call_api(
            access_token,
            ControllerApi,
            "get_version_v3_version_get",
            "ControllerApi->get_version_v3_version_get"
        )
            
    def stats(self, access_token):
        """Get the GNS3 controller statistics.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            
        Returns:
            dict: The statistics information
        """
        return self._call_api(
            access_token,
            ControllerApi,
            "get_statistics_v3_statistics_get",
            "ControllerApi->get_statistics_v3_statistics_get"
        )
            
    def shutdown(self, access_token):
        """Shutdown the GNS3 controller.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            ControllerApi,
            "shutdown_v3_shutdown_post",
            "ControllerApi->shutdown_v3_shutdown_post"
        )
            
    def reload(self, access_token):
        """Reload the GNS3 controller.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            
        Returns:
            dict: The response data
        """
        return self._call_api(
            access_token,
            ControllerApi,
            "reload_v3_reload_post",
            "ControllerApi->reload_v3_reload_post"
        )
            
    def notifications(self, access_token):
        """Get the GNS3 controller notifications.
        
        Args:
            access_token (str): The OAuth2 access token for authentication
            
        Returns:
            list: The list of notifications
        """
        return self._call_api(
            access_token,
            ControllerApi,
            "get_notifications_v3_notifications_get",
            "ControllerApi->get_notifications_v3_notifications_get"
        )

