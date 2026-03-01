"""Sidebar navigation component."""

from typing import Optional, Callable, Dict

import flet as ft

from azure_things.config import LIST_NAMES
from azure_things.ui.theme import (
    BACKGROUND_COLOR,
    SIDEBAR_COLOR,
    SURFACE_COLOR,
    PRIMARY_COLOR,
    TEXT_PRIMARY_COLOR,
    TEXT_SECONDARY_COLOR,
    HOVER_COLOR,
)

SIDEBAR_ICONS = {
    "Inbox": ft.Icons.INBOX,
    "Today": ft.Icons.STAR,
    "Upcoming": ft.Icons.CALENDAR_MONTH,
    "Anytime": ft.Icons.ALL_INCLUSIVE,
    "Someday": ft.Icons.CLOUD_QUEUE,
    "Logbook": ft.Icons.BOOK,
    "Trash": ft.Icons.DELETE,
}


class Sidebar:
    """Left sidebar with list navigation and count badges."""

    def __init__(
        self,
        on_list_select: Optional[Callable] = None,
        on_settings: Optional[Callable] = None,
    ):
        self.on_list_select = on_list_select
        self.on_settings = on_settings
        self.selected_list = "Inbox"
        self._counts: Dict[str, int] = {name: 0 for name in LIST_NAMES}
        self._list_containers: Dict[str, ft.Container] = {}
        self._count_texts: Dict[str, ft.Text] = {}

    def set_counts(self, counts: Dict[str, int]):
        """Update item counts for each list."""
        self._counts = counts
        for name, text in self._count_texts.items():
            count = counts.get(name, 0)
            text.value = str(count) if count > 0 else ""
            text.update()

    def select_list(self, name: str):
        """Update the selected list visual state."""
        old = self.selected_list
        self.selected_list = name

        if old in self._list_containers:
            self._list_containers[old].bgcolor = "transparent"
            self._list_containers[old].update()

        if name in self._list_containers:
            self._list_containers[name].bgcolor = SURFACE_COLOR
            self._list_containers[name].update()

    def _handle_list_click(self, name: str):
        def handler(e):
            self.select_list(name)
            if self.on_list_select:
                self.on_list_select(name)
        return handler

    def _build_list_item(self, name: str) -> ft.Container:
        icon = SIDEBAR_ICONS.get(name, ft.Icons.LIST)
        is_selected = name == self.selected_list

        count_text = ft.Text(
            str(self._counts.get(name, 0)) if self._counts.get(name, 0) > 0 else "",
            color=TEXT_SECONDARY_COLOR,
            size=12,
        )
        self._count_texts[name] = count_text

        container = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(icon, color=PRIMARY_COLOR, size=18),
                    ft.Text(name, color=TEXT_PRIMARY_COLOR, size=14, expand=True),
                    count_text,
                ],
                spacing=12,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.padding.symmetric(horizontal=12, vertical=8),
            border_radius=8,
            bgcolor=SURFACE_COLOR if is_selected else "transparent",
            on_click=self._handle_list_click(name),
            ink=True,
        )

        self._list_containers[name] = container
        return container

    def build(self) -> ft.Container:
        title = ft.Text(
            "Azure Things",
            size=16,
            weight=ft.FontWeight.BOLD,
            color=TEXT_PRIMARY_COLOR,
        )

        settings_btn = ft.IconButton(
            icon=ft.Icons.SETTINGS,
            icon_color=TEXT_SECONDARY_COLOR,
            icon_size=18,
            on_click=lambda _: self.on_settings() if self.on_settings else None,
            tooltip="Settings",
        )

        header = ft.Row(
            controls=[title, settings_btn],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        )

        list_items = [self._build_list_item(name) for name in LIST_NAMES]

        return ft.Container(
            content=ft.Column(
                controls=[
                    ft.Container(content=header, padding=ft.padding.only(left=12, right=4, top=12, bottom=8)),
                    ft.Divider(height=1, color=SURFACE_COLOR),
                    *list_items,
                ],
                spacing=2,
            ),
            width=240,
            bgcolor=SIDEBAR_COLOR,
            padding=ft.padding.only(left=8, right=8, top=8, bottom=16),
        )
