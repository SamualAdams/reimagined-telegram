"""Individual task item component."""

import flet as ft

from azure_things.azure.models import WorkItem
from azure_things.ui.theme import (
    SURFACE_COLOR,
    PRIMARY_COLOR,
    TEXT_PRIMARY_COLOR,
    TEXT_SECONDARY_COLOR,
    HOVER_COLOR,
)


class TaskItem:
    """Individual task row with checkbox and metadata."""

    def __init__(self, work_item: WorkItem, on_complete=None, on_delete=None):
        self.work_item = work_item
        self.on_complete = on_complete
        self.on_delete = on_delete
        self._delete_btn = None

    def _handle_complete(self, e):
        if self.on_complete:
            self.on_complete(self.work_item)

    def _handle_delete(self, e):
        if self.on_delete:
            self.on_delete(self.work_item)

    def _handle_hover(self, e):
        if self._delete_btn:
            self._delete_btn.visible = e.data == "true"
            self._delete_btn.update()

    def build(self) -> ft.Container:
        is_done = self.work_item.state in ("Resolved", "Closed", "Done")

        checkbox = ft.Checkbox(
            value=is_done,
            on_change=self._handle_complete,
        )

        title = ft.Text(
            self.work_item.title,
            color=TEXT_SECONDARY_COLOR if is_done else TEXT_PRIMARY_COLOR,
            size=14,
            expand=True,
            max_lines=1,
            overflow=ft.TextOverflow.ELLIPSIS,
        )

        metadata = []
        if self.work_item.due_date:
            metadata.append(ft.Text(
                self.work_item.due_date.strftime("%b %d"),
                color=TEXT_SECONDARY_COLOR,
                size=12,
            ))

        priority = self.work_item.priority
        if priority and priority <= 2:
            priority_colors = {1: "#FF3B30", 2: "#FF9500"}
            metadata.append(ft.Container(
                content=ft.Text(
                    "!" * (3 - priority),
                    color=priority_colors.get(priority, TEXT_SECONDARY_COLOR),
                    size=12,
                    weight=ft.FontWeight.BOLD,
                ),
            ))

        if self.work_item.work_item_type != "Task":
            metadata.append(ft.Container(
                content=ft.Text(
                    self.work_item.work_item_type,
                    color=TEXT_SECONDARY_COLOR,
                    size=11,
                ),
                bgcolor=HOVER_COLOR,
                border_radius=4,
                padding=ft.padding.symmetric(horizontal=6, vertical=2),
            ))

        self._delete_btn = ft.IconButton(
            icon=ft.Icons.DELETE_OUTLINE,
            icon_color=TEXT_SECONDARY_COLOR,
            icon_size=16,
            on_click=self._handle_delete,
            visible=False,
        )

        row = ft.Row(
            controls=[
                checkbox,
                title,
                *metadata,
                self._delete_btn,
            ],
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=8,
        )

        return ft.Container(
            content=row,
            padding=ft.padding.symmetric(horizontal=12, vertical=4),
            border_radius=8,
            on_hover=self._handle_hover,
        )
