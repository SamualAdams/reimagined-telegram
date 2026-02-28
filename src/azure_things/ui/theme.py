"""Dark theme configuration matching Things app."""

import flet as ft
from azure_things.config import COLORS


def get_theme() -> ft.Theme:
    """Get the Things app-style dark theme.

    Returns:
        Flet Theme object
    """
    # TODO: Implement complete theme in Phase 5
    return ft.Theme(
        color_scheme_seed=COLORS["primary"],
    )


# Export color constants for use in components
BACKGROUND_COLOR = COLORS["background"]
SURFACE_COLOR = COLORS["surface"]
PRIMARY_COLOR = COLORS["primary"]
TEXT_PRIMARY_COLOR = COLORS["text_primary"]
TEXT_SECONDARY_COLOR = COLORS["text_secondary"]
