"""Azure Boards API client for work item operations."""

from typing import List, Optional


class AzureBoardsClient:
    """Client for interacting with Azure Boards REST API.

    This class will handle all CRUD operations for work items.
    Implements Phase 2: Azure Integration.
    """

    def __init__(self, organization: str, pat: str):
        """Initialize the Azure Boards client.

        Args:
            organization: Azure DevOps organization name
            pat: Personal Access Token for authentication
        """
        self.organization = organization
        self.pat = pat
        # TODO: Implement authentication in Phase 2

    def get_work_items(self, ids: Optional[List[int]] = None):
        """Fetch work items from Azure Boards.

        Args:
            ids: Optional list of work item IDs to fetch

        Returns:
            List of work items
        """
        # TODO: Implement in Phase 2
        pass

    def create_work_item(self, title: str, work_item_type: str = "Task"):
        """Create a new work item.

        Args:
            title: Work item title
            work_item_type: Type of work item (Task, Bug, etc.)

        Returns:
            Created work item
        """
        # TODO: Implement in Phase 2
        pass

    def update_work_item(self, work_item_id: int, fields: dict):
        """Update an existing work item.

        Args:
            work_item_id: ID of work item to update
            fields: Dictionary of fields to update

        Returns:
            Updated work item
        """
        # TODO: Implement in Phase 2
        pass

    def delete_work_item(self, work_item_id: int):
        """Delete a work item.

        Args:
            work_item_id: ID of work item to delete
        """
        # TODO: Implement in Phase 2
        pass
