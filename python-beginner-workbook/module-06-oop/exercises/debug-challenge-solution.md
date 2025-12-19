# Debug Challenge Solution

**Errors:**
1. Missing `self` in `__init__`: `def __init__(title):` → `def __init__(self, title):`
2. Missing `self` in `display`: `def display():` → `def display(self):`

**Fixed:**
```python
class Task:
    def __init__(self, title):
        self.title = title
    
    def display(self):
        print(self.title)
```

