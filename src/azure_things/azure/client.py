"""Azure Boards API client for work item operations."""

from datetime import datetime
from typing import List, Optional
from urllib.parse import quote

import requests

from azure_things.azure.auth import get_auth_header
from azure_things.azure.models import WorkItem
from azure_things.config import API_VERSION


class AzureBoardsClient:
    """Client for interacting with Azure Boards REST API."""

    def __init__(self, organization: str, pat: str, project: str):
        """Initialize the Azure Boards client.

        Args:
            organization: Azure DevOps organization name
            pat: Personal Access Token for authentication
            project: Azure DevOps project name
        """
        self.organization = organization
        self.project = project
        self.headers = get_auth_header(pat)
        self.base_url = f"https://dev.azure.com/{quote(organization)}/{quote(project)}/_apis"

    def query_work_items(self, wiql: Optional[str] = None) -> List[WorkItem]:
        """Query work items using WIQL.

        Args:
            wiql: WIQL query string. If None, fetches all assigned work items.

        Returns:
            List of WorkItem objects
        """
        if wiql is None:
            wiql = (
                "SELECT [System.Id] FROM WorkItems "
                "WHERE [System.TeamProject] = @project "
                "AND [System.State] <> '' "
                "ORDER BY [System.ChangedDate] DESC"
            )

        url = f"{self.base_url}/wit/wiql?api-version={API_VERSION}"
        response = requests.post(
            url,
            json={"query": wiql},
            headers=self.headers,
        )
        response.raise_for_status()

        work_item_refs = response.json().get("workItems", [])
        if not work_item_refs:
            return []

        ids = [ref["id"] for ref in work_item_refs[:200]]
        return self.get_work_items(ids)

    def get_work_items(self, ids: List[int]) -> List[WorkItem]:
        """Fetch work items by IDs.

        Args:
            ids: List of work item IDs to fetch

        Returns:
            List of WorkItem objects
        """
        if not ids:
            return []

        ids_str = ",".join(str(i) for i in ids)
        fields = (
            "System.Id,System.Title,System.WorkItemType,System.State,"
            "Microsoft.VSTS.Common.Priority,Microsoft.VSTS.Scheduling.DueDate,"
            "System.CreatedDate,System.Tags,System.AssignedTo,System.Description"
        )
        url = (
            f"{self.base_url}/wit/workitems"
            f"?ids={ids_str}&fields={fields}&api-version={API_VERSION}"
        )
        response = requests.get(url, headers=self.headers)
        response.raise_for_status()

        items = []
        for raw in response.json().get("value", []):
            fields_data = raw.get("fields", {})
            tags_str = fields_data.get("System.Tags", "")
            tags = [t.strip() for t in tags_str.split(";") if t.strip()] if tags_str else []

            due_date_str = fields_data.get("Microsoft.VSTS.Scheduling.DueDate")
            due_date = None
            if due_date_str:
                due_date = datetime.fromisoformat(due_date_str.replace("Z", "+00:00"))

            created_str = fields_data.get("System.CreatedDate", "")
            created_date = datetime.fromisoformat(created_str.replace("Z", "+00:00"))

            assigned_to = None
            assigned_raw = fields_data.get("System.AssignedTo")
            if isinstance(assigned_raw, dict):
                assigned_to = assigned_raw.get("displayName")
            elif isinstance(assigned_raw, str):
                assigned_to = assigned_raw

            item = WorkItem(
                id=raw["id"],
                title=fields_data.get("System.Title", ""),
                work_item_type=fields_data.get("System.WorkItemType", "Task"),
                state=fields_data.get("System.State", "New"),
                priority=fields_data.get("Microsoft.VSTS.Common.Priority"),
                due_date=due_date,
                created_date=created_date,
                tags=tags,
                assigned_to=assigned_to,
                description=fields_data.get("System.Description"),
            )
            items.append(item)

        return items

    def create_work_item(self, title: str, work_item_type: str = "Task", **kwargs) -> WorkItem:
        """Create a new work item.

        Args:
            title: Work item title
            work_item_type: Type of work item (Task, Bug, etc.)

        Returns:
            Created WorkItem
        """
        url = (
            f"{self.base_url}/wit/workitems/${quote(work_item_type)}"
            f"?api-version={API_VERSION}"
        )
        patch_doc = [
            {"op": "add", "path": "/fields/System.Title", "value": title},
        ]

        if "state" in kwargs:
            patch_doc.append({"op": "add", "path": "/fields/System.State", "value": kwargs["state"]})
        if "priority" in kwargs:
            patch_doc.append({"op": "add", "path": "/fields/Microsoft.VSTS.Common.Priority", "value": kwargs["priority"]})
        if "due_date" in kwargs and kwargs["due_date"]:
            patch_doc.append({"op": "add", "path": "/fields/Microsoft.VSTS.Scheduling.DueDate", "value": kwargs["due_date"].isoformat()})

        headers = {**self.headers, "Content-Type": "application/json-patch+json"}
        response = requests.post(url, json=patch_doc, headers=headers)
        response.raise_for_status()

        return self.get_work_items([response.json()["id"]])[0]

    def update_work_item(self, work_item_id: int, fields: dict) -> WorkItem:
        """Update an existing work item.

        Args:
            work_item_id: ID of work item to update
            fields: Dictionary mapping field paths to values

        Returns:
            Updated WorkItem
        """
        url = f"{self.base_url}/wit/workitems/{work_item_id}?api-version={API_VERSION}"
        patch_doc = [
            {"op": "replace", "path": f"/fields/{field}", "value": value}
            for field, value in fields.items()
        ]

        headers = {**self.headers, "Content-Type": "application/json-patch+json"}
        response = requests.patch(url, json=patch_doc, headers=headers)
        response.raise_for_status()

        return self.get_work_items([work_item_id])[0]

    def delete_work_item(self, work_item_id: int):
        """Delete a work item (moves to recycle bin).

        Args:
            work_item_id: ID of work item to delete
        """
        url = f"{self.base_url}/wit/workitems/{work_item_id}?api-version={API_VERSION}"
        response = requests.delete(url, headers=self.headers)
        response.raise_for_status()
