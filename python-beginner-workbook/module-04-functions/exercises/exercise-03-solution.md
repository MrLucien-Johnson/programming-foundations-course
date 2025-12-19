# Exercise 3 Solution

```python
def is_valid_password(password):
    if len(password) >= 8:
        return True
    else:
        return False

# Or more simply:
def is_valid_password(password):
    return len(password) >= 8
```

