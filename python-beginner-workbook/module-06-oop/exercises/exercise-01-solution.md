# Exercise 1 Solution

```python
class TaskItem:
    def __init__(self, title):
        self.title = title
        self.is_completed = False
    
    def mark_complete(self):
        self.is_completed = True

task = TaskItem("Buy groceries")
task.mark_complete()
```

