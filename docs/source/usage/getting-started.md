# Getting Started

This guide will walk you through the basics of using the GNS3 Client library to interact with the GNS3 server.

## Connecting to the GNS3 Server

First, you'll need to import the `GNS3Client` class and create an instance:

```python
from gns3client import GNS3Client

# Connect to the GNS3 server
client = GNS3Client(host="http://localhost:3080", username="admin", password="admin")
```

Once connected, you can verify the connection by checking the server version:

```python
version_info = client.version()
print(f"Connected to GNS3 server version: {version_info['version']}")
```

## Working with Projects

### List All Projects

```python
projects = client.list_projects()
for project in projects:
    print(f"Project: {project.name} (ID: {project.id})")
```

### Create a New Project

```python
new_project = client.create_project("My Network Project")
print(f"Created project: {new_project.name} (ID: {new_project.id})")
```

### Get an Existing Project

You can get a project by its ID or name:

```python
# By ID
project = client.get_project("project-id-here")

# By name
project = client.get_project("My Network Project")
```

### Open and Close Projects

Projects need to be opened before you can work with them:

```python
# Open a project
project.open()

# Close when done
project.close()
```

### Delete a Project

```python
project.delete()
```

## Working with Nodes

### Create a Node

```python
# First get a project
project = client.get_project("My Network Project")

# Create a VPCS node
vpcs_node = project.create_node(
    name="PC1",
    node_type="vpcs"
)

# Create a Cisco router
router = project.create_node(
    name="R1",
    node_type="dynamips",
    properties={
        "platform": "c7200",
        "image": "c7200-adventerprisek9-mz.152-4.S6.image",
    }
)
```

### List Nodes in a Project

```python
nodes = project.list_nodes()
for node in nodes:
    print(f"Node: {node.name} (Type: {node.node_type}, Status: {node.status})")
```

### Control Nodes

```python
# Start a node
node.start()

# Stop a node
node.stop()

# Restart a node
node.stop()
node.start()

# Suspend a node
node.suspend()
```

### Get Node Console Information

```python
print(f"Console port: {node.console}")
print(f"Console host: {node.console_host}")
```

### Delete a Node

```python
node.delete()
```

## Working with Links

### Create a Link

To create a link, you need to specify the nodes and ports to connect:

```python
# Create a link between two nodes
link = project.create_link([
    {
        "node_id": router.id,
        "adapter_number": 0,
        "port_number": 0
    },
    {
        "node_id": vpcs_node.id, 
        "adapter_number": 0,
        "port_number": 0
    }
])
```

### List Links in a Project

```python
links = project.list_links()
for link in links:
    print(f"Link ID: {link.id}, Connected nodes: {len(link.nodes)}")
```

### Packet Capture on a Link

```python
# Start packet capture
link.start_capture(capture_file_name="my_capture.pcap")

# Stop capture
link.stop_capture()

# Get capture data
capture_data = link.get_capture_stream()
with open("my_capture.pcap", "wb") as f:
    f.write(capture_data)
```

### Delete a Link

```python
link.delete()
```

## Project Control Operations

You can control all nodes in a project with these operations:

```python
# Start all nodes
project.start_all()

# Stop all nodes
project.stop_all()

# Suspend all nodes
project.suspend_all()
```

## Next Steps

Now that you understand the basics, check out:

- [Python API Reference](python-api.md) for more details on the Python API
- [Command Line Interface](cli.md) for information on using the CLI tool
- [API Reference](../api/client.md) for a complete reference of all available methods 