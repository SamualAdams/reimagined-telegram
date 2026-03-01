# Azure Things

A Things app-like interface for managing Azure Boards work items.

## Overview

Azure Things provides a familiar, intuitive task management UI for Azure Boards, bringing the elegant simplicity of the Things app to your work item management workflow.

**Key Features:**
- Things-style list organization (Inbox, Today, Upcoming, Anytime, Someday, Logbook, Trash)
- Dark theme matching Things app aesthetic
- Simple credential management via .env file
- Bidirectional sync with Azure Boards
- Offline support with local caching

## Quick Start

```bash
# Clone the repository
git clone https://github.com/SamualAdams/reimagined-telegram.git
cd reimagined-telegram

# Run the application (UV auto-installs Python 3.12 and dependencies)
uv run azure-things
```

## First-Time Setup

1. **Generate a Personal Access Token (PAT)**
   - Go to https://dev.azure.com/{your-organization}/_usersSettings/tokens
   - Create a new token with "Work item (read & write)" scope
   - Copy the token

2. **Create .env file**
   ```bash
   # In the project root, create a .env file:
   AZURE_DEVOPS_ORG=your-organization-name
   AZURE_DEVOPS_PAT=your-personal-access-token
   ```

3. **Run the app**
   ```bash
   uv run azure-things
   ```

## Development

### Prerequisites

- UV package manager (automatically installs Python 3.12)
- Git

### Setup Development Environment

```bash
# Install dependencies
uv sync

# Run tests
uv run pytest

# Run linting
uv run ruff check src/ tests/
uv run black --check src/ tests/

# Format code
uv run black src/ tests/
```

### Project Structure

```
reimagined-telegram/
├── src/azure_things/      # Source code
│   ├── azure/            # Azure Boards API integration
│   ├── ui/               # Flet UI components
│   ├── storage/          # Credentials and caching
│   └── utils/            # Business logic
├── tests/                # Test suite (mirrors src/)
├── pm/phase0/            # Planning documentation
└── .github/              # Issue/PR templates
```

## Implementation Status

This project is being built in phases:

- ✅ **Phase 1**: Project Foundation (current)
  - UV project setup
  - Directory structure
  - Configuration and placeholders

- 🚧 **Phase 2**: Azure Integration
  - Azure Boards API client
  - Authentication
  - Work item models

- 🚧 **Phase 3**: Credential Storage
  - .env file management
  - Settings dialog
  - Validation

- 🚧 **Phase 4**: Data Mapping
  - Work item categorization
  - List logic
  - Caching

- 🚧 **Phase 5**: UI Foundation
  - Flet app structure
  - Theme implementation
  - Components

- 🚧 **Phase 6**: Feature Integration
  - CRUD operations
  - Sync functionality
  - Error handling

- 🚧 **Phase 7**: Testing & Documentation
  - Comprehensive tests
  - Documentation
  - Bug fixes

## Contributing

See `CLAUDE.md` for development guidelines and workflow.

### Creating Issues

Use the test plan template:
```bash
gh issue create --template template-issue.md
```

### Creating Pull Requests

PR template auto-populates:
```bash
gh pr create --draft --title "[Phase]: Description"
```

## Documentation

- **Planning Docs**: `pm/phase0/`
  - `intent.md` - Project goals and phases
  - `environment.md` - Tech stack and setup
  - `user_experience.md` - UX design
  - `architecture.md` - Codebase structure

- **Development Guide**: `CLAUDE.md`

## License

[Add license information]

## Support

For issues and questions, please create an issue using the template.
