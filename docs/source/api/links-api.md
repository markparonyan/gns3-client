# Link API Reference

The `Link` class represents a GNS3 link between nodes in a project. It provides methods for managing the link and capturing packets.

## Class: Link

```python
from gns3client import GNS3Client
# Link objects are created by the Project class
client = GNS3Client()
project = client.get_project("My Project")
link = project.get_link("link-id-here")
```

### Properties

#### id

```python
link_id = link.id
```

Get the link ID.

##### Returns

- `str`: The link ID

##### Example

```python
print(f"Link ID: {link.id}")
```

#### nodes

```python
link_nodes = link.nodes
```

Get the nodes connected by this link.

##### Returns

- `List[Dict[str, Any]]`: List of node connection information

##### Example

```python
print(f"Link connects {len(link.nodes)} nodes:")
for node_conn in link.nodes:
    print(f"Node ID: {node_conn['node_id']}, Adapter: {node_conn['adapter_number']}, Port: {node_conn['port_number']}")
```

#### capturing

```python
is_capturing = link.capturing
```

Check if packet capturing is enabled on this link.

##### Returns

- `bool`: True if packet capturing is enabled

##### Example

```python
if link.capturing:
    print("Packet capture is active")
else:
    print("No active packet capture")
```

#### capture_file_path

```python
file_path = link.capture_file_path
```

Get the path to the packet capture file.

##### Returns

- `str`: The path to the packet capture file on the server

##### Example

```python
if link.capturing:
    print(f"Capture file path: {link.capture_file_path}")
```

#### capture_file_name

```python
file_name = link.capture_file_name
```

Get the name of the packet capture file.

##### Returns

- `str`: The name of the packet capture file

##### Example

```python
if link.capturing:
    print(f"Capture file name: {link.capture_file_name}")
```

### Link Management Methods

#### refresh

```python
link = link.refresh()
```

Refresh the link data from the server.

##### Returns

- `Link`: The updated link instance

##### Example

```python
# Refresh link data
link = link.refresh()
print(f"Capturing status: {link.capturing}")
```

#### update

```python
link = link.update(**kwargs)
```

Update the link properties.

##### Parameters

- `**kwargs`: Link attributes to update

##### Returns

- `Link`: The updated link instance

##### Example

```python
# Update link filters
link = link.update(filters={"latency": [10]})
print("Link updated with latency filter")
```

#### reset

```python
link = link.reset()
```

Reset the link (simulate disconnect/reconnect).

##### Returns

- `Link`: The updated link instance

##### Example

```python
# Reset a link
link = link.reset()
print("Link reset")
```

### Packet Capture Methods

#### start_capture

```python
link = link.start_capture(capture_file_name=None, data_link_type="DLT_EN10MB")
```

Start packet capturing on the link.

##### Parameters

- `capture_file_name` (str, optional): Optional name for the capture file
- `data_link_type` (str, optional): The data link type (default: "DLT_EN10MB")

##### Returns

- `Link`: The updated link instance

##### Example

```python
# Start packet capture with default settings
link = link.start_capture()
print(f"Capture started: {link.capture_file_path}")

# Start capture with custom file name
link = link.start_capture(capture_file_name="custom_capture.pcap")
print(f"Capture started: {link.capture_file_name}")
```

#### stop_capture

```python
link = link.stop_capture()
```

Stop packet capturing on the link.

##### Returns

- `Link`: The updated link instance

##### Example

```python
# Stop packet capture
link = link.stop_capture()
print("Packet capture stopped")
```

#### get_capture_stream

```python
capture_data = link.get_capture_stream()
```

Get the packet capture stream.

##### Returns

- `bytes`: The packet capture stream data

##### Example

```python
# Get capture data and save to file
if link.capturing:
    capture_data = link.get_capture_stream()
    with open("capture.pcap", "wb") as f:
        f.write(capture_data)
    print(f"Saved capture to capture.pcap ({len(capture_data)} bytes)")
```

#### get_available_filters

```python
filters = link.get_available_filters()
```

Get available packet filters for the link.

##### Returns

- `List[str]`: List of available packet filters

##### Example

```python
# Get available filters
filters = link.get_available_filters()
print("Available filters:")
for filter_name in filters:
    print(f"- {filter_name}")
```

### Example: Complete Packet Capture Workflow

```python
from gns3client import GNS3Client
import time

# Connect to GNS3 server
client = GNS3Client()

# Get a project
project = client.get_project("My Network")

# Create nodes and link if needed
router1 = project.create_node(name="Router1", node_type="vpcs")
router2 = project.create_node(name="Router2", node_type="vpcs")

# Start nodes
router1.start()
router2.start()

# Create a link between them
link = project.create_link([
    {"node_id": router1.id, "adapter_number": 0, "port_number": 0},
    {"node_id": router2.id, "adapter_number": 0, "port_number": 0}
])

# Start packet capture
link.start_capture(capture_file_name="test_capture.pcap")
print(f"Capture started: {link.capture_file_name}")

# Wait for some traffic to flow
time.sleep(30)

# Get the capture data
capture_data = link.get_capture_stream()
with open("capture.pcap", "wb") as f:
    f.write(capture_data)
print(f"Saved {len(capture_data)} bytes to capture.pcap")

# Stop the capture
link.stop_capture()
print("Capture stopped")
``` 