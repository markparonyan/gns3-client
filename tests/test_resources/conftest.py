import pytest
from unittest.mock import MagicMock


@pytest.fixture
def mock_client():
    """Mock GNS3Client instance."""
    client = MagicMock()
    client.host = "http://test-host:3080"
    client.access_token = "test-access-token"
    client._get_api.return_value = MagicMock()
    return client


@pytest.fixture
def project_data():
    """Sample project data."""
    return {
        "project_id": "test-project-id",
        "name": "Test Project",
        "status": "opened",
        "path": "/path/to/project",
    }


@pytest.fixture
def node_data():
    """Sample node data."""
    return {
        "node_id": "test-node-id",
        "name": "Test Node",
        "node_type": "vpcs",
        "compute_id": "local",
        "status": "started",
        "console": 5000,
        "console_host": "127.0.0.1",
    }


@pytest.fixture
def link_data():
    """Sample link data."""
    return {
        "link_id": "test-link-id",
        "nodes": [
            {"node_id": "node1", "adapter_number": 0, "port_number": 0},
            {"node_id": "node2", "adapter_number": 0, "port_number": 0},
        ],
        "capturing": False,
        "capture_file_path": "",
        "capture_file_name": "",
    }


@pytest.fixture
def template_data():
    """Sample template data."""
    return {
        "template_id": "test-template-id",
        "name": "Test Template",
        "template_type": "vpcs",
        "compute_id": "local",
    } 