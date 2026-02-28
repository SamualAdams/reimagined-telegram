# Environment - Phase 0

This project is a Python application called Azure Things that provides a Things app-like interface for managing Azure Boards work items. The application will be built using modern Python tooling and frameworks designed to work seamlessly across different machines and team member setups.

The technology stack has been carefully selected to prioritize simplicity and cross-platform compatibility. UV serves as the package manager and will handle Python version management automatically, ensuring all team members use Python 3.12 consistently without manual configuration. Flet provides a web-based UI framework that runs in a browser but feels like a native application, eliminating cross-platform GUI compatibility issues. For backend integration, we'll use the Azure Boards REST API directly via HTTP requests with the requests library, and Pydantic will handle data validation and serialization. Python-dotenv handles credential management by loading from a simple .env file.

The project is organized into a clear source structure under `src/azure_things/` with distinct modules for different concerns. The Azure integration lives in the `azure/` subdirectory with separate modules for API client operations, PAT authentication, and Pydantic data models. User interface components are organized under `ui/` with a main app orchestrator, sidebar navigation, task list display, individual task items, settings dialog, and theme configuration. Storage and credential management are handled in the `storage/` module with .env loading and caching. Utility functions for mapping work items to Things-style lists and validating user input are in the `utils/` module. Tests are organized in a parallel structure for easy discovery and execution.

The application will use a dark color scheme matching the Things app aesthetic with a background color of `#1C1C1E`, surface elements at `#2C2C2E`, and the Things blue primary color at `#3478F6`. The Azure Boards API integration will use version 7.1 endpoints at `https://dev.azure.com/{organization}/_apis` with Basic Authentication using a Personal Access Token encoded in Base64.

Distribution to team members is straightforward: they clone the repository and run `uv run azure-things`, which automatically installs Python 3.12 and all dependencies. First-time setup involves entering the Azure DevOps organization URL and PAT, which are then saved to a `.env` file in the project root. This approach keeps credential management simple while ensuring the `.env` file is never committed to git.

## Credential Management

The application uses a `.env` file in the project root to store Azure Boards credentials. When the application starts, it loads the `.env` file using python-dotenv, which parses two environment variables:

- `AZURE_DEVOPS_ORG`: The Azure DevOps organization name (e.g., `myorganization`)
- `AZURE_DEVOPS_PAT`: The Personal Access Token with work item read/write permissions

**Example .env file:**
```
AZURE_DEVOPS_ORG=contoso
AZURE_DEVOPS_PAT=abcdefghijklmnopqrstuvwxyz1234567890
```

The `.env` file approach is intentionally simple: it requires no complex OS-specific credential storage logic and works identically across Windows, macOS, and Linux. The settings dialog in the application provides a user-friendly interface for creating or updating the `.env` file without requiring manual text editing.

The `.env` file is listed in `.gitignore` to prevent accidental commits of credentials to the repository. Team members must create their own `.env` file locally with their own PAT (generated at `https://dev.azure.com/{organization}/_usersSettings/tokens`). The PAT should have "Work item (read & write)" scope to allow the application to perform all CRUD operations on work items.

When the app detects a missing or incomplete `.env` file on startup, it displays the settings dialog automatically, guiding the user through credential entry. After credentials are saved, the app reloads the environment variables and proceeds to fetch work items from Azure Boards.
