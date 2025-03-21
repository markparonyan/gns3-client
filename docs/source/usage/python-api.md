# Python API Reference

This guide provides more advanced examples for working with the GNS3 Client Python API.

## GNS3Client Advanced Usage

### Error Handling

It's important to handle errors properly when interacting with the GNS3 server:

```python
from gns3client import GNS3Client

try:
    client = GNS3Client(host="http://localhost:3080")
    client.version()
except Exception as e:
    print(f"Error connecting to GNS3 server: {e}")
```

### Authentication

For servers with authentication, you can either provide credentials during initialization or login later:

```python
# Option 1: During initialization
client = GNS3Client(
    host="http://localhost:3080",
    username="admin",
    password="admin"
)

# Option 2: Login after initialization
client = GNS3Client(host="http://localhost:3080")
try:
    client.login(username="admin", password="admin")
    print("Successfully authenticated")
except ValueError:
    print("Authentication failed")
```

## Project Management

### Project Properties

Projects have several properties you can access:

```python
project = client.get_project("My Project")
print(f"Project name: {project.name}")
print(f"Project ID: {project.id}")
print(f"Project status: {project.status}")
print(f"Project path: {project.path}")
```

### Import/Export Projects

Import a project from a file:

```python
with open("network_project.gns3project", "rb") as f:
    project_data = f.read()
    
new_project = client.import_project(project_data, name="Imported Project")
```

## Working with Nodes

### Advanced Node Creation

Create different types of nodes with specific configurations:

```python
# Create a Cisco IOSv router
router = project.create_node(
    name="R1",
    node_type="qemu",
    compute_id="local",
    properties={
        "template_id": "iosv-template-id"
    }
)

# Create a Linux container
container = project.create_node(
    name="Ubuntu",
    node_type="docker",
    compute_id="local",
    properties={
        "image": "ubuntu:latest"
    }
)
```

### Working with Node Files

Access and modify files on nodes:

```python
# Get file contents from a node
config = node.get_file("/etc/network/interfaces")
print(config)

# Write to a file on a node
new_config = "auto eth0\niface eth0 inet dhcp\n"
node.post_file("/etc/network/interfaces", new_config)
```

### Node Duplication

Create a copy of an existing node:

```python
# Duplicate a node
node_copy = node.duplicate()
print(f"Created duplicate node: {node_copy.name}")
```

## Working with Links

### Advanced Link Operations

Create links with specific settings:

```python
# Create a link with filters
link = project.create_link([
    {
        "node_id": router1.id,
        "adapter_number": 0,
        "port_number": 0
    },
    {
        "node_id": router2.id,
        "adapter_number": 0,
        "port_number": 0,
        "label": {
            "text": "WAN Link",
            "style": "font-size: 12px; font-weight: bold;"
        }
    }
])

# Reset a link (simulate disconnect/reconnect)
link.reset()
```

### Packet Capture Analysis

```python
import subprocess
import tempfile

# Start capture on a link
link.start_capture()

# ... allow some traffic to flow ...

# Get capture and analyze with tshark (if installed)
capture_data = link.get_capture_stream()
with tempfile.NamedTemporaryFile(delete=False, suffix='.pcap') as f:
    f.write(capture_data)
    pcap_file = f.name

try:
    # Call tshark to analyze the capture file
    output = subprocess.check_output(
        ["tshark", "-r", pcap_file, "-T", "fields", "-e", "ip.src", "-e", "ip.dst"],
        universal_newlines=True
    )
    print("Traffic summary:")
    print(output)
except Exception as e:
    print(f"Failed to analyze capture: {e}")
finally:
    # Stop capture
    link.stop_capture()
```

## Working with Snapshots

Snapshots allow you to save and restore the state of a project:

```python
# Create a snapshot
snapshot = project.create_snapshot("Before configuration")
print(f"Created snapshot: {snapshot.name}")

# List snapshots
snapshots = project.list_snapshots()
for snapshot in snapshots:
    print(f"Snapshot: {snapshot.name}, Created: {snapshot.created_at}")

# Restore a snapshot
project.restore_snapshot(snapshot.id)
```

## Bulk Operations

Perform operations on multiple nodes at once:

```python
# Start all nodes in a project
project.start_all()

# Get all routers in a project
routers = [node for node in project.list_nodes() if "router" in node.name.lower()]

# Perform an operation on all routers
for router in routers:
    router.start()
    print(f"Started router: {router.name}")
```

## Real-world Examples

### Create a Basic Network Topology

This example creates a simple topology with two routers connected by a link:

```python
# Create a new project
project = client.create_project("Router Network")

# Create two routers
router1 = project.create_node(
    name="Router1",
    node_type="dynamips",
    properties={
        "platform": "c7200",
        "image": "c7200-adventerprisek9-mz.152-4.S6.image"
    }
)

router2 = project.create_node(
    name="Router2",
    node_type="dynamips",
    properties={
        "platform": "c7200",
        "image": "c7200-adventerprisek9-mz.152-4.S6.image"
    }
)

# Connect the routers
link = project.create_link([
    {
        "node_id": router1.id,
        "adapter_number": 0,
        "port_number": 0
    },
    {
        "node_id": router2.id,
        "adapter_number": 0,
        "port_number": 0
    }
])

# Start the routers
router1.start()
router2.start()

print(f"Router1 console port: {router1.console}")
print(f"Router2 console port: {router2.console}")
```

### Network Automation Script

This example shows how to automatically configure IP addresses on connected devices:

```python
# Configure IP addresses on the routers
router1_config = """
interface FastEthernet0/0
 ip address 192.168.1.1 255.255.255.0
 no shutdown
exit
"""

router2_config = """
interface FastEthernet0/0
 ip address 192.168.1.2 255.255.255.0
 no shutdown
exit
"""

# Assuming the routers are already created and started
router1.post_file("/startup-config", router1_config)
router2.post_file("/startup-config", router2_config)

# Reload the routers to apply the configuration
router1.reload()
router2.reload()
``` 