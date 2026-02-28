"""Tests for input validators."""

from azure_things.utils.validators import validate_org_url, validate_pat


def test_validate_org_url():
    """Test organization URL validation."""
    assert validate_org_url("my-org") is True
    assert validate_org_url("") is False
    assert validate_org_url("   ") is False


def test_validate_pat():
    """Test PAT validation."""
    assert validate_pat("a" * 52) is True  # Typical PAT length
    assert validate_pat("short") is False
    assert validate_pat("") is False


# TODO: Add more validation tests in Phase 3
