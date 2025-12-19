# Enhancement 5: Save/Load Tasks to JSON File

Add the ability to save tasks to a file and load them when the program starts.

## Steps

1. **Add JSON import:**
   ```python
   import json
   ```

2. **Modify `task_manager.py`:**
   - Add `save_to_file(filename)` method
   - Add `load_from_file(filename)` method
   - Call `load_from_file()` in constructor
   - Call `save_to_file()` when tasks change

3. **Modify `main.py`:**
   - Save tasks before exiting
   - Load tasks when starting

## Example Code Structure

```python
def save_to_file(self, filename):
    tasks_data = []
    for task in self.tasks:
        tasks_data.append({
            "title": task.title,
            "is_completed": task.is_completed
        })
    with open(filename, 'w') as f:
        json.dump(tasks_data, f)

def load_from_file(self, filename):
    try:
        with open(filename, 'r') as f:
            tasks_data = json.load(f)
            for task_data in tasks_data:
                task = TaskItem(task_data["title"])
                if task_data["is_completed"]:
                    task.mark_complete()
                self.tasks.append(task)
    except FileNotFoundError:
        pass  # File doesn't exist yet, that's okay
```

## Tips

- Handle file not found (first run)
- Save after each change or when exiting
- Use a simple filename like "tasks.json"

