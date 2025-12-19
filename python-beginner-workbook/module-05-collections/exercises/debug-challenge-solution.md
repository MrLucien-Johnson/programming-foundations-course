# Debug Challenge Solution

**Errors:**
1. `tasks[3]` - IndexError! List has indices 0, 1, 2 (3 items, last index is 2)
2. `customer["email"]` - KeyError! Key "email" doesn't exist

**Fixed:**
```python
tasks = ["Task 1", "Task 2", "Task 3"]
print(tasks[2])  # Last item (index 2)

customer = {"name": "Sarah"}
print(customer.get("email", "Not provided"))  # Safe access
```

