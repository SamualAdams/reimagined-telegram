"""Work item categorization logic."""

from datetime import datetime, timedelta, timezone
from typing import List, Dict

from azure_things.azure.models import WorkItem


def categorize_work_items(work_items: List[WorkItem]) -> Dict[str, List[WorkItem]]:
    """Categorize work items into Things-style lists.

    Maps work items to Inbox, Today, Upcoming, Anytime, Someday, Logbook, Trash
    based on state, due date, and priority.

    Args:
        work_items: List of WorkItem objects

    Returns:
        Dictionary mapping list names to work items
    """
    categories: Dict[str, List[WorkItem]] = {
        "Inbox": [],
        "Today": [],
        "Upcoming": [],
        "Anytime": [],
        "Someday": [],
        "Logbook": [],
        "Trash": [],
    }

    today = datetime.now(timezone.utc).date()
    week_out = today + timedelta(days=7)

    for item in work_items:
        state = item.state
        priority = item.priority
        due_date = item.due_date
        tags = [t.lower() for t in item.tags]

        if state == "Removed" or "trash" in tags:
            categories["Trash"].append(item)
        elif state in ("Resolved", "Closed", "Done"):
            categories["Logbook"].append(item)
        elif priority == 4 or "someday" in tags:
            categories["Someday"].append(item)
        elif (due_date and due_date.date() == today) or priority == 1:
            categories["Today"].append(item)
        elif due_date and today < due_date.date() <= week_out:
            categories["Upcoming"].append(item)
        elif state == "New" and not due_date:
            categories["Inbox"].append(item)
        else:
            categories["Anytime"].append(item)

    return categories
