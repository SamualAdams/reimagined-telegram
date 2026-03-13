"""Input validation utilities."""


def validate_org_url(org: str) -> bool:
    """Validate Azure DevOps organization name.

    Args:
        org: Organization name

    Returns:
        True if valid, False otherwise
    """
    # TODO: Implement in Phase 3
    # Check for valid organization name format
    if not org or not org.strip():
        return False
    return True


def validate_pat(pat: str) -> bool:
    """Validate Personal Access Token format.

    Args:
        pat: Personal Access Token

    Returns:
        True if valid format, False otherwise
    """
    # TODO: Implement in Phase 3
    # Check for valid PAT format (basic length check)
    if not pat or len(pat) < 20:
        return False
    return True
