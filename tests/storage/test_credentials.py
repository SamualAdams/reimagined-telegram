"""Tests for credential loading."""

from azure_things.storage.credentials import load_credentials, credentials_exist


def test_load_credentials():
    """Test credentials can be loaded."""
    org, pat, project = load_credentials()
    assert org is None or isinstance(org, str)
    assert pat is None or isinstance(pat, str)
    assert project is None or isinstance(project, str)


def test_credentials_exist():
    """Test credentials_exist check."""
    result = credentials_exist()
    assert isinstance(result, bool)
