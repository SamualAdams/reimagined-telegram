---
name: Test Plan Item
about: Create a comprehensive test plan for a feature or component
title: 'Test: [Feature Name]'
labels: testing, test-plan
assignees: ''
---

# Test: [Feature Name]

**References:** #[parent issue number]

**Platform Coverage:**
- [ ] macOS (@username)
- [ ] Linux (@username)
- [ ] Windows (@username)

**Complexity:** [1-5]

---

## Setup

**Prerequisites:**
1. [List prerequisites here]
2. [Environment requirements]
3. [Access/credentials needed]

**Initial Configuration:**
```bash
# Setup commands
```

**Environment Setup:**
[Describe .env or config file requirements]

> **Note:** [Any important setup notes]

---

## Scenarios

### [Category 1]

#### 1. [Scenario Name]
- Should [expected behavior]
- Should [expected behavior]
- Should handle [error case]
- Example:
  ```
  [Example code or data]
  ```

#### 2. [Another Scenario]
- Should [expected behavior]
- Should [expected behavior]

### [Category 2]

#### 3. [Scenario Name]
- Should [expected behavior]
- Should show [specific UI element]
- Should validate [input/output]

---

## Success Criteria

- [ ] All core functionality works
- [ ] Error handling is user-friendly
- [ ] Performance meets requirements
- [ ] UI/UX matches design
- [ ] Works across all platforms

---

**Authored by:** @username
**Date:** YYYY-MM-DD
