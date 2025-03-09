from __future__ import annotations
from typing import Optional, Dict, Type, Any, List, Callable


from gns3client.api.projects import ProjectsAPI
from gns3client.api.nodes import NodesAPI
from gns3client.api.links import LinksAPI
from gns3client.api.users import UsersAPI
from gns3client.api.templates import TemplatesAPI
from gns3client.api.drawings import DrawingsAPI
from gns3client.api.snapshots import SnapshotsAPI
from gns3client.api.controller import ControllerAPI
from gns3client.api.base_api import BaseAPI
from gns3client.resources.project import Project
from gns3client.resources.template import Template



class GNS3Client:
    """Client for interacting with the GNS3 server.
    
    This client provides access to all the GNS3 API endpoints through
    specialized API wrappers.
    """
    
    def __init__(self, host="http://127.0.0.1:3080", username="admin", password="admin", access_token=None):
        """Initialize the GNS3 client.
        
        Args:
            host: The GNS3 server host URL (default: http://127.0.0.1:3080)
            username: The username for authentication (default: admin)
            password: The password for authentication (default: admin)
            access_token: The OAuth2 access token for authentication
        """
        self.host = host
        self.username = username
        self.password = password
        self.access_token = access_token
        self._api_instances: Dict[Type[BaseAPI], BaseAPI] = {}
        
        if username and password and not access_token:
            self.login(username, password)

    
    @property
    def projects(self) -> APIProxy:
        """Get the projects API wrapper.
        
        Returns:
            APIProxy: A proxy for the ProjectsAPI that automatically passes the access token
            
        Examples:
            >>> client.projects.list()  # List all projects
            >>> client.projects.get("project_id")  # Get a specific project
            >>> client.projects.create("New Project")  # Create a new project
        """
        return self._get_api(ProjectsAPI)
    
    @property
    def nodes(self) -> APIProxy:
        """Get the nodes API wrapper.
        
        Returns:
            APIProxy: A proxy for the NodesAPI that automatically passes the access token
            
        Examples:
            >>> client.nodes.list("project_id")  # List all nodes in a project
            >>> client.nodes.get("project_id", "node_id")  # Get a specific node
            >>> client.nodes.create("project_id", node_data)  # Create a new node
        """
        return self._get_api(NodesAPI)
    
    @property
    def links(self) -> APIProxy:
        """Get the links API wrapper.
        
        Returns:
            APIProxy: A proxy for the LinksAPI that automatically passes the access token
            
        Examples:
            >>> client.links.list("project_id")  # List all links in a project
            >>> client.links.get("project_id", "link_id")  # Get a specific link
            >>> client.links.create("project_id", link_data)  # Create a new link
        """
        return self._get_api(LinksAPI)
    
    @property
    def users(self) -> APIProxy:
        """Get the users API wrapper.
        
        Returns:
            APIProxy: A proxy for the UsersAPI that automatically passes the access token
            
        Examples:
            >>> client.users.list()  # List all users
            >>> client.users.get("user_id")  # Get a specific user
            >>> client.users.me()  # Get the current logged-in user
        """
        return self._get_api(UsersAPI)
    
    @property
    def templates(self) -> APIProxy:
        """Get the templates API wrapper.
        
        Returns:
            APIProxy: A proxy for the TemplatesAPI that automatically passes the access token
            
        Examples:
            >>> client.templates.list()  # List all templates
            >>> client.templates.get("template_id")  # Get a specific template
            >>> client.templates.create(template_data)  # Create a new template
        """
        return self._get_api(TemplatesAPI)
    
    @property
    def drawings(self) -> APIProxy:
        """Get the drawings API wrapper.
        
        Returns:
            APIProxy: A proxy for the DrawingsAPI that automatically passes the access token
            
        Examples:
            >>> client.drawings.list("project_id")  # List all drawings in a project
            >>> client.drawings.get("project_id", "drawing_id")  # Get a specific drawing
            >>> client.drawings.create("project_id", drawing_data)  # Create a new drawing
        """
        return self._get_api(DrawingsAPI)
    
    @property
    def snapshots(self) -> APIProxy:
        """Get the snapshots API wrapper.
        
        Returns:
            APIProxy: A proxy for the SnapshotsAPI that automatically passes the access token
            
        Examples:
            >>> client.snapshots.list("project_id")  # List all snapshots for a project
            >>> client.snapshots.get("project_id", "snapshot_id")  # Get a specific snapshot
            >>> client.snapshots.create("project_id", "Snapshot Name")  # Create a new snapshot
        """
        return self._get_api(SnapshotsAPI)
    
    @property
    def controller(self) -> APIProxy:
        """Get the controller API wrapper.
        
        Returns:
            APIProxy: A proxy for the ControllerAPI that automatically passes the access token
            
        Examples:
            >>> client.controller.version()  # Get the GNS3 controller version
            >>> client.controller.stats()  # Get controller statistics
            >>> client.controller.reload()  # Reload the controller
        """
        return self._get_api(ControllerAPI)
    
    
    def login(self, username: str = None, password: str = None) -> str | None:
        """Login to the GNS3 server and get an access token.
        
        Args:
            username: The username (defaults to self.username if not provided)
            password: The password (defaults to self.password if not provided)
            
        Returns:
            str: The access token if successful
            
        Raises:
            ValueError: If login fails
        """
        username = username or self.username
        password = password or self.password
        
        response = self.users.login(username, password)
        if response and "access_token" in response:
            self.access_token = response["access_token"]
            return self.access_token
        
        raise ValueError("Login failed. Check your credentials and server connection.")
    
    def set_access_token(self, access_token: str) -> None:
        """Set the access token for authentication.
        
        Args:
            access_token: The OAuth2 access token
        """
        self.access_token = access_token
        self._api_instances = {}
    
    def version(self) -> Dict[str, Any]:
        """Get the GNS3 controller version.
        
        Returns:
            dict: The version information
        """
        controller_api = ControllerAPI(self.host)
        return controller_api.version(self.access_token)
    
    def list_projects(self) -> List[Project]:
        """Get all projects.
        
        Returns:
            list: List of Project objects
        """
        projects_api = ProjectsAPI(self.host)
        projects_data = projects_api.list(self.access_token)
        
        return [Project(self, data) for data in projects_data]
    
    def get_project(self, project_id: str) -> Project:
        """Get a project by ID.
        
        Args:
            project_id: The project ID
            
        Returns:
            Project: The project object
        """
        projects_api = ProjectsAPI(self.host)
        project_data = projects_api.get(self.access_token, project_id)
        
        return Project(self, project_data)
    
    def create_project(self, name: str, **kwargs) -> Project:
        """Create a new project.
        
        Args:
            name: The project name
            **kwargs: Additional project attributes
            
        Returns:
            Project: The created project object
        """
        projects_api = ProjectsAPI(self.host)
        project_data = projects_api.create(self.access_token, name, **kwargs)
        
        return Project(self, project_data)
    
    def list_templates(self) -> List[Template]:
        """Get all templates.
        
        Returns:
            list: List of Template objects
        """
        templates_api = TemplatesAPI(self.host)
        templates_data = templates_api.list(self.access_token)
        
        return [Template(self, data) for data in templates_data]
    
    def _get_api(self, api_class: Type[BaseAPI]) -> APIProxy:
        """Get an API instance with the current access token.
        
        Args:
            api_class: The API class to instantiate
            
        Returns:
            APIProxy: A proxy for the API that automatically passes the access token
        """
        if api_class not in self._api_instances:
            self._api_instances[api_class] = api_class(self.host)
        
        return APIProxy(self._api_instances[api_class], self.access_token)


class APIProxy:
    """Proxy for API instances that automatically passes the access token."""
    
    def __init__(self, api_instance, access_token: str):
        """Initialize the API proxy.
        
        Args:
            api_instance: The API instance to proxy
            access_token: The access token to pass to API methods
        """
        self._api_instance = api_instance
        self._access_token = access_token
    
    def __getattr__(self, name: str):
        """Get an attribute from the API instance.
        
        This method intercepts attribute access and wraps API methods to
        automatically pass the access token.
        
        Args:
            name: The attribute name
            
        Returns:
            callable: A wrapper function that passes the access token to the API method
        """
        attr = getattr(self._api_instance, name)
        
        if callable(attr):
            def wrapper(*args, **kwargs):
                return attr(self._access_token, *args, **kwargs)
            return wrapper
        
        return attr

