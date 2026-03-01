"""Main application container and layout."""

import threading
from typing import Dict, List

import flet as ft

from azure_things.azure.client import AzureBoardsClient
from azure_things.azure.models import WorkItem
from azure_things.config import LIST_NAMES
from azure_things.storage.credentials import load_credentials, credentials_exist
from azure_things.utils.mapper import categorize_work_items
from azure_things.ui.sidebar import Sidebar
from azure_things.ui.task_list import TaskList
from azure_things.ui.settings import SettingsDialog
from azure_things.ui.theme import BACKGROUND_COLOR, SURFACE_COLOR, TEXT_SECONDARY_COLOR, TEXT_PRIMARY_COLOR


class AzureThingsApp:
    """Main application container that orchestrates all UI components."""

    def __init__(self, page: ft.Page):
        self.page = page
        self._client = None
        self._work_items: List[WorkItem] = []
        self._categories: Dict[str, List[WorkItem]] = {n: [] for n in LIST_NAMES}
        self._current_list = "Inbox"

        self.sidebar = Sidebar(
            on_list_select=self._handle_list_select,
            on_settings=self._handle_settings,
        )
        self.task_list = TaskList(
            on_complete=self._handle_task_complete,
            on_delete=self._handle_task_delete,
            on_create=self._handle_task_create,
            on_refresh=self._handle_refresh,
        )

    def _show_error(self, msg: str):
        """Show an error message as a banner at the top of the page."""
        error_banner = ft.Container(
            content=ft.Row(
                controls=[
                    ft.Icon(ft.Icons.ERROR_OUTLINE, color=TEXT_PRIMARY_COLOR, size=16),
                    ft.Text(msg, color=TEXT_PRIMARY_COLOR, size=13, expand=True),
                    ft.IconButton(
                        icon=ft.Icons.CLOSE,
                        icon_color=TEXT_PRIMARY_COLOR,
                        icon_size=14,
                        on_click=lambda _: self._dismiss_error(error_banner),
                    ),
                ],
                spacing=8,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
            bgcolor="#FF3B30",
            padding=ft.padding.symmetric(horizontal=16, vertical=8),
            border_radius=8,
            margin=ft.margin.only(left=16, right=16, top=8),
        )
        self.page.overlay.append(error_banner)
        self.page.update()

    def _dismiss_error(self, banner):
        """Remove an error banner."""
        if banner in self.page.overlay:
            self.page.overlay.remove(banner)
            self.page.update()

    def build(self):
        """Build and display the main app layout."""
        self.page.title = "Azure Things"
        self.page.theme_mode = ft.ThemeMode.DARK
        self.page.bgcolor = BACKGROUND_COLOR
        self.page.padding = 0
        self.page.spacing = 0
        self.page.window.width = 1000
        self.page.window.height = 700
        self.page.window.min_width = 700
        self.page.window.min_height = 500

        sidebar_control = self.sidebar.build()
        task_list_control = self.task_list.build()

        layout = ft.Row(
            controls=[
                sidebar_control,
                ft.VerticalDivider(width=1, color=SURFACE_COLOR),
                task_list_control,
            ],
            expand=True,
            spacing=0,
        )

        self.page.add(layout)

        if credentials_exist():
            self._init_client()
            self._load_work_items()
        else:
            self._handle_settings()
            self.task_list.set_items("Inbox", [])

    def _init_client(self):
        """Initialize the Azure Boards client from stored credentials."""
        org, pat, project = load_credentials()
        if org and pat and project:
            self._client = AzureBoardsClient(org, pat, project)

    def _load_work_items(self):
        """Fetch work items from Azure Boards and categorize them."""
        if not self._client:
            return

        def fetch():
            try:
                self._work_items = self._client.query_work_items()
                self._categories = categorize_work_items(self._work_items)
                self.page.run_thread(update_ui)
            except Exception as e:
                error_msg = str(e)
                self.page.run_thread(lambda: self._on_load_error(error_msg))

        def update_ui():
            counts = {name: len(items) for name, items in self._categories.items()}
            self.sidebar.set_counts(counts)
            self.task_list.set_items(
                self._current_list,
                self._categories.get(self._current_list, []),
            )

        thread = threading.Thread(target=fetch, daemon=True)
        thread.start()

    def _on_load_error(self, msg: str):
        """Handle work item load error on the UI thread."""
        self._show_error(f"Error loading work items: {msg}")
        self.task_list.set_items(self._current_list, [])

    def _handle_list_select(self, list_name: str):
        """Handle sidebar list selection."""
        self._current_list = list_name
        self.task_list.set_items(
            list_name,
            self._categories.get(list_name, []),
        )

    def _handle_task_complete(self, work_item: WorkItem):
        """Handle task completion toggle."""
        if not self._client:
            return

        is_done = work_item.state in ("Resolved", "Closed", "Done")
        new_state = "New" if is_done else "Closed"

        def do_update():
            try:
                self._client.update_work_item(
                    work_item.id,
                    {"System.State": new_state},
                )
                self._load_work_items()
            except Exception as e:
                error_msg = str(e)
                self.page.run_thread(lambda: self._show_error(f"Error: {error_msg}"))

        threading.Thread(target=do_update, daemon=True).start()

    def _handle_task_delete(self, work_item: WorkItem):
        """Handle task deletion."""
        if not self._client:
            return

        def do_delete():
            try:
                self._client.update_work_item(
                    work_item.id,
                    {"System.State": "Removed"},
                )
                self._load_work_items()
            except Exception as e:
                error_msg = str(e)
                self.page.run_thread(lambda: self._show_error(f"Error: {error_msg}"))

        threading.Thread(target=do_delete, daemon=True).start()

    def _handle_task_create(self, title: str, current_list: str):
        """Handle new task creation."""
        if not self._client:
            return

        kwargs = {}
        if current_list == "Today":
            kwargs["priority"] = 1
        elif current_list == "Someday":
            kwargs["priority"] = 4

        def do_create():
            try:
                self._client.create_work_item(title, **kwargs)
                self._load_work_items()
            except Exception as e:
                error_msg = str(e)
                self.page.run_thread(lambda: self._show_error(f"Error: {error_msg}"))

        threading.Thread(target=do_create, daemon=True).start()

    def _handle_refresh(self):
        """Handle manual refresh."""
        self._load_work_items()

    def _handle_settings(self):
        """Show the settings dialog."""
        dialog = SettingsDialog(self.page, on_save=self._on_credentials_saved)
        self.page.show_dialog(dialog.build())

    def _on_credentials_saved(self):
        """Handle credential save from settings dialog."""
        self._init_client()
        self._load_work_items()
