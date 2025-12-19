# Exercise 2 Solution

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def display_info(self):
        print(f"{self.name}: £{self.price:.2f}")

product = Product("Laptop", 999.99)
product.display_info()
```

