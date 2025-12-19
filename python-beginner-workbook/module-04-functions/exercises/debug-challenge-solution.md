# Debug Challenge Solution

**Errors:**
1. Missing comma: `def calculate_total(price tax_rate):` → `def calculate_total(price, tax_rate):`
2. Missing return value: `return` → `return total`

**Fixed code:**
```python
def calculate_total(price, tax_rate):
    total = price + (price * tax_rate)
    return total

result = calculate_total(100, 0.20)
print(result)  # Output: 120.0
```

