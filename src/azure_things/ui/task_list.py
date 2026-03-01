"""Task list view component."""

from typing import List, Optional, Callable

import flet as ft

from azure_things.azure.models import WorkItem
from azure_things.ui.task_item import TaskItem
from azure_things.ui.theme import (
    BACKGROUND_COLOR,
    PRIMARY_COLOR,
    TEXT_PRIMARY_COLOR,
    TEXT_SECONDARY_COLOR,
    SURFACE_COLOR,
)


class TaskList:
    """Main content area displaying filtered work items."""

    def __init__(
        self,
        on_complete: Optional[Callable] = None,
        on_delete: Optional[Callable] = None,
        on_create: Optional[Callable] = None,
        on_refresh: Optional[Callable] = None,
    ):
        self.on_complete = on_complete
        self.on_delete = on_delete
        self.on_create = on_create
        self.on_refresh = on_refresh
        self._current_list = "Inbox"
        self._header_text = ft.Text(
            "Inbox",
            size=24,
            weight=ft.FontWeight.BOLD,
            color=TEXT_PRIMARY_COLOR,
        )
        self._count_text = ft.Text(
            "0 items",
            size=14,
            color=TEXT_SECONDARY_COLOR,
        )
        self._items_column = ft.Column(
            controls=[],
            spacing=2,
            scroll=ft.ScrollMode.AUTO,
            expand=True,
        )
        self._new_task_field = ft.TextField(
            hint_text="New Task",
            hint_style=ft.TextStyle(color=TEXT_SECONDARY_COLOR),
            border_color="transparent",
            focused_border_color=PRIMARY_COLOR,
            color=TEXT_PRIMARY_COLOR,
            cursor_color=PRIMARY_COLOR,
            text_size=14,
            on_submit=self._handle_create,
            expand=True,
        )
        self._empty_text = ft.Container(
            content=ft.Column(
                controls=[
                    ft.Icon(ft.Icons.CHECK_CIRCLE_OUTLINE, color=TEXT_SECONDARY_COLOR, size=48),
                    ft.Text("No items", color=TEXT_SECONDARY_COLOR, size=16),
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                alignment=ft.MainAxisAlignment.CENTER,
                spacing=12,
            ),
            expand=True,
            alignment=ft.Alignment(0, 0),
        )
        self._container = None

    def set_items(self, list_name: str, items: List[WorkItem]):
        """Update the displayed items."""
        self._current_list = list_name
        self._header_text.value = list_name
        self._count_text.value = f"{len(items)} item{'s' if len(items) != 1 else ''}"

        task_controls = [
            TaskItem(
                item,
                on_complete=self.on_complete,
                on_delete=self.on_delete,
            ).build()
            for item in items
        ]

        self._items_column.controls = task_controls if task_controls else [self._empty_text]

        if self._container:
            self._container.update()

    def _handle_create(self, e):
        title = self._new_task_field.value
        if title and title.strip() and self.on_create:
            self.on_create(title.strip(), self._current_list)
            self._new_task_field.value = ""
            self._new_task_field.update()

    def build(self) -> ft.Container:
        refresh_btn = ft.IconButton(
            icon=ft.Icons.REFRESH,
            icon_color=TEXT_SECONDARY_COLOR,
            icon_size=20,
            on_click=lambda _: self.on_refresh() if self.on_refresh else None,
            tooltip="Refresh",
        )

        header = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Column(
                        controls=[self._header_text, self._count_text],
                        spacing=2,
                    ),
                    refresh_btn,
                ],
                alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                vertical_alignment=ft.CrossAxisAlignment.START,
            ),
            padding=ft.padding.only(left=24, right=16, top=20, bottom=12),
        )

        new_task_row = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.ADD, color=PRIMARY_COLOR, size=20),
                    self._new_task_field,
                ],
                spacing=8,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            padding=ft.padding.symmetric(horizontal=16, vertical=8),
            border=ft.border.only(top=ft.BorderSide(1, SURFACE_COLOR)),
        )

        self._container = ft.Container(
            content=ft.Column(
                controls=[
                    header,
                    ft.Container(content=self._items_column, expand=True, padding=ft.padding.symmetric(horizontal=8)),
                    new_task_row,
                ],
                spacing=0,
                expand=True,
            ),
            bgcolor=BACKGROUND_COLOR,
            expand=True,
        )

        return self._container
