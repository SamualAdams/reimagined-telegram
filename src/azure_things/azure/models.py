"""Pydantic models for Azure Boards work items."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class WorkItem(BaseModel):
    """Represents an Azure Boards work item.

    This model will be implemented in Phase 2 with all necessary fields.
    """

    id: int
    title: str
    work_item_type: str
    state: str
    priority: Optional[int] = None
    due_date: Optional[datetime] = None
    created_date: datetime
    # TODO: Add more fields in Phase 2


class WorkItemUpdate(BaseModel):
    """Represents an update to a work item.

    Used for PATCH operations on work items.
    """

    # TODO: Implement in Phase 2
    pass
