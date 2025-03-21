# Node API Reference

The `Node` class represents a GNS3 node (device) within a project. It provides methods for controlling the node, managing files, and getting status information.

## Class: Node

```python
from gns3client import GNS3Client
# Node objects are created by the Project class
client = GNS3Client()
project = client.get_project("My Project")
node = project.get_node("node-id-here")
```

### Properties

#### id

```python
node_id = node.id
```

Get the node ID.

##### Returns

- `str`: The node ID

##### Example

```python
print(f"Node ID: {node.id}")
```

#### name

```python
node_name = node.name
```

Get the node name.

##### Returns

- `str`: The node name

##### Example

```python
print(f"Node name: {node.name}")
```

#### node_type

```python
node_type = node.node_type
```

Get the node type.

##### Returns

- `str`: The node type (e.g., "vpcs", "dynamips", "qemu", "docker")

##### Example

```python
print(f"Node type: {node.node_type}")
```

#### compute_id

```python
compute_id = node.compute_id
```

Get the compute ID.

##### Returns

- `str`: The compute ID

##### Example

```python
print(f"Compute ID: {node.compute_id}")
```

#### status

```python
node_status = node.status
```

Get the node status.

##### Returns

- `str`: The node status (e.g., "started", "stopped", "suspended")

##### Example

```python
print(f"Node status: {node.status}")
```

#### console

```python
console_port = node.console
```

Get the console port.

##### Returns

- `int`: The console port

##### Example

```python
print(f"Console port: {node.console}")
```

#### console_host

```python
console_host = node.console_host
```

Get the console host.

##### Returns

- `str`: The console host

##### Example

```python
print(f"Console host: {node.console_host}")
```

### Node Management Methods

#### refresh

```python
node = node.refresh()
```

Refresh the node data from the server.

##### Returns

- `Node`: The updated node instance

##### Example

```python
# Refresh node data
node = node.refresh()
print(f"Node status: {node.status}")
```

#### update

```python
node = node.update(**kwargs)
```

Update the node properties.

##### Parameters

- `**kwargs`: Node attributes to update

##### Returns

- `Node`: The updated node instance

##### Example

```python
# Update node name
node = node.update(name="Updated Node Name")
print(f"New node name: {node.name}")
```

### Node Control Methods

#### start

```python
node = node.start()
```

Start the node.

##### Returns

- `Node`: The updated node instance

##### Example

```python
# Start the node
node = node.start()
print(f"Node status after starting: {node.status}")
```

#### stop

```python
node = node.stop()
```

Stop the node.

##### Returns

- `Node`: The updated node instance

##### Example

```python
# Stop the node
node = node.stop()
print(f"Node status after stopping: {node.status}")
```

#### suspend

```python
node = node.suspend()
```

Suspend the node.

##### Returns

- `Node`: The updated node instance

##### Example

```python
# Suspend the node
node = node.suspend()
print(f"Node status after suspending: {node.status}")
```

#### reload

```python
node = node.reload()
```

Reload the node.

##### Returns

- `Node`: The updated node instance

##### Example

```python
# Reload the node
node = node.reload()
print(f"Node status after reloading: {node.status}")
```

#### console_reset

```python
node = node.console_reset()
```

Reset the console of the node.

##### Returns

- `Node`: The updated node instance

##### Example

```python
# Reset the console
node = node.console_reset()
print("Console reset")
```

### Node File Operations

#### get_file

```python
file_contents = node.get_file(path)
```

Get the contents of a file from the node.

##### Parameters

- `path` (str): The path to the file

##### Returns

- `str`: The file contents

##### Example

```python
# Get a configuration file
config = node.get_file("/etc/config.txt")
print(config)
```

#### post_file

```python
node.post_file(path, data)
```

Write data to a file on the node.

##### Parameters

- `path` (str): The path to the file
- `data` (str): The data to write

##### Example

```python
# Write to a configuration file
node.post_file("/etc/config.txt", "interface eth0\n  ip address 192.168.1.1/24\n")
print("File written")
```

### Advanced Node Operations

#### duplicate

```python
duplicate_node = node.duplicate()
```

Creates a copy of the node.

##### Returns

- `Node`: The duplicated node instance

##### Example

```python
# Duplicate a node
duplicate = node.duplicate()
print(f"Created duplicate node: {duplicate.name}")
```

#### isolate

```python
node = node.isolate()
```

Isolate the node from the network.

##### Returns

- `Node`: The updated node instance

##### Example

```python
# Isolate a node
node = node.isolate()
print("Node isolated")
```

#### unisolate

```python
node = node.unisolate()
```

Remove isolation from the node.

##### Returns

- `Node`: The updated node instance

##### Example

```python
# Remove isolation
node = node.unisolate()
print("Node unisolated")
```

#### links

```python
node_links = node.links()
```

Get links connected to this node.

##### Returns

- `List[Dict[str, Any]]`: List of links

##### Example

```python
# Get all links for this node
links = node.links()
for link in links:
    print(f"Link ID: {link['link_id']}")
```

### Cisco IOS Specific Methods

#### auto_idlepc

```python
idlepc_result = node.auto_idlepc()
```

Find the best idlepc value (Cisco IOS specific).

##### Returns

- `Dict[str, Any]`: The result including the idlepc value

##### Example

```python
# Find the best idlepc value for a Cisco router
result = node.auto_idlepc()
print(f"Best idlepc value: {result['idlepc']}")
```

#### idlepc_proposals

```python
proposals = node.idlepc_proposals()
```

Get idlepc proposals (Cisco IOS specific).

##### Returns

- `List[str]`: List of idlepc proposals

##### Example

```python
# Get idlepc proposals for a Cisco router
proposals = node.idlepc_proposals()
print("Idlepc proposals:")
for proposal in proposals:
    print(f"- {proposal}")
```

### Disk Image Management

#### create_disk_image

```python
result = node.create_disk_image(disk_path, **kwargs)
```

Create a disk image.

##### Parameters

- `disk_path` (str): Path to the disk image
- `**kwargs`: Additional parameters

##### Returns

- `Dict[str, Any]`: The result

##### Example

```python
# Create a disk image for a QEMU node
result = node.create_disk_image("/hda_disk.qcow2", qemu_img="qcow2")
print(f"Disk image created: {result}")
```

#### update_disk_image

```python
result = node.update_disk_image(disk_path, **kwargs)
```

Update a disk image.

##### Parameters

- `disk_path` (str): Path to the disk image
- `**kwargs`: Additional parameters

##### Returns

- `Dict[str, Any]`: The result

##### Example

```python
# Update a disk image
result = node.update_disk_image("/hda_disk.qcow2", new_path="/updated_disk.qcow2")
print(f"Disk image updated: {result}")
```

#### delete_disk_image

```python
node.delete_disk_image(disk_path)
```

Delete a disk image.

##### Parameters

- `disk_path` (str): Path to the disk image

##### Example

```python
# Delete a disk image
node.delete_disk_image("/hda_disk.qcow2")
print("Disk image deleted")
``` 