"""Tests for work item categorization."""

from datetime import datetime, timezone

from azure_things.azure.models import WorkItem
from azure_things.utils.mapper import categorize_work_items


def _make_item(**kwargs) -> WorkItem:
    defaults = {
        "id": 1,
        "title": "Test",
        "work_item_type": "Task",
        "state": "New",
        "created_date": datetime.now(timezone.utc),
    }
    defaults.update(kwargs)
    return WorkItem(**defaults)


def test_categorize_work_items_empty():
    """Test categorization with empty list."""
    result = categorize_work_items([])
    assert "Inbox" in result
    assert "Today" in result
    assert len(result["Inbox"]) == 0


def test_inbox_new_no_due_date():
    """Test new items without due dates go to Inbox."""
    item = _make_item(state="New")
    result = categorize_work_items([item])
    assert len(result["Inbox"]) == 1


def test_logbook_closed():
    """Test closed items go to Logbook."""
    item = _make_item(state="Closed")
    result = categorize_work_items([item])
    assert len(result["Logbook"]) == 1


def test_today_priority_1():
    """Test priority 1 items go to Today."""
    item = _make_item(state="Active", priority=1)
    result = categorize_work_items([item])
    assert len(result["Today"]) == 1


def test_someday_priority_4():
    """Test priority 4 items go to Someday."""
    item = _make_item(state="Active", priority=4)
    result = categorize_work_items([item])
    assert len(result["Someday"]) == 1
