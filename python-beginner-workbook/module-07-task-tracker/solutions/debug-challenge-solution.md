# Debug Challenge Solution

## Errors Found

1. **Missing Index Conversion:** `index = task_number` should be `index = task_number - 1`
2. **Wrong Condition:** `if index > len(self.tasks):` should be `if 0 <= index < len(self.tasks):`
3. **Missing Completion Check:** Should check if task is already completed
4. **Wrong Message:** Else branch handles invalid index, not already-completed

## Fixed Code

```python
def complete_task(self, task_number):
    index = task_number - 1  # Fixed: Convert to 0-based index
    
    if 0 <= index < len(self.tasks):  # Fixed: Check valid range
        if self.tasks[index].is_completed:  # Fixed: Check if already completed
            print("This task is already completed!")
        else:
            self.tasks[index].mark_complete()
            print(f"✓ Task '{self.tasks[index].title}' marked as complete!")
    else:
        print("Invalid task number. Please try again.")  # Fixed: Correct message
```

