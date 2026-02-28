"""Tests for work item categorization."""

from azure_things.utils.mapper import categorize_work_items


def test_categorize_work_items_empty():
    """Test categorization with empty list."""
    result = categorize_work_items([])
    assert "Inbox" in result
    assert "Today" in result
    assert len(result["Inbox"]) == 0


# TODO: Add comprehensive categorization tests in Phase 4
