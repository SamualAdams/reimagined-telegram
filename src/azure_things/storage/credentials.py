"""Credential loading from .env file."""

import os
from typing import Optional, Tuple
from dotenv import load_dotenv


def load_credentials() -> Tuple[Optional[str], Optional[str]]:
    """Load Azure credentials from .env file.

    Loads AZURE_DEVOPS_ORG and AZURE_DEVOPS_PAT from .env file.
    Implements Phase 3: Credential Storage.

    Returns:
        Tuple of (organization, pat) or (None, None) if not found
    """
    load_dotenv()

    org = os.getenv("AZURE_DEVOPS_ORG")
    pat = os.getenv("AZURE_DEVOPS_PAT")

    return org, pat


def credentials_exist() -> bool:
    """Check if credentials are configured in .env file.

    Returns:
        True if both org and PAT are set, False otherwise
    """
    org, pat = load_credentials()
    return org is not None and pat is not None
