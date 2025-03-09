"""
GNS3 client library.

A Python client library for interacting with the GNS3 API.
"""

from gns3client.client import GNS3Client
from gns3client.resources.project import Project
from gns3client.resources.template import Template

__version__ = "0.1.0"
__all__ = [
    'GNS3Client',
    'Project',
    'Template',
]

