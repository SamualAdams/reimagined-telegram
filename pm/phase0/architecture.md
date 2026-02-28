# Codebase Structure - Phase 0

The Azure Things codebase follows modern Python packaging best practices, using a src layout with clear module organization and consistent naming conventions. This structure makes the code easy to navigate, test, and maintain.

## Project Root Layout

The project uses the src layout pattern, which is the current Python packaging best practice. This layout prevents accidental imports of uninstalled code during development and clearly separates source code from configuration, tests, and documentation.

```
reimagined-telegram/
├── .python-version          # Python version pinned to 3.12
├── pyproject.toml           # UV project config, dependencies, metadata
├── .gitignore               # Git exclusions (.env, __pycache__, etc.)
├── .env                     # Credentials (git-ignored, user creates locally)
├── README.md                # Setup and usage instructions
├── src/                     # All source code lives here
│   └── azure_things/        # Main package
├── tests/                   # Test suite (mirrors src structure)
└── pm/                      # Project management docs (phase0, etc.)
```

The root level contains only configuration files and documentation. All Python code lives under `src/azure_things/`, never in the root. This prevents `import azure_things` from working until the package is properly installed, catching import issues early.

## Source Code Organization

The `src/azure_things/` directory is the main package. Each subdirectory is a Python package (contains `__init__.py`) representing a distinct area of functionality. Modules within packages are single-purpose files, typically containing one main class or a group of related functions.

```
src/azure_things/
├── __init__.py              # Package root, exposes version
├── main.py                  # Entry point, launches Flet app
├── config.py                # Constants (API URLs, colors, list names)
├── azure/                   # Azure Boards integration
│   ├── __init__.py         # Exposes client, models
│   ├── client.py           # AzureBoardsClient class
│   ├── auth.py             # get_auth_header() and helpers
│   └── models.py           # WorkItem, WorkItemUpdate Pydantic models
├── ui/                      # Flet UI components
│   ├── __init__.py         # Exposes main app
│   ├── app.py              # AzureThingsApp main container
│   ├── sidebar.py          # Sidebar component
│   ├── task_list.py        # TaskList component
│   ├── task_item.py        # TaskItem component
│   ├── settings.py         # SettingsDialog component
│   └── theme.py            # COLORS dict, get_theme() function
├── storage/                 # Persistence layer
│   ├── __init__.py         # Exposes credentials, cache
│   ├── credentials.py      # load_credentials() function
│   └── cache.py            # WorkItemCache class
└── utils/                   # Business logic helpers
    ├── __init__.py         # Exposes public functions
    ├── mapper.py           # categorize_work_items() function
    └── validators.py       # validate_org_url(), validate_pat()
```

## Module Naming Conventions

**File names** are lowercase with underscores (snake_case): `task_list.py`, not `TaskList.py` or `task-list.py`. This follows PEP 8 Python style guidelines.

**Module names** match file names exactly. The file `task_list.py` is imported as `from azure_things.ui import task_list`.

**Class names** use PascalCase: `AzureBoardsClient`, `WorkItem`, `TaskList`. Each file typically contains one primary class with a name that makes the file's purpose obvious.

**Function names** use snake_case: `load_credentials()`, `categorize_work_items()`, `get_auth_header()`.

## Package __init__.py Files

Each `__init__.py` file defines what the package exposes publicly. This creates clean import paths and hides implementation details.

**src/azure_things/__init__.py**:
```python
__version__ = "0.1.0"
```

**src/azure_things/azure/__init__.py**:
```python
from .client import AzureBoardsClient
from .models import WorkItem, WorkItemUpdate

__all__ = ["AzureBoardsClient", "WorkItem", "WorkItemUpdate"]
```

This allows other modules to import `from azure_things.azure import AzureBoardsClient` instead of `from azure_things.azure.client import AzureBoardsClient`. The shorter path is cleaner and hides the internal organization.

## Import Organization

Imports within each file follow a consistent order (enforced by ruff/black):

1. Standard library imports
2. Third-party imports (flet, requests, pydantic)
3. Local imports from azure_things

Each group is separated by a blank line. Within groups, imports are alphabetically sorted.

```python
# Standard library
import os
from datetime import datetime
from typing import Optional

# Third-party
import requests
from pydantic import BaseModel

# Local
from azure_things.azure.auth import get_auth_header
from azure_things.config import API_VERSION
```

