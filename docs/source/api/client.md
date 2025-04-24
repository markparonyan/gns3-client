# GNS3Client API Reference

The `GNS3Client` class is the main entry point for interacting with the GNS3 server. It provides methods for authentication, project management, and server control.

## Class: GNS3Client

```python
from gns3client import GNS3Client
```

### Constructor

```python
client = GNS3Client(host="http://127.0.0.1:3080", username="admin", password="admin", access_token=None)
```

#### Parameters

- `host` (str): The GNS3 server host URL, defaults to "http://127.0.0.1:3080"
- `username` (str): The username for authentication, defaults to "admin" 
- `password` (str): The password for authentication, defaults to "admin"
- `access_token` (str, optional): The OAuth2 access token for authentication

#### Example

```python
# Create a client with default connection settings
client = GNS3Client()

# Create a client with custom connection settings
client = GNS3Client(
    host="http://gns3-server:3080",
    username="admin",
    password="secret"
)

# Create a client with an access token
client = GNS3Client(
    host="http://gns3-server:3080",
    access_token="your-access-token"
)
```

### Authentication Methods

#### login

```python
access_token = client.login(username=None, password=None)
```

Login to the GNS3 server and get an access token.

##### Parameters

- `username` (str, optional): The username (defaults to self.username if not provided)
- `password` (str, optional): The password (defaults to self.password if not provided)

##### Returns

- `str`: The access token if successful

##### Raises

- `ValueError`: If login fails

##### Example

```python
try:
    token = client.login()
    print(f"Successfully logged in with token: {token}")
except ValueError as e:
    print(f"Login failed: {e}")
```

#### set_access_token

```python
client.set_access_token(access_token)
```

Set the access token for authentication.

##### Parameters

- `access_token` (str): The OAuth2 access token

##### Example

```python
# Set an access token
client.set_access_token("your-access-token")
```

### Server Information Methods

#### version

```python
version_info = client.version()
```

Get the GNS3 controller version.

##### Returns

- `dict`: The version information

##### Example

```python
version = client.version()
print(f"GNS3 server version: {version['version']}")
```

#### stats

```python
stats_info = client.stats()
```

Get the GNS3 controller statistics.

##### Returns

- `dict`: The statistics information

##### Example

```python
stats = client.stats()
print(f"GNS3 server memory usage: {stats['memory']['used']} / {stats['memory']['total']}")
```

#### shutdown

```python
response = client.shutdown()
```

Shutdown the GNS3 controller.

##### Returns

- `dict`: The response data

##### Example

```python
client.shutdown()
print("GNS3 server is shutting down")
```

#### reload

```python
response = client.reload()
```

Reload the GNS3 controller.

##### Returns

- `dict`: The response data

##### Example

```python
client.reload()
print("GNS3 server is reloading")
```

#### notifications

```python
notifications_list = client.notifications()
```

Get the GNS3 controller notifications.

##### Returns

- `list`: The list of notifications

##### Example

```python
notifications = client.notifications()
for notification in notifications:
    print(f"Notification: {notification['message']}")
```

### Project Management Methods

#### create_project

```python
project = client.create_project(name, **kwargs)
```

Create a new project.

##### Parameters

- `name` (str): The name of the project
- `**kwargs`: Additional project parameters

##### Returns

- `Project`: The created Project object

##### Example

```python
# Create a simple project
project = client.create_project("My New Project")

# Create a project with additional parameters
project = client.create_project(
    name="Advanced Project",
    path="/path/to/projects/advanced",
    auto_open=True,
    auto_close=False
)
```

#### list_projects

```python
projects = client.list_projects()
```

Get all projects.

##### Returns

- `list`: List of Project objects

##### Example

```python
projects = client.list_projects()
for project in projects:
    print(f"Project: {project.name} (ID: {project.id})")
```

#### get_project

```python
project = client.get_project(identifier)
```

Get a project by ID or name.

##### Parameters

- `identifier` (str): The project ID or name

##### Returns

- `Project`: The project object

##### Raises

- `ValueError`: If no project with the provided name/ID exists

##### Example

```python
# Get by ID
project = client.get_project("project-id-here")

# Get by name
project = client.get_project("My Network Project")
```

#### import_project

```python
project = client.import_project(project_file, name=None)
```

Import a project from a file.

##### Parameters

- `project_file` (bytes): The project file content to import
- `name` (str, optional): The name for the imported project

##### Returns

- `Project`: The imported Project object

##### Example

```python
with open("network.gns3project", "rb") as f:
    project_data = f.read()
    
imported_project = client.import_project(project_data, name="Imported Network")
```

#### list_templates

```python
templates = client.list_templates()
```

Get all templates.

##### Returns

- `list`: List of Template objects

##### Example

```python
templates = client.list_templates()
for template in templates:
    print(f"Template: {template.name} (Type: {template.template_type})")
``` 