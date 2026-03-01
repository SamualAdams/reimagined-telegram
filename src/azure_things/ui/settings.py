"""Settings dialog for credential management."""

from pathlib import Path
from typing import Optional, Callable

import flet as ft

from azure_things.storage.credentials import load_credentials
from azure_things.utils.validators import validate_org_url, validate_pat
from azure_things.ui.theme import SURFACE_COLOR, TEXT_PRIMARY_COLOR, TEXT_SECONDARY_COLOR, PRIMARY_COLOR


class SettingsDialog:
    """Settings dialog for Azure credentials."""

    def __init__(self, page: ft.Page, on_save: Optional[Callable] = None):
        self.page = page
        self.on_save = on_save

        org, pat, project = load_credentials()

        self._org_field = ft.TextField(
            label="Organization",
            value=org or "",
            color=TEXT_PRIMARY_COLOR,
            label_style=ft.TextStyle(color=TEXT_SECONDARY_COLOR),
            border_color=TEXT_SECONDARY_COLOR,
            focused_border_color=PRIMARY_COLOR,
            cursor_color=PRIMARY_COLOR,
        )
        self._pat_field = ft.TextField(
            label="Personal Access Token",
            value=pat or "",
            password=True,
            can_reveal_password=True,
            color=TEXT_PRIMARY_COLOR,
            label_style=ft.TextStyle(color=TEXT_SECONDARY_COLOR),
            border_color=TEXT_SECONDARY_COLOR,
            focused_border_color=PRIMARY_COLOR,
            cursor_color=PRIMARY_COLOR,
        )
        self._project_field = ft.TextField(
            label="Project",
            value=project or "",
            color=TEXT_PRIMARY_COLOR,
            label_style=ft.TextStyle(color=TEXT_SECONDARY_COLOR),
            border_color=TEXT_SECONDARY_COLOR,
            focused_border_color=PRIMARY_COLOR,
            cursor_color=PRIMARY_COLOR,
        )
        self._status_text = ft.Text("", color="#FF3B30", size=12)

    def save_credentials(self, org: str, pat: str, project: str):
        """Save credentials to .env file."""
        env_path = Path(".env")
        env_path.write_text(
            f"# Azure DevOps Configuration\n"
            f"AZURE_DEVOPS_ORG={org}\n"
            f"AZURE_DEVOPS_PAT={pat}\n"
            f"AZURE_DEVOPS_PROJECT={project}\n"
        )

    def _handle_save(self, e):
        org = self._org_field.value.strip()
        pat = self._pat_field.value.strip()
        project = self._project_field.value.strip()

        if not validate_org_url(org):
            self._status_text.value = "Organization name is required."
            self._status_text.update()
            return

        if not validate_pat(pat):
            self._status_text.value = "PAT must be at least 20 characters."
            self._status_text.update()
            return

        if not project:
            self._status_text.value = "Project name is required."
            self._status_text.update()
            return

        self.save_credentials(org, pat, project)
        self.page.close(self._dialog)
        if self.on_save:
            self.on_save()

    def _handle_cancel(self, e):
        self.page.close(self._dialog)

    def build(self) -> ft.AlertDialog:
        self._dialog = ft.AlertDialog(
            modal=True,
            title=ft.Text("Azure DevOps Settings", color=TEXT_PRIMARY_COLOR),
            content=ft.Column(
                controls=[
                    ft.Text(
                        "Enter your Azure DevOps credentials.",
                        color=TEXT_SECONDARY_COLOR,
                        size=13,
                    ),
                    self._org_field,
                    self._project_field,
                    self._pat_field,
                    self._status_text,
                ],
                tight=True,
                spacing=16,
                width=400,
            ),
            actions=[
                ft.TextButton("Cancel", on_click=self._handle_cancel),
                ft.FilledButton("Save", on_click=self._handle_save),
            ],
            bgcolor=SURFACE_COLOR,
        )
        return self._dialog
