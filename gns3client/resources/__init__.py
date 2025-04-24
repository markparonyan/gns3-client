"""
Resource classes for the GNS3 client.

These classes provide a simple, intuitive interface to GNS3 resources.
"""

from gns3client.resources.project import Project
from gns3client.resources.template import Template
from gns3client.resources.node import Node
from gns3client.resources.link import Link
from gns3client.resources.snapshot import Snapshot

__all__ = [
    'Project',
    'Template',
    'Node',
    'Link',
    'Snapshot',
] 