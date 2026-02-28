# Claude Code Instructions

This file contains instructions and guidelines for Claude Code when working on this project.

## Project Overview

**Azure Things** is a Things app-like interface for managing Azure Boards work items. It's a Python application using UV for package management, Flet for the UI, and a simple .env file for credentials.

## Development Workflow

### Issue and PR Templates

This project follows the **VSCode repository pattern** for issues and pull requests. Templates are located in `.github/`:

**Test Plan Items (Issues):**
- Use `.github/ISSUE_TEMPLATE/test-plan.md` for comprehensive feature test plans
- Include platform coverage, setup instructions, and detailed scenarios
- Follow the "Should..." pattern for acceptance criteria
- Reference: See `pm/phase0/example-issue.md` for a complete example

**Pull Requests:**
- Use `.github/PULL_REQUEST_TEMPLATE.md` for all PRs
- Include summary, detailed changes, testing steps, and checklists
- Always add "Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"
- Reference: See `pm/phase0/example-pr.md` for a complete example

### Creating Issues

```bash
# Create a test plan issue using the template
gh issue create --template test-plan.md

# Or create from scratch with template content
gh issue create --title "Test: [Feature]" --body "$(cat .github/ISSUE_TEMPLATE/test-plan.md)"
```

### Creating Pull Requests

```bash
# Create a PR (template auto-fills)
gh pr create --draft --title "[Phase]: Description"

# The template in .github/PULL_REQUEST_TEMPLATE.md will auto-populate
```

## Project Structure

Follow the **src layout** pattern (see `pm/phase0/architecture.md`):

```
reimagined-telegram/
├── src/azure_things/     # All source code here
├── tests/                # Mirror src structure
├── pm/phase0/            # Planning docs (narrative format)
└── .github/              # Issue/PR templates
```

### Module Organization

- **azure/** - Azure Boards API integration
- **ui/** - Flet UI components
- **storage/** - Credential loading and caching
- **utils/** - Business logic (mapping, validation)

### Import Rules

- Use absolute imports: `from azure_things.azure import AzureBoardsClient`
- Never use relative imports
- Respect import boundaries (ui → azure/storage/utils, never reverse)

## Credential Management

**Simple .env approach:**
```
AZURE_DEVOPS_ORG=your-organization
AZURE_DEVOPS_PAT=your-pat-token
```

- Load with python-dotenv
- Never commit .env to git
- Settings dialog helps users create/edit .env
- See `pm/phase0/environment.md` for details

## Code Quality Standards

**Before committing:**
```bash
# Run tests
uv run pytest

# Lint code
uv run ruff check src/ tests/
uv run black --check src/ tests/

# Fix formatting
uv run black src/ tests/
```

**Type hints:**
- All public functions should have type hints
- Use Pydantic models for data validation

**Docstrings:**
- All public functions and classes need docstrings
- Explain purpose, parameters, and return values

## Git Workflow

**Commit messages:**
- Use imperative mood: "Add feature" not "Added feature"
- Include context in body for complex changes
- Always add: "Co-Authored-By: Claude Sonnet 4.5 <noreply@anthropic.com>"

**Branch naming:**
```
phase0-documentation
phase1-project-foundation
phase2-azure-integration
feature/specific-feature
bugfix/specific-bug
```

**Creating PRs:**
1. Create feature branch from main
2. Make changes and commit
3. Push branch: `git push -u origin branch-name`
4. Create draft PR: `gh pr create --draft`
5. Fill in template (auto-populated)
6. Request review when ready

## Testing Strategy

**Structure:**
- Mirror src/ structure in tests/
- Use `test_` prefix for all test files and functions
- Group tests by module: `tests/azure/test_client.py`

**Running tests:**
```bash
# All tests
uv run pytest

# Specific module
uv run pytest tests/azure/

# With coverage
uv run pytest --cov=azure_things
```

## Documentation

**Phase 0 Planning Docs:**
- `pm/phase0/intent.md` - Project goals and phases
- `pm/phase0/environment.md` - Tech stack and setup
- `pm/phase0/user_experience.md` - UX flow
- `pm/phase0/architecture.md` - Codebase structure

All docs use **narrative format** (flowing prose, not bullet lists).

## Common Commands

```bash
# Run the app
uv run azure-things

# Install dependencies
uv sync

# Add a dependency
uv add package-name

# Run tests
uv run pytest

# Format code
uv run black src/ tests/

# Lint
uv run ruff check src/ tests/
```

## Azure Boards API

**Base URL:** `https://dev.azure.com/{organization}/_apis`
**API Version:** 7.1
**Authentication:** Basic Auth with PAT (Base64 encoded)

**Key Endpoints:**
- WIQL queries: `POST /wit/wiql`
- Get work items: `GET /wit/workitems?ids={ids}`
- Create: `POST /wit/workitems/${type}`
- Update: `PATCH /wit/workitems/{id}`
- Delete: `DELETE /wit/workitems/{id}`

## UI Theme

**Things App Dark Theme:**
- Background: `#1C1C1E`
- Surface: `#2C2C2E`
- Primary: `#3478F6` (Things blue)

See `config.py` for all constants.

## Work Item Categorization

**List mapping logic:**
- **Inbox**: State='New' AND no due date
- **Today**: DueDate=Today OR Priority=1 (High)
- **Upcoming**: DueDate within next 7 days
- **Anytime**: Active items without due dates (default backlog)
- **Someday**: Priority=4 (Very Low) OR tagged "someday"
- **Logbook**: State IN ('Resolved', 'Closed')
- **Trash**: State='Removed' OR tagged "trash"

See `utils/mapper.py` for implementation.

## Best Practices

1. **Keep it simple** - Don't over-engineer
2. **Follow the templates** - Use issue/PR templates consistently
3. **Test before committing** - Run pytest and linting
4. **Document decisions** - Update pm/phase0/ docs when architecture changes
5. **Respect boundaries** - Follow import rules and module separation
6. **Stay focused** - Each PR should do one thing well
7. **Communicate changes** - Use detailed PR descriptions

## References

- **Example Test Plan:** `pm/phase0/example-issue.md`
- **Example PR:** `pm/phase0/example-pr.md`
- **VSCode Issue Pattern:** https://github.com/microsoft/vscode/issues/297090
