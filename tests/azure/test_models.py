"""Tests for Pydantic models."""

from datetime import datetime
from azure_things.azure.models import WorkItem


def test_work_item_model():
    """Test WorkItem model can be instantiated."""
    work_item = WorkItem(
        id=1,
        title="Test task",
        work_item_type="Task",
        state="New",
        created_date=datetime.now(),
    )
    assert work_item.id == 1
    assert work_item.title == "Test task"


# TODO: Add more tests in Phase 2
