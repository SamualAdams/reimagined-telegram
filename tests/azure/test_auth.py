"""Tests for authentication utilities."""

import base64

from azure_things.azure.auth import get_auth_header


def test_get_auth_header():
    """Test auth header is properly formatted."""
    header = get_auth_header("test-pat")
    expected = base64.b64encode(b":test-pat").decode()
    assert header == {"Authorization": f"Basic {expected}"}
