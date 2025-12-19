# example-02-function-with-parameters.py
# Demonstrates functions with parameters

def calculate_total(price, tax_rate=0.20):
    """Calculate total price with tax."""
    tax = price * tax_rate
    total = price + tax
    return total

# Use the function with different prices
order1 = calculate_total(100.00)
order2 = calculate_total(150.00, 0.15)  # Different tax rate

print(f"Order 1 Total: £{order1:.2f}")
print(f"Order 2 Total: £{order2:.2f}")

