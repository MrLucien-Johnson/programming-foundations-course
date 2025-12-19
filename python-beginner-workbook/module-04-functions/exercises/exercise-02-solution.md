# Exercise 2 Solution

```python
def calculate_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

final = calculate_discount(100.00, 15)
print(f"Final price: £{final:.2f}")
```

