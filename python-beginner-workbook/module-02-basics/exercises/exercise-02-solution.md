# Exercise 2 Solution: VAT Calculator

## ✅ Sample Solution

Here's one way to solve this exercise:

```python
# Get base price from user
base_price = float(input("Enter the base price: £"))

# Calculate VAT (20% in UK)
vat_rate = 0.20
vat_amount = base_price * vat_rate

# Calculate total
total = base_price + vat_amount

# Display results
print("\n=== Price Breakdown ===")
print(f"Base Price: £{base_price:.2f}")
print(f"VAT (20%): £{vat_amount:.2f}")
print(f"Total Price: £{total:.2f}")
```

## 📝 Explanation

- **Line 2:** Gets price using `float(input())` to allow decimals
- **Line 5:** Sets VAT rate as 0.20 (which is 20%)
- **Line 6:** Calculates VAT amount by multiplying base price by rate
- **Line 9:** Calculates total by adding base price and VAT
- **Lines 12-15:** Display formatted results with 2 decimal places

## 💡 Important Points

- Use `float()` instead of `int()` to allow decimal prices
- VAT rate of 0.20 represents 20% (20/100 = 0.20)
- `:.2f` formats numbers to 2 decimal places (currency format)
- Store intermediate values (vat_rate, vat_amount) for clarity

## 🎯 Your Solution vs This Solution

**Remember:** Your solution might:
- Use different variable names
- Calculate in one step: `total = base_price * 1.20`
- Have different formatting

**What matters:** Does it calculate correctly? Does it display nicely? If yes, you succeeded! 🎉

## 🚀 Try This Variation

Want to make it more flexible? Try this:

```python
base_price = float(input("Enter the base price: £"))
vat_rate = float(input("Enter VAT rate (as decimal, e.g., 0.20 for 20%): "))

vat_amount = base_price * vat_rate
total = base_price + vat_amount

print("\n=== Price Breakdown ===")
print(f"Base Price: £{base_price:.2f}")
print(f"VAT ({vat_rate*100:.0f}%): £{vat_amount:.2f}")
print(f"Total Price: £{total:.2f}")
```

## ✅ Next Steps

- Run your solution and test with different prices
- Try the variation above to make it more flexible
- Move on to Exercise 3 when you're ready!

