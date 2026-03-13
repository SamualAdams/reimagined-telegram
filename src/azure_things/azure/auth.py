"""Authentication utilities for Azure Boards API."""

import base64


def get_auth_header(pat: str) -> dict:
    """Generate Basic Auth header for Azure Boards API.

    Args:
        pat: Personal Access Token

    Returns:
        Dictionary with Authorization header
    """
    encoded = base64.b64encode(f":{pat}".encode()).decode()
    return {"Authorization": f"Basic {encoded}"}