Modules use absolute imports from the package root: `from azure_things.azure import AzureBoardsClient`, never relative imports like `from ..azure import AzureBoardsClient`. Absolute imports are more explicit and work consistently across the codebase.

## Test Structure

The `tests/` directory mirrors the `src/azure_things/` structure exactly. Each source module has a corresponding test file with a `test_` prefix.

```
tests/
├── __init__.py
├── test_config.py
├── azure/
│   ├── __init__.py
│   ├── test_client.py
│   ├── test_auth.py
│   └── test_models.py
├── ui/
│   ├── __init__.py
│   ├── test_app.py
│   ├── test_sidebar.py
│   └── test_task_list.py
├── storage/
│   ├── __init__.py
│   ├── test_credentials.py
│   └── test_cache.py
└── utils/
    ├── __init__.py
    ├── test_mapper.py
    └── test_validators.py
```

This mirroring makes tests easy to find: if you're working on `src/azure_things/azure/client.py`, you know tests are in `tests/azure/test_client.py`. Test discovery tools (pytest) automatically find all `test_*.py` files.

Test function names start with `test_` and describe what they verify: `test_load_credentials_missing_file()`, `test_categorize_work_items_today_list()`. This makes test output readable when tests fail.

## Configuration Files

Configuration files live in the project root, not buried in subdirectories:

**pyproject.toml** - UV project configuration, dependencies, build settings, tool configs (ruff, pytest, black)

**.python-version** - Pins Python version to 3.12 for UV

**.env** - Runtime credentials, git-ignored, created by user or settings dialog

**.gitignore** - Excludes `.env`, `__pycache__/`, `*.pyc`, `.pytest_cache/`, `dist/`, `.venv/`

This keeps configuration discoverable at the root where tools expect to find it. Never nest configuration files like `src/.env` or `tests/pytest.ini` unless tools specifically require it.

## Entry Point Definition

The application entry point is defined in `pyproject.toml` as a console script:

```toml
[project.scripts]
azure-things = "azure_things.main:main"
```

This creates a `azure-things` command that calls the `main()` function in `src/azure_things/main.py`. Users run `uv run azure-things` to launch the app. The entry point is never an executable Python file in the root—it's always a function in an installed package.

## Import Boundaries

Modules respect clear import boundaries to prevent circular dependencies and maintain separation of concerns:

- **UI modules** can import from azure, storage, and utils, but never vice versa
- **azure modules** don't import from ui or storage
- **storage modules** don't import from azure or ui
- **utils modules** don't import from any other package (only stdlib and third-party)

The dependency graph flows one direction: ui → azure/storage/utils → config. No module ever imports from a module that imports it. This makes the codebase acyclic and prevents import-time errors.

## File Size and Scope

Each module file stays focused and relatively small (typically under 300 lines). When a file grows large, it's a signal to split it into smaller focused modules. For example, if `client.py` grows to include both HTTP logic and retry logic, split retry handling into `client_retry.py`.

Modules contain related functionality, not just "all the functions." The `mapper.py` module contains only work item categorization logic, not general utility functions. General utilities go in their own appropriately named module.

## Shared Constants

The `config.py` file at the package root contains all shared constants: API endpoints, color values, list names, default work item types. This prevents magic strings scattered throughout the code and provides a single place to update configuration.

```python
# config.py
API_VERSION = "7.1"
API_BASE = "https://dev.azure.com/{org}/_apis"

COLORS = {
    "background": "#1C1C1E",
    "surface": "#2C2C2E",
    "primary": "#3478F6",
}

LIST_NAMES = ["Inbox", "Today", "Upcoming", "Anytime", "Someday", "Logbook", "Trash"]
```

Modules import specific constants: `from azure_things.config import API_VERSION`, not `from azure_things import config` and then `config.API_VERSION`. Specific imports make dependencies explicit.

## Documentation Location

User-facing documentation (README.md) lives in the project root. Developer documentation about architecture, codebase structure, and design decisions lives in `pm/phase0/`. This keeps project management artifacts separate from code while keeping user documentation easily discoverable.

Code comments and docstrings live inline with the code itself. Each public function and class has a docstring explaining its purpose, parameters, and return value. Internal implementation details are commented inline where the logic isn't obvious.
