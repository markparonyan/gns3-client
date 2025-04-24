# Project API Reference

The `Project` class represents a GNS3 project and provides methods for managing project resources like nodes, links, and drawings.

## Class: Project

```python
from gns3client import GNS3Client
# Project objects are created by the GNS3Client
client = GNS3Client()
project = client.get_project("My Project")
```

### Properties

#### id

```python
project_id = project.id
```

Get the project ID.

##### Returns

- `str`: The project ID

##### Example

```python
print(f"Project ID: {project.id}")
```

#### name

```python
project_name = project.name
```

Get the project name.

##### Returns

- `str`: The project name

##### Example

```python
print(f"Project name: {project.name}")
```

#### status

```python
project_status = project.status
```

Get the project status.

##### Returns

- `str`: The project status (e.g., "opened", "closed")

##### Example

```python
print(f"Project status: {project.status}")
```

#### path

```python
project_path = project.path
```

Get the project file path.

##### Returns

- `str`: The project file path on the server

##### Example

```python
print(f"Project path: {project.path}")
```

### Project Management Methods

#### refresh

```python
project = project.refresh()
```

Refresh the project data from the server.

##### Returns

- `Project`: The updated project instance

##### Example

```python
# Refresh project data
project = project.refresh()
print(f"Project status: {project.status}")
```

#### open

```python
project = project.open()
```

Open the project.

##### Returns

- `Project`: The updated project instance

##### Example

```python
# Open the project
project = project.open()
print(f"Project status after opening: {project.status}")
```

#### close

```python
project = project.close()
```

Close the project.

##### Returns

- `Project`: The updated project instance

##### Example

```python
# Close the project
project = project.close()
print(f"Project status after closing: {project.status}")
```

#### delete

```python
project.delete()
```

Delete the project.

##### Example

```python
# Delete the project
project.delete()
print("Project deleted")
```

#### update

```python
project = project.update(**kwargs)
```

Update the project properties.

##### Parameters

- `**kwargs`: Project attributes to update

##### Returns

- `Project`: The updated project instance

##### Example

```python
# Update project name
project = project.update(name="Updated Project Name")
print(f"New project name: {project.name}")
```

### Node Management Methods

#### list_nodes

```python
nodes = project.list_nodes()
```

List all nodes in the project.

##### Returns

- `List[Node]`: List of Node objects

##### Example

```python
# Get all nodes in the project
nodes = project.list_nodes()
for node in nodes:
    print(f"Node: {node.name} (Type: {node.node_type}, Status: {node.status})")
```

#### get_node

```python
node = project.get_node(node_id)
```

Get a specific node in the project.

##### Parameters

- `node_id` (str): The ID of the node

##### Returns

- `Node`: The Node object

##### Example

```python
# Get a specific node
node = project.get_node("node-id-here")
print(f"Node: {node.name}")
```

#### create_node

```python
node = project.create_node(name, node_type, compute_id="local", **kwargs)
```

Create a new node in the project.

##### Parameters

- `name` (str): The name of the node
- `node_type` (str): The type of the node
- `compute_id` (str, optional): The compute ID (default: "local")
- `**kwargs`: Additional node parameters

##### Returns

- `Node`: The created Node object

##### Example

```python
# Create a VPCS node
vpcs = project.create_node(
    name="PC1",
    node_type="vpcs"
)

# Create a Cisco router
router = project.create_node(
    name="R1",
    node_type="dynamips",
    properties={
        "platform": "c7200",
        "image": "c7200-adventerprisek9-mz.152-4.S6.image"
    }
)
```

#### start_all

```python
project.start_all()
```

Start all nodes in the project.

##### Example

```python
# Start all nodes
project.start_all()
print("All nodes started")
```

#### stop_all

```python
project.stop_all()
```

Stop all nodes in the project.

##### Example

```python
# Stop all nodes
project.stop_all()
print("All nodes stopped")
```

#### suspend_all

```python
project.suspend_all()
```

Suspend all nodes in the project.

##### Example

```python
# Suspend all nodes
project.suspend_all()
print("All nodes suspended")
```

#### reload_all

```python
project.reload_all()
```

Reload all nodes in the project.

##### Example

```python
# Reload all nodes
project.reload_all()
print("All nodes reloaded")
```

#### reset_console_all

```python
project.reset_console_all()
```

Reset console for all nodes in the project.

##### Example

```python
# Reset all consoles
project.reset_console_all()
print("All consoles reset")
```

#### delete_node

```python
project.delete_node(node_id)
```

Delete a node from the project.

##### Parameters

- `node_id` (str): The ID of the node

