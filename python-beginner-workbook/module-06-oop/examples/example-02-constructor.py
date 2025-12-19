# example-02-constructor.py
# Demonstrates constructor with parameters

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def display_info(self):
        print(f"{self.name}: £{self.price:.2f}")

# Create products
laptop = Product("Laptop", 999.99)
mouse = Product("Mouse", 29.99)

laptop.display_info()
mouse.display_info()

