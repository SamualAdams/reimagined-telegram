"""Work item categorization logic."""

from datetime import datetime, timedelta
from typing import List, Dict


def categorize_work_items(work_items: List[dict]) -> Dict[str, List[dict]]:
    """Categorize work items into Things-style lists.

    Maps work items to Inbox, Today, Upcoming, Anytime, Someday, Logbook, Trash
    based on state, due date, and priority.

    Implements Phase 4: Data Mapping.

    Args:
        work_items: List of work item dictionaries

    Returns:
        Dictionary mapping list names to work items
    """
    # TODO: Implement in Phase 4
    # Logic:
    # - Inbox: State='New' AND no due date
    # - Today: DueDate=Today OR Priority=1 (High)
    # - Upcoming: DueDate within next 7 days
    # - Anytime: Active items without due dates (default backlog)
    # - Someday: Priority=4 (Very Low) OR tagged "someday"
    # - Logbook: State IN ('Resolved', 'Closed')
    # - Trash: State='Removed' OR tagged "trash"

    categories = {
        "Inbox": [],
        "Today": [],
        "Upcoming": [],
        "Anytime": [],
        "Someday": [],
        "Logbook": [],
        "Trash": [],
    }

    return categories
