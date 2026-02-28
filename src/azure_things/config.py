"""Application configuration and constants."""

# Azure Boards API Configuration
API_VERSION = "7.1"
API_BASE = "https://dev.azure.com/{org}/_apis"

# UI Theme Colors (Things App Dark Theme)
COLORS = {
    "background": "#1C1C1E",
    "surface": "#2C2C2E",
    "primary": "#3478F6",
    "text_primary": "#FFFFFF",
    "text_secondary": "#98989D",
}

# Things-style List Names
LIST_NAMES = [
    "Inbox",
    "Today",
    "Upcoming",
    "Anytime",
    "Someday",
    "Logbook",
    "Trash",
]

# Default Work Item Settings
DEFAULT_WORK_ITEM_TYPE = "Task"
DEFAULT_PRIORITY = 2  # Normal priority
