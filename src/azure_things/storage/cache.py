"""Local caching for offline support."""

from typing import List, Optional


class WorkItemCache:
    """In-memory cache for work items.

    Provides offline support by caching work items locally.
    Implements Phase 4: Data Mapping.
    """

    def __init__(self):
        """Initialize the cache."""
        self._cache = {}
        # TODO: Implement in Phase 4

    def get(self, work_item_id: int) -> Optional[dict]:
        """Get a cached work item.

        Args:
            work_item_id: Work item ID

        Returns:
            Cached work item or None
        """
        # TODO: Implement in Phase 4
        return self._cache.get(work_item_id)

    def set(self, work_item_id: int, work_item: dict):
        """Cache a work item.

        Args:
            work_item_id: Work item ID
            work_item: Work item data
        """
        # TODO: Implement in Phase 4
        self._cache[work_item_id] = work_item

    def get_all(self) -> List[dict]:
        """Get all cached work items.

        Returns:
            List of all cached work items
        """
        # TODO: Implement in Phase 4
        return list(self._cache.values())

    def clear(self):
        """Clear the cache."""
        self._cache.clear()
