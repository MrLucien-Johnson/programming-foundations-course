# Debug Challenge: Find the Errors

Look at this broken `complete_task` method and find **all the errors**.

## The Broken Code

```python
def complete_task(self, task_number):
    index = task_number  # Should convert to 0-based index
    
    if index > len(self.tasks):  # Wrong condition
        self.tasks[index].mark_complete()
        print(f"Task completed!")
    else:
        print("Task already completed!")  # Wrong message
```

## Find All Mistakes

1. Error 1: _______________
2. Error 2: _______________
3. Error 3: _______________
4. Error 4: _______________

## Check Your Work

See `solutions/debug-challenge-solution.md` for the solution.

