"""Tests for Azure Boards client."""

import pytest
from azure_things.azure.client import AzureBoardsClient


def test_client_initialization():
    """Test client can be initialized."""
    client = AzureBoardsClient("test-org", "test-pat")
    assert client.organization == "test-org"
    assert client.pat == "test-pat"


# TODO: Add more tests in Phase 2
