# Intent - Phase 1

Phase 1 delivers a working Azure Things application with a complete user interface that connects to Azure Boards. The goal is to go from scaffolding to a functional desktop app that a team member can launch, authenticate against their Azure DevOps organization, and immediately start viewing and managing their work items in a Things-style interface.

The application implements a two-column layout with a sidebar listing seven smart categories (Inbox, Today, Upcoming, Anytime, Someday, Logbook, Trash) and a main content area displaying work items for the selected category. Work items are automatically categorized based on their state, due date, and priority. Users can create new tasks, mark tasks complete, and delete tasks, with all changes syncing back to Azure Boards.

The Azure Boards REST API integration uses WIQL queries to fetch work items and supports full CRUD operations. Authentication uses a Personal Access Token stored in a .env file alongside the organization name and project name. A settings dialog allows users to configure their credentials from within the app.

Phase 1 also establishes the build system properly using hatchling with a src layout, ensuring that `uv run azure-things` works reliably after `uv sync` without manual intervention.
