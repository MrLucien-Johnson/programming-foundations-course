# Enhancement 1: Add Due Dates to Tasks

Add due date functionality to your Task Tracker. Tasks should have a due date, and you should be able to see which tasks are due soon.

## Steps

1. **Modify `task_item.py`:**
   - Add a `due_date` property (use `datetime` or string)
   - Update constructor to accept optional due date
   - Update `display_info()` to show due date if it exists

2. **Modify `task_manager.py`:**
   - Update `add_task()` to ask for due date (optional)
   - Add method to show tasks due today or soon

3. **Modify `main.py`:**
   - Update menu to include "Show tasks due soon"
   - Handle date input from user

## Hints

- Use `datetime.date` for dates: `from datetime import date`
- Use `date.today()` to get today's date
- Compare dates: `due_date <= date.today()` for overdue
- Format dates: `due_date.strftime("%Y-%m-%d")`

## Example Output

```
=== Your Tasks ===
1. Buy groceries - ○ Incomplete (Due: 2024-01-15)
2. Finish report - ○ Incomplete (Due: 2024-01-20)
```

