"""Tests for theme configuration."""

from azure_things.ui.theme import (
    get_theme,
    BACKGROUND_COLOR,
    PRIMARY_COLOR,
)


def test_theme_colors():
    """Test theme colors are defined."""
    assert BACKGROUND_COLOR == "#1C1C1E"
    assert PRIMARY_COLOR == "#3478F6"


def test_get_theme():
    """Test theme can be created."""
    theme = get_theme()
    assert theme is not None
