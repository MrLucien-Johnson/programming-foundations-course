# Exercise 3 Solution

```python
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display(self):
        print(f"Customer: {self.name} ({self.email})")

customer = Customer("Sarah", "sarah@example.com")
customer.display()
```

