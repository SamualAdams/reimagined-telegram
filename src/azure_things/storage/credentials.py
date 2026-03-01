"""Credential loading from .env file."""

import os
from typing import Optional, Tuple
from dotenv import load_dotenv


def load_credentials() -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """Load Azure credentials from .env file.

    Returns:
        Tuple of (organization, pat, project) or Nones if not found
    """
    load_dotenv()

    org = os.getenv("AZURE_DEVOPS_ORG")
    pat = os.getenv("AZURE_DEVOPS_PAT")
    project = os.getenv("AZURE_DEVOPS_PROJECT")

    return org, pat, project


def credentials_exist() -> bool:
    """Check if credentials are configured in .env file.

    Returns:
        True if org, PAT, and project are set, False otherwise
    """
    org, pat, project = load_credentials()
    return all(v is not None for v in (org, pat, project))
