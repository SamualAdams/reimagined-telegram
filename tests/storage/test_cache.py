"""Tests for work item cache."""

from azure_things.storage.cache import WorkItemCache


def test_cache_initialization():
    """Test cache can be initialized."""
    cache = WorkItemCache()
    assert cache is not None


def test_cache_operations():
    """Test basic cache operations."""
    cache = WorkItemCache()

    # Test empty cache
    assert cache.get(1) is None
    assert cache.get_all() == []

    # Test set and get
    cache.set(1, {"id": 1, "title": "Test"})
    assert cache.get(1) == {"id": 1, "title": "Test"}

    # Test clear
    cache.clear()
    assert cache.get(1) is None


# TODO: Add more tests in Phase 4
