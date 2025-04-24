# GNS3 Client

### Installation

```bash
pip install -U --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple gns3client
```

### Simple Example

Connect to a GNS3 server and list existing projects:

```python
from gns3client import GNS3Client

# Connect to the GNS3 server (defaults to localhost:3080)
client = GNS3Client()

# List all projects
projects = client.list_projects()
for project in projects:
    print(f"Project: {project.name} ({project.id})")
    print(f"Status: {project.status}")
```

### More Complex Example

Create a project with two connected VPCS nodes:

```python
from gns3client import GNS3Client

# Connect to GNS3 server
client = GNS3Client()

# Create a new project
project = client.create_project("Two-Node-Network")

# Create two VPCS nodes
pc1 = project.create_node(name="PC1", node_type="vpcs")
pc2 = project.create_node(name="PC2", node_type="vpcs")

# Create a link between the nodes
link = project.create_link(
    node_a=pc1, 
    port_a=0,  # First Ethernet port 
    node_b=pc2,
    port_b=0   # First Ethernet port
)

# Start the nodes
pc1.start()
pc2.start()

print(f"Created project '{project.name}' with 2 nodes and 1 link")
print(f"Access PC1 console at port {pc1.console}")
print(f"Access PC2 console at port {pc2.console}")
```

### Network Inventory Report Example

Generate a comprehensive report of your GNS3 environment:

```python
from gns3client import GNS3Client
from tabulate import tabulate
import datetime

def print_section(title, width=80):
    print("\n" + "=" * width)
    print(f"{title:^{width}}")
    print("=" * width)

client = GNS3Client()
projects = client.list_projects()

current_time = datetime.datetime.now().strftime("%Y-%m-%d")
print_section(f"GNS3 NETWORK TOPOLOGY REPORT - {current_time}")

# Summarize projects
projects_data = []
for project in projects:
    nodes = project.list_nodes()
    links = project.list_links()
    
    projects_data.append([
        project.name,
        len(nodes),
        len(links),
        project.status
    ])

headers = ["Project Name", "Nodes", "Links", "Status"]
print(tabulate(projects_data, headers=headers, tablefmt="pretty"))

# Show total inventory
print(f"\nTotal Projects: {len(projects)}")
print(f"Total Nodes: {sum(len(project.list_nodes()) for project in projects)}")
print(f"Total Links: {sum(len(project.list_links()) for project in projects)}")
```

## Documentation

For complete documentation, visit the [GNS3 Client Documentation](https://markparonyan.github.io/gns3-client/).

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.
