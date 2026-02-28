"""Tests for configuration module."""

from azure_things.config import API_VERSION, COLORS, LIST_NAMES


def test_api_version():
    """Test API version is set correctly."""
    assert API_VERSION == "7.1"


def test_colors_defined():
    """Test all required colors are defined."""
    assert "background" in COLORS
    assert "surface" in COLORS
    assert "primary" in COLORS


def test_list_names():
    """Test all seven list names are defined."""
    assert len(LIST_NAMES) == 7
    assert "Inbox" in LIST_NAMES
    assert "Today" in LIST_NAMES
