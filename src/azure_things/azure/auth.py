"""Authentication utilities for Azure Boards API."""

import base64


def get_auth_header(pat: str) -> dict:
    """Generate Basic Auth header for Azure Boards API.

    Args:
        pat: Personal Access Token

    Returns:
        Dictionary with Authorization header
    """
    # TODO: Implement in Phase 2
    # Encode PAT as Base64 for Basic Auth
    # Format: Authorization: Basic :{PAT}
    pass
