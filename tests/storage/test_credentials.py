"""Tests for credential loading."""

from azure_things.storage.credentials import load_credentials, credentials_exist


def test_load_credentials():
    """Test credentials can be loaded."""
    org, pat = load_credentials()
    # Will be None if no .env file exists
    assert org is None or isinstance(org, str)
    assert pat is None or isinstance(pat, str)


def test_credentials_exist():
    """Test credentials_exist check."""
    result = credentials_exist()
    assert isinstance(result, bool)


# TODO: Add more tests with mocked .env file in Phase 3
