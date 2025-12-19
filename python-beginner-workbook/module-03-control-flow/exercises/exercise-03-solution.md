# Exercise 3 Solution: Task Reminder Loop

## ✅ Sample Solution

```python
# Create list of tasks
tasks = [
    "Buy groceries",
    "Finish report",
    "Call client",
    "Review documents"
]

# Display tasks with numbers
print("=== Task Reminders ===")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")

print("\nAll tasks displayed!")
```

## 📝 Explanation

- Creates list of tasks
- Uses `enumerate()` to get both index and task
- `start=1` makes numbering start at 1 (not 0)
- Loops through and displays each task

## 💡 Alternative Approach

```python
tasks = ["Buy groceries", "Finish report", "Call client"]

print("=== Task Reminders ===")
for i in range(len(tasks)):
    print(f"{i + 1}. {tasks[i]}")
```

Both work! `enumerate()` is more Pythonic.

