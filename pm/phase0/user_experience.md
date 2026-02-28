# User Experience - Phase 0

The Azure Things application is designed to feel familiar and effortless for anyone who has used the Things app, while seamlessly integrating with Azure Boards behind the scenes. The entire experience prioritizes simplicity and clarity, making task management feel natural rather than technical.

## First Launch

When a team member first runs the application with `uv run azure-things`, the app opens in their default web browser. If no `.env` file exists with credentials, the application immediately displays a clean settings dialog rather than showing an empty or broken interface. This dialog welcomes the user and explains what's needed: their Azure DevOps organization name and a Personal Access Token.

The settings dialog provides helpful context, including a direct link to generate a PAT at the Azure DevOps token management page. The user enters their organization name (just the name, not the full URL—the app constructs the API endpoints automatically) and pastes their newly generated PAT. A "Test Connection" button allows them to verify their credentials work before saving. When they click Save, the app writes the `.env` file and immediately loads their work items, transitioning smoothly into the main interface.

## Main Interface

The main interface uses a two-column layout that mirrors the Things app aesthetic. The left sidebar is narrow and dark, displaying a vertical list of categories: Inbox, Today, Upcoming, Anytime, Someday, Logbook, and Trash. Each category shows a count badge indicating how many work items it contains. The sidebar has a subtle settings icon in the top corner for accessing credentials later.

The right side of the screen is the task list, which fills the remaining space. At the top is a simple header showing the current list name (e.g., "Today") and a refresh button to sync with Azure Boards. Below that, tasks are displayed as clean rows with checkboxes on the left, task titles in a readable font, and subtle metadata (due date, priority indicator) on the right in a muted color.

The dark theme uses nearly black backgrounds (`#1C1C1E`) with slightly lighter surfaces (`#2C2C2E`) for individual UI elements. The Things blue (`#3478F6`) appears sparingly for primary actions and selected states, creating visual hierarchy without overwhelming the interface. Text is crisp white or light gray, ensuring excellent readability while maintaining the dark aesthetic.

## Navigating Lists

Clicking any list name in the sidebar instantly filters the task view to show only relevant work items. The application uses intelligent categorization: Inbox shows new items that haven't been triaged yet, Today shows anything due today or marked high priority, Upcoming shows tasks due within the next week, and Anytime holds everything else that's active. Someday contains low-priority items for future consideration, while Logbook shows completed work and Trash holds deleted items.

This categorization happens automatically based on work item state, due date, and priority fields in Azure Boards. Users don't manually assign items to lists—the app does it intelligently, just like Things does.

## Working with Tasks

Creating a new task is straightforward: a "+ New Task" button appears at the bottom of the current list. Clicking it opens an inline input field where the user types the task title and presses Enter. The app immediately creates the work item in Azure Boards and displays it in the list. For the initial version, tasks are created with sensible defaults (type: Task, state: New, priority based on the list).

Completing a task is as simple as checking its checkbox. The task smoothly animates out of the current list and moves to Logbook. Behind the scenes, the app updates the work item state to "Closed" in Azure Boards. If the user unchecks a completed task in Logbook, it returns to its appropriate list (based on its due date and priority) and reopens in Azure Boards.

Deleting a task happens via a subtle delete button that appears when hovering over a task, or through a right-click context menu. Deleted tasks move to Trash and their state changes to "Removed" in Azure Boards. Users can permanently delete from Trash or restore items back to their original list.

Editing task details works inline: clicking on a task title makes it editable, clicking on the due date opens a date picker, and priority can be adjusted with a small dropdown indicator. All changes sync to Azure Boards immediately, with subtle visual feedback confirming the save.

## Synchronization and Feedback

The app maintains a local cache of work items for fast loading and basic offline viewing. When online, clicking the refresh button fetches the latest work items from Azure Boards, updating the local cache and refreshing the current view. The refresh happens smoothly without jarring loading states—a subtle progress indicator appears in the header while syncing.

Error handling is user-friendly and informative. If the network is unavailable, the app displays cached data with a small banner indicating offline mode. If authentication fails (expired PAT, incorrect credentials), a clear message explains the issue and offers to open settings. If a sync conflict occurs (item changed both locally and remotely), the app defaults to the server version but notifies the user.

## Settings and Credential Management

Users can access settings anytime via the icon in the sidebar. The settings dialog shows their current organization name (with the PAT masked for security) and allows updating either credential. Clicking Save updates the `.env` file and re-establishes the connection. A "Test Connection" button provides immediate feedback on whether credentials are working.

## Overall Feel

The entire experience feels fast and responsive. List transitions are instant, task updates provide immediate visual feedback, and the UI never blocks or freezes. The dark theme is easy on the eyes during long work sessions, and the minimal design keeps focus on the tasks themselves rather than UI chrome.

For team members familiar with Things, the experience feels instantly comfortable. For those new to both, the interface is intuitive enough to use without training. The application succeeds in making Azure Boards feel less like enterprise tooling and more like a personal productivity app designed for individual workflows.
