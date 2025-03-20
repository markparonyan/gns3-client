from typing import Dict, Any, Optional
from datetime import datetime


class Snapshot:
    """Represents a GNS3 project snapshot.
    
    This class provides methods for working with a GNS3 project snapshot.
    """
    
    def __init__(self, client, project_id: str, data: Dict[str, Any] = None):
        """Initialize a Snapshot instance.
        
        Args:
            client: The GNS3Client instance
            project_id: The ID of the project
            data: The snapshot data dictionary
        """
        self._client = client
        self._project_id = project_id
        self._data = data or {}

    @property
    def id(self) -> str:
        """Get the snapshot ID.
        
        Returns:
            str: The snapshot ID
        """
        return self._data.get('snapshot_id', '')
    
    @property
    def name(self) -> str:
        """Get the snapshot name.
        
        Returns:
            str: The snapshot name
        """
        return self._data.get('name', '')
    
    @property
    def created_at(self) -> Optional[datetime]:
        """Get the snapshot creation date and time.
        
        Returns:
            datetime: The snapshot creation date and time, or None if not available
        """
        created_at = self._data.get('created_at')
        if created_at:
            try:
                return datetime.fromisoformat(created_at.replace('Z', '+00:00'))
            except (ValueError, TypeError):
                pass
        return None
    
    def restore(self) -> Dict[str, Any]:
        """Restore this snapshot.
        
        Returns:
            Dict[str, Any]: The response data
        """
        from gns3client.api.snapshots import SnapshotsAPI
        
        return self._client._get_api(SnapshotsAPI).restore(
            self._client.access_token, 
            self._project_id, 
            self.id
        )
    
    def __repr__(self) -> str:
        """String representation of the snapshot.
        
        Returns:
            str: String representation
        """
        return f"<Snapshot id={self.id} name={self.name}>" 