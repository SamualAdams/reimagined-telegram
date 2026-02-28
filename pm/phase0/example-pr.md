# Phase 1: Project Foundation & Basic Structure

**Closes:** #2
**Related:** #1 (parent feature)

---

## Summary

This PR establishes the foundational project structure for Azure Things, implementing Phase 1 of the development plan. It sets up UV package management, creates the core directory structure following Python best practices (src layout), and adds essential configuration files.

**What's included:**
- ✅ UV project initialization with Python 3.12
- ✅ Core dependencies configured (Flet, requests, pydantic, python-dotenv)
- ✅ Complete source directory structure (`azure/`, `ui/`, `storage/`, `utils/`)
- ✅ Proper `.gitignore` for Python projects
- ✅ README with setup instructions for teammates
- ✅ Entry point configuration for `uv run azure-things`

**What's NOT included (future PRs):**
- Azure Boards API client implementation
- UI components (Flet app)
- Credential management logic
- Work item categorization

---

## Changes

### Project Configuration

**pyproject.toml**
- Added UV project configuration with Python 3.12 requirement
- Configured dependencies:
  - `flet>=0.24.0` - Web UI framework
  - `requests>=2.31.0` - HTTP client for Azure API
  - `pydantic>=2.0.0` - Data validation
  - `python-dotenv>=1.0.0` - Credential loading from .env
- Defined console script entry point: `azure-things = "azure_things.main:main"`
- Added dev dependencies: `pytest`, `black`, `ruff` for testing and linting

**.python-version**
- Pinned to Python 3.12 for consistent UV behavior across team

**.gitignore**
- Excluded `.env` (credentials)
- Excluded Python artifacts (`__pycache__/`, `*.pyc`, `.pytest_cache/`)
- Excluded build artifacts (`dist/`, `*.egg-info/`)
- Excluded virtual environments (`.venv/`, `venv/`)

### Source Structure

Created complete package structure under `src/azure_things/`:

```
src/azure_things/
├── __init__.py          # Package root with version
├── main.py              # Entry point (placeholder main() function)
├── config.py            # Constants (API version, colors, list names)
├── azure/
│   ├── __init__.py     # Exposes client, models
│   ├── client.py       # Placeholder AzureBoardsClient class
│   ├── auth.py         # Placeholder auth helpers
│   └── models.py       # Placeholder Pydantic models
├── ui/
│   ├── __init__.py     # Exposes main app
│   ├── app.py          # Placeholder AzureThingsApp
│   ├── sidebar.py      # Placeholder Sidebar component
│   ├── task_list.py    # Placeholder TaskList component
│   ├── task_item.py    # Placeholder TaskItem component
│   ├── settings.py     # Placeholder SettingsDialog
│   └── theme.py        # Dark theme colors and constants
├── storage/
│   ├── __init__.py     # Exposes credentials, cache
│   ├── credentials.py  # Placeholder credential loading
│   └── cache.py        # Placeholder cache class
└── utils/
    ├── __init__.py     # Exposes public functions
    ├── mapper.py       # Placeholder categorization logic
    └── validators.py   # Placeholder validation functions
```

**Current Implementation:**
- All modules are placeholders with docstrings explaining their purpose
- `config.py` contains actual constants (API_VERSION, COLORS, LIST_NAMES)
- `theme.py` has complete color definitions for dark theme
- `main.py` has basic entry point structure (imports Flet, defines main())

### Test Structure

Created mirror test structure under `tests/`:

```
tests/
├── __init__.py
├── test_config.py       # Tests for constants
├── azure/
│   ├── __init__.py
│   ├── test_client.py   # Placeholder
│   ├── test_auth.py     # Placeholder
│   └── test_models.py   # Placeholder
├── ui/
│   ├── __init__.py
│   ├── test_app.py      # Placeholder
│   └── test_sidebar.py  # Placeholder
├── storage/
│   ├── __init__.py
│   ├── test_credentials.py  # Placeholder
│   └── test_cache.py        # Placeholder
└── utils/
    ├── __init__.py
    ├── test_mapper.py    # Placeholder
    └── test_validators.py  # Placeholder
```

### Documentation

**README.md**
- Added project overview and goals
- Setup instructions for teammates: `uv run azure-things`
- First-time credential setup flow
- Development workflow (running tests, linting)
- Contribution guidelines

---

## Testing

**Verification Steps:**
```bash
# 1. Clone and verify Python version
uv python --version  # Should show 3.12.x

# 2. Install dependencies
uv sync

# 3. Run placeholder app (should not crash)
uv run azure-things

# 4. Run tests (placeholder tests should pass)
uv run pytest

# 5. Run linting
uv run ruff check src/ tests/
uv run black --check src/ tests/
```

**Expected Results:**
- ✅ UV installs Python 3.12 automatically
- ✅ All dependencies install without errors
- ✅ `azure-things` command runs without import errors
- ✅ Placeholder tests pass (currently just imports)
- ✅ Code passes linting checks (ruff, black)

**Manual Testing:**
- [x] Fresh clone on macOS works
- [ ] Fresh clone on Linux works
- [ ] Fresh clone on Windows works

---

## Code Quality

**Linting:**
```bash
# All checks pass
uv run ruff check src/ tests/
uv run black --check src/ tests/
```

**Type Checking:**
- Placeholder code includes type hints for future mypy integration
- All public functions have docstrings

**Documentation:**
- All modules include module-level docstrings
- README provides clear setup instructions
- Comments explain non-obvious placeholder design decisions

---

## Breaking Changes

None (initial implementation)

---

## Migration Guide

**For teammates:**
1. Pull this branch
2. Run `uv run azure-things`
3. UV will automatically install Python 3.12 and dependencies
4. Create `.env` file with credentials (see README)

**No migration needed** - this is the initial project setup.

---

## Screenshots

_Application doesn't have UI yet - this PR only sets up structure._

**Directory structure verification:**
```bash
$ tree src/azure_things -L 2
src/azure_things
├── __init__.py
├── main.py
├── config.py
├── azure/
│   ├── __init__.py
│   ├── client.py
│   ├── auth.py
│   └── models.py
├── ui/
│   ├── __init__.py
│   ├── app.py
│   ├── sidebar.py
│   ├── task_list.py
│   ├── task_item.py
│   ├── settings.py
│   └── theme.py
├── storage/
│   ├── __init__.py
│   ├── credentials.py
│   └── cache.py
└── utils/
    ├── __init__.py
    ├── mapper.py
    └── validators.py
```

---

## Checklist

**Before merging:**
- [x] All placeholder tests pass
- [x] Code passes linting (ruff, black)
- [x] README includes setup instructions
- [x] `.gitignore` excludes `.env` and Python artifacts
- [x] `pyproject.toml` defines correct entry point
- [ ] At least one team member has tested fresh clone on their machine
- [ ] PR reviewed by at least one other developer

**Post-merge:**
- [ ] Create Phase 2 issue (Azure Boards API client implementation)
- [ ] Update project board to mark Phase 1 as complete

---

**Reviewer notes:**

This is a foundational PR - focus on:
1. Directory structure follows Python best practices (src layout)
2. All configuration files are correct (pyproject.toml, .python-version, .gitignore)
3. Entry point is properly defined
4. README provides clear instructions

Don't worry about placeholder implementations - those will be filled in subsequent PRs (Phases 2-7).

---

**Co-Authored-By:** Claude Sonnet 4.5 <noreply@anthropic.com>
