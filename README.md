# GNS3 Client
Library for interacting with GNS3 server.

## Installation

```bash
pip install -U --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple gns3client
```

## Quick Start

```python
from gns3client import GNS3Client
from tabulate import tabulate

# Create a client instance
client = GNS3Client()

projects = client.list_projects()

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

headers = ["Project Name", "Total Nodes", "Total Links", "Status"]
print(tabulate(projects_data, headers=headers, tablefmt="simple"))
"""
Project Name      Total Nodes    Total Links  Status
--------------  -------------  -------------  --------
tt                        2              1   closed
test_pbr                  6              3   opened
"""
```

### another example

```python
from gns3client import GNS3Client
from tabulate import tabulate
import datetime

def print_section(title, width=80):
    print("\n" + "=" * width)
    print(f"{title:^{width}}")
    print("=" * width)

def print_subsection(title, width=80):
    print("\n" + "-" * width)
    print(f"{title:^{width}}")
    print("-" * width)


client = GNS3Client()
projects = client.list_projects()

current_time = datetime.datetime.now().strftime("%Y-%m-%d")
print_section(f"GNS3 NETWORK TOPOLOGY REPORT - {current_time}")

projects_data = []
for project in projects:
    nodes = project.list_nodes()
    links = project.list_links()
    
    projects_data.append([
        project.name,
        project.id,
        len(nodes),
        len(links),
        project.status if hasattr(project, 'status') else "unknown"
    ])

print_subsection("PROJECT SUMMARY")
headers = ["Project Name", "Project ID", "Nodes", "Links", "Status"]
print(tabulate(projects_data, headers=headers, tablefmt="pretty"))

for project in projects:
    nodes = project.list_nodes()
    if nodes:
        print_subsection(f"NODES IN {project.name}")
        nodes_data = []
        for node in nodes:
            nodes_data.append([
                node.name,
                node.node_type if hasattr(node, 'node_type') else "unknown",
                node.status if hasattr(node, 'status') else "unknown",
                node.console if hasattr(node, 'console') else "N/A"
            ])
        
        node_headers = ["Name", "Type", "Status", "Console Port"]
        print(tabulate(nodes_data, headers=node_headers, tablefmt="pretty"))
    

print(f"Total Projects: {len(projects)}")
total_nodes = sum(len(project.list_nodes()) for project in projects)
total_links = sum(len(project.list_links()) for project in projects)
print(f"Total Nodes: {total_nodes}")
print(f"Total Links: {total_links}")
"""
================================================================================
               GNS3 NETWORK TOPOLOGY REPORT - 2025-03-09              
================================================================================

--------------------------------------------------------------------------------
                                PROJECT SUMMARY                                 
--------------------------------------------------------------------------------
+--------------+--------------------------------------+-------+-------+--------+
| Project Name |              Project ID              | Nodes | Links | Status |
+--------------+--------------------------------------+-------+-------+--------+
|     adsf     | 32d1ed61-fee4-4168-b2bb-b6f2cb012404 |   2   |   1   | closed |
|  _new_test   | 75ce2bf9-48de-48c9-aa29-f27b169437a3 |   6   |   3   | opened |
+--------------+--------------------------------------+-------+-------+--------+

--------------------------------------------------------------------------------
                                 NODES IN adsf                                  
--------------------------------------------------------------------------------
+------+------+--------+--------------+
| Name | Type | Status | Console Port |
+------+------+--------+--------------+
| PC1  | vpcs |        |     5000     |
| PC2  | vpcs |        |     5002     |
+------+------+--------+--------------+

--------------------------------------------------------------------------------
                               NODES IN _new_test                               
--------------------------------------------------------------------------------
+----------------+--------+---------+-----------------------+
|      Name      |  Type  | Status  |     Console Port      |
+----------------+--------+---------+-----------------------+
|      PC1       |  vpcs  | stopped |         5000          |
|      PC2       |  vpcs  | stopped |         5002          |
|      PC3       |  vpcs  | stopped |         5004          |
|      PC4       |  vpcs  | stopped |         5006          |
|      PC6       |  vpcs  | stopped |         5010          |
| Ubuntu64-bit-1 | vmware | stopped | <DynamicSchema: None> |
+----------------+--------+---------+-----------------------+
Total Projects: 2
Total Nodes: 8
Total Links: 4
"""
```
