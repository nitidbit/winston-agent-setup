---
name: clear-prd-and-issues
description: This skill is used before `/write-a-prd` to clear away the previous work's thinking so we can start fresh. It deletes all the files under $ISSUES_DIR.
---

# Clear PRD and Issues

Delete all files under $ISSUES_DIR so the next `/write-a-prd` run starts from a clean slate, without any leftover PRD or issue files influencing the new work.

## Settings
$AGENT_DIR = agent~/
$ISSUES_DIR = $AGENT_DIR/issues/

## Process

### 1. Check what exists

List the files currently in $ISSUES_DIR. If the directory doesn't exist or is already empty, tell the user there is nothing to clear and stop.

### 2. Confirm with the user

Show the list of files that will be deleted and ask the user to confirm before deleting. This is a destructive, hard-to-reverse action.

### 3. Delete

Once confirmed, delete all files under $ISSUES_DIR. Leave the $ISSUES_DIR directory itself in place (empty) rather than removing it.

Do NOT touch any files outside of $ISSUES_DIR.