##### Example

```python
# Delete a node
project.delete_node("node-id-here")
print("Node deleted")
```

### Link Management Methods

#### list_links

```python
links = project.list_links()
```

List all links in the project.

##### Returns

- `List[Link]`: List of Link objects

##### Example

```python
# Get all links in the project
links = project.list_links()
for link in links:
    print(f"Link: {link.id}")
```

#### get_link

```python
link = project.get_link(link_id)
```

Get a specific link in the project.

##### Parameters

- `link_id` (str): The ID of the link

##### Returns

- `Link`: The Link object

##### Example

```python
# Get a specific link
link = project.get_link("link-id-here")
print(f"Link: {link.id}")
```

#### create_link

```python
link = project.create_link(nodes)
```

Create a new link in the project.

##### Parameters

- `nodes` (List[Dict[str, Any]]): List of node connection information

##### Returns

- `Link`: The created Link object

##### Example

```python
# Create a link between two nodes
link = project.create_link([
    {
        "node_id": "router1-id",
        "adapter_number": 0,
        "port_number": 0
    },
    {
        "node_id": "router2-id",
        "adapter_number": 0,
        "port_number": 0
    }
])
print(f"Link created: {link.id}")
```

#### delete_link

```python
project.delete_link(link_id)
```

Delete a link from the project.

##### Parameters

- `link_id` (str): The ID of the link

##### Example

```python
# Delete a link
project.delete_link("link-id-here")
print("Link deleted")
```

### Drawing Management Methods

#### list_drawings

```python
drawings = project.list_drawings()
```

List all drawings in the project.

##### Returns

- `List[Dict[str, Any]]`: List of drawing data dictionaries

##### Example

```python
# Get all drawings in the project
drawings = project.list_drawings()
for drawing in drawings:
    print(f"Drawing: {drawing['drawing_id']}")
```

#### get_drawing

```python
drawing = project.get_drawing(drawing_id)
```

Get a specific drawing in the project.

##### Parameters

- `drawing_id` (str): The ID of the drawing

##### Returns

- `Dict[str, Any]`: The drawing data dictionary

##### Example

```python
# Get a specific drawing
drawing = project.get_drawing("drawing-id-here")
print(f"Drawing: {drawing}")
```

#### create_drawing

```python
drawing = project.create_drawing(drawing_data)
```

Create a new drawing in the project.

##### Parameters

- `drawing_data` (Dict[str, Any]): The drawing data

##### Returns

- `Dict[str, Any]`: The created drawing data

##### Example

```python
# Create a text drawing
drawing = project.create_drawing({
    "svg": "<svg><text>Hello GNS3</text></svg>",
    "x": 100,
    "y": 100,
    "z": 0
})
print(f"Drawing created: {drawing['drawing_id']}")
```

#### delete_drawing

```python
project.delete_drawing(drawing_id)
```

Delete a drawing from the project.

##### Parameters

- `drawing_id` (str): The ID of the drawing

##### Example

```python
# Delete a drawing
project.delete_drawing("drawing-id-here")
print("Drawing deleted")
```

### Snapshot Management Methods

#### list_snapshots

```python
snapshots = project.list_snapshots()
```

List all snapshots in the project.

##### Returns

- `List[Snapshot]`: List of Snapshot objects

##### Example

```python
# Get all snapshots
snapshots = project.list_snapshots()
for snapshot in snapshots:
    print(f"Snapshot: {snapshot.name}")
```

#### create_snapshot

```python
snapshot = project.create_snapshot(name)
```

Create a new snapshot of the project.

##### Parameters

- `name` (str): The name of the snapshot

##### Returns

- `Snapshot`: The created Snapshot object

##### Example

```python
# Create a snapshot
snapshot = project.create_snapshot("Initial configuration")
print(f"Snapshot created: {snapshot.name}")
```

#### restore_snapshot

```python
project.restore_snapshot(snapshot_id)
```

Restore a snapshot of the project.

##### Parameters

- `snapshot_id` (str): The ID of the snapshot

##### Returns

- `Dict[str, Any]`: The response data

##### Example

```python
# Restore a snapshot
project.restore_snapshot("snapshot-id-here")
print("Snapshot restored")
```

#### delete_snapshot

```python
project.delete_snapshot(snapshot_id)
```

Delete a snapshot of the project.

##### Parameters

- `snapshot_id` (str): The ID of the snapshot

##### Returns

- `Dict[str, Any]`: The response data

##### Example

```python
# Delete a snapshot
project.delete_snapshot("snapshot-id-here")
print("Snapshot deleted")
``` 