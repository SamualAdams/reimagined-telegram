"""Main entry point for Azure Things application."""

import flet as ft

from azure_things.ui.app import AzureThingsApp


def _app_main(page: ft.Page):
    """Initialize and build the application."""
    app = AzureThingsApp(page)
    app.build()


def main():
    """Launch the Azure Things application."""
    ft.app(target=_app_main)


if __name__ == "__main__":
    main()
