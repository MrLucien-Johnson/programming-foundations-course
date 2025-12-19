# Enhancement 3: Delete Tasks

Add the ability to delete tasks from the task list.

## Steps

1. **Modify `task_manager.py`:**
   - Add `delete_task(task_number)` method
   - Validate the task number
   - Remove the task from the list
   - Show confirmation message

2. **Modify `main.py`:**
   - Add menu option "Delete Task"
   - Show task list before deletion
   - Ask for confirmation before deleting

## Example Output

```
=== Your Tasks ===
1. Buy groceries - ○ Incomplete
2. Finish report - ○ Incomplete

Enter task number to delete: 2
Are you sure you want to delete 'Finish report'? (yes/no): yes
✓ Task 'Finish report' deleted successfully!
```

