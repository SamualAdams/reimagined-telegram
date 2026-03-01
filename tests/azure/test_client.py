"""Tests for Azure Boards client."""

from azure_things.azure.client import AzureBoardsClient


def test_client_initialization():
    """Test client can be initialized."""
    client = AzureBoardsClient("test-org", "test-pat", "test-project")
    assert client.organization == "test-org"
    assert client.project == "test-project"
