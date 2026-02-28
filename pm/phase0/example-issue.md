# Test: Azure Things MVP - Core Task Management

**References:** #1 (parent feature issue)

**Platform Coverage:**
- [ ] macOS (@username)
- [ ] Linux (@username)
- [ ] Windows (@username)

**Complexity:** 4

---

## Setup

**Prerequisites:**
1. Python 3.12 installed (or UV will install automatically)
2. Azure DevOps organization with active work items
3. Personal Access Token with "Work item (read & write)" scope

**Initial Configuration:**
```bash
# Clone repository
git clone https://github.com/your-org/reimagined-telegram.git
cd reimagined-telegram

# Run application
uv run azure-things
```

**Environment Setup:**
Create `.env` file in project root:
```
AZURE_DEVOPS_ORG=your-organization
AZURE_DEVOPS_PAT=your-personal-access-token
```

> **Note:** If no `.env` exists, the settings dialog should appear automatically on first launch.

---

## Scenarios

### Setup & Configuration

#### 1. First Launch (No Credentials)
- Should display settings dialog automatically when no `.env` file exists
- Should provide clear instructions for generating a PAT
- Should include a link to `https://dev.azure.com/{org}/_usersSettings/tokens`
- Should not show broken UI or error messages before credentials are entered

#### 2. Credential Entry
- Should accept organization name (just the name, not full URL)
- Should accept PAT as a password-masked input field
- Should have a "Test Connection" button that validates credentials before saving
- Should show success message when connection test passes
- Should show specific error message when connection test fails (auth error vs network error)
- Should create `.env` file in project root when Save is clicked
- Should load work items immediately after successful save

#### 3. Settings Access
- Should show settings icon in sidebar (top corner)
- Should open settings dialog when icon is clicked
- Should display current organization name (PAT should be masked)
- Should allow updating credentials at any time
- Should re-validate connection when credentials are updated

### Work Item Display

#### 4. List Categories
- Should display all seven categories in sidebar: Inbox, Today, Upcoming, Anytime, Someday, Logbook, Trash
- Should show count badge next to each category name
- Should update counts automatically when work items are categorized

#### 5. `Inbox` List
- Should show work items where `State = 'New'` and no due date is set
- Should display empty state message when no items match criteria
- Example work item that should appear in Inbox:
  ```
  Title: "New feature request"
  State: New
  Due Date: (none)
  Priority: 2
  ```

#### 6. `Today` List
- Should show work items where due date is today
- Should also show work items with `Priority = 1` (High) regardless of due date
- Should sort by priority (high to low), then by due date
- Example work items:
  ```
  # Should appear in Today:
  Title: "Fix critical bug"
  State: Active
  Due Date: 2026-02-28 (today)
  Priority: 1

  # Should also appear in Today (high priority):
  Title: "Deploy hotfix"
  State: Active
  Due Date: 2026-03-05
  Priority: 1
  ```

#### 7. `Upcoming` List
- Should show work items with due date within next 7 days (excluding today)
- Should not show items already in Today list
- Should display due dates relative to today ("in 2 days", "in 5 days")

#### 8. `Anytime` List
- Should show active work items without specific due dates
- Should exclude items in Inbox, Today, Upcoming, Someday
- Should be the default backlog view
- Should show items with `State IN ('Active', 'New')` that don't match other list criteria

#### 9. `Someday` List
- Should show work items with `Priority = 4` (Very Low)
- Should also show items tagged with "someday" tag
- Should indicate these are low-priority future considerations

#### 10. `Logbook` List
- Should show completed work items: `State IN ('Resolved', 'Closed')`
- Should display completion date
- Should allow unchecking to reopen items
- When unchecked, item should return to appropriate list based on due date/priority

#### 11. `Trash` List
- Should show deleted work items: `State = 'Removed'`
- Should also show items tagged with "trash" tag
- Should allow permanent deletion or restoration

### Task Operations

#### 12. Creating Tasks
- Should show "+ New Task" button in current list view
- Should open inline input field when button is clicked
- Should create work item in Azure Boards when Enter is pressed
- Should set sensible defaults based on current list:
  ```
  # Creating in Today list:
  Type: Task
  State: New
  Priority: 1 (High)
  Due Date: Today

  # Creating in Anytime list:
  Type: Task
  State: New
  Priority: 2 (Normal)
  Due Date: (none)
  ```
- Should display new task immediately in the list
- Should handle creation errors gracefully (network failure, auth expiration)

#### 13. Completing Tasks
- Should have checkbox on left side of each task
- Should animate task out of current list when checked
- Should move task to Logbook
- Should update work item state to "Closed" in Azure Boards
- Should show subtle confirmation feedback

#### 14. Deleting Tasks
- Should show delete button on hover or right-click menu
- Should move task to Trash (not permanent deletion)
- Should update work item state to "Removed" in Azure Boards
- Should allow restoration from Trash

#### 15. Editing Task Details
- Should allow inline editing of task title (click to edit)
- Should show date picker when clicking due date
- Should show priority dropdown when clicking priority indicator
- Should sync changes to Azure Boards immediately
- Should show visual feedback on save (subtle highlight or checkmark)
- Should handle concurrent edits gracefully (server version wins)

### Synchronization

#### 16. Refresh Operation
- Should have refresh button in task list header
- Should fetch latest work items from Azure Boards when clicked
- Should show subtle progress indicator during sync
- Should update counts and task positions after sync completes
- Should preserve current list selection during refresh

#### 17. Offline Mode
- Should display cached work items when network is unavailable
- Should show banner indicating offline mode
- Should allow viewing cached tasks (read-only)
- Should queue local changes for sync when connection returns
- Should not show creation errors as failures (queue for retry)

#### 18. Error Handling
- Should display user-friendly messages for all errors:
  - **Auth failure (401):** "Authentication failed. Please check your credentials in Settings."
  - **Not found (404):** "Work item not found. It may have been deleted."
  - **Rate limit (429):** "Too many requests. Please wait a moment and try again."
  - **Network error:** "Unable to connect to Azure Boards. Working offline."
- Should never show raw exception tracebacks to users
- Should offer actionable next steps (open settings, retry, etc.)

### UI/UX Polish

#### 19. Dark Theme
- Should use background color `#1C1C1E`
- Should use surface color `#2C2C2E` for cards and panels
- Should use Things blue `#3478F6` for primary actions and selected states
- Should have readable white/light gray text on dark backgrounds
- Should provide sufficient contrast for accessibility

#### 20. Responsiveness
- Should handle window resizing gracefully (sidebar stays fixed width, task list flexes)
- Should render list transitions instantly (< 100ms)
- Should update UI immediately after local actions (optimistic updates)
- Should handle 100+ work items without performance degradation
- Should scroll smoothly in task list with large datasets

#### 21. Layout
- Should use two-column layout: sidebar (250px) + task list (remaining width)
- Should show list name in task list header
- Should show count badge for each sidebar list item
- Should highlight currently selected list in sidebar
- Should maintain consistent spacing and alignment

---

## Success Criteria

- [ ] All core CRUD operations work (create, read, update, delete)
- [ ] Work items sync bidirectionally with Azure Boards
- [ ] Smart categorization places items in correct lists automatically
- [ ] UI matches Things app aesthetic (dark theme, clean layout)
- [ ] Credentials persist securely in `.env` file
- [ ] Offline mode works with cached data
- [ ] All error scenarios display user-friendly messages
- [ ] Application handles 100+ work items smoothly
- [ ] Teammate can clone and run with single command: `uv run azure-things`

---

**Authored by:** @username
**Date:** 2026-02-28
