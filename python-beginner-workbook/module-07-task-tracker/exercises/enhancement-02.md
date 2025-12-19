# Enhancement 2: Add Task Categories

Add category functionality to tasks. Tasks can belong to categories like "Work", "Personal", "Shopping", etc.

## Steps

1. **Modify `task_item.py`:**
   - Add a `category` property
   - Update constructor to accept category
   - Update `display_info()` to show category

2. **Modify `task_manager.py`:**
   - Update `add_task()` to ask for category
   - Add method `list_tasks_by_category(category)` to filter tasks

3. **Modify `main.py`:**
   - Add menu option "Filter by Category"
   - Let user choose a category to filter by

## Example Output

```
=== Your Tasks ===
1. Buy groceries - ○ Incomplete [Shopping]
2. Finish report - ○ Incomplete [Work]

=== Filter by Category ===
Enter category: Work

=== Work Tasks ===
2. Finish report - ○ Incomplete [Work]
```

