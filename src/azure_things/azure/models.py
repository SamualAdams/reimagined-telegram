"""Pydantic models for Azure Boards work items."""

from datetime import datetime
from typing import Optional
from pydantic import BaseModel


class WorkItem(BaseModel):
    """Represents an Azure Boards work item."""

    id: int
    title: str
    work_item_type: str
    state: str
    priority: Optional[int] = None
    due_date: Optional[datetime] = None
    created_date: datetime
    tags: list[str] = []
    assigned_to: Optional[str] = None
    description: Optional[str] = None


class WorkItemUpdate(BaseModel):
    """Represents an update to a work item for PATCH operations."""

    title: Optional[str] = None
    state: Optional[str] = None
    priority: Optional[int] = None
    due_date: Optional[datetime] = None
    tags: Optional[list[str]] = None
