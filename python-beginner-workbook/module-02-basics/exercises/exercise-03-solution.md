# Exercise 3 Solution: Weekly Pay Estimator

## ✅ Sample Solution

Here's one way to solve this exercise:

```python
# Get hours worked
hours = float(input("Enter hours worked this week: "))

# Get hourly rate
rate = float(input("Enter hourly rate: £"))

# Calculate gross pay
gross_pay = hours * rate

# Display results
print("\n=== Weekly Pay Estimate ===")
print(f"Hours Worked: {hours}")
print(f"Hourly Rate: £{rate:.2f}")
print(f"Gross Pay: £{gross_pay:.2f}")
```

## 📝 Explanation

- **Line 2:** Gets hours using `float()` to allow decimal hours (e.g., 37.5)
- **Line 5:** Gets hourly rate using `float()` for decimal rates
- **Line 8:** Calculates gross pay by multiplying hours × rate
- **Lines 11-14:** Display formatted summary with currency formatting

## 💡 Important Points

- Use `float()` for both inputs to allow decimals
- Gross pay = hours × rate (simple multiplication)
- `:.2f` formats currency to 2 decimal places
- Store the calculation in `gross_pay` variable for clarity

## 🎯 Your Solution vs This Solution

**Remember:** Your solution might:
- Use different variable names
- Have different formatting
- Calculate differently

**What matters:** Does it calculate correctly? Does it display nicely? If yes, you succeeded! 🎉

## 🚀 Try This Variation

Want to add more features? Try this:

```python
hours = float(input("Enter hours worked this week: "))
rate = float(input("Enter hourly rate: £"))

gross_pay = hours * rate

# Calculate daily average (assuming 5-day work week)
daily_average = gross_pay / 5

print("\n=== Weekly Pay Estimate ===")
print(f"Hours Worked: {hours}")
print(f"Hourly Rate: £{rate:.2f}")
print(f"Gross Pay: £{gross_pay:.2f}")
print(f"Daily Average (5-day week): £{daily_average:.2f}")
```

## ✅ Next Steps

- Run your solution and test with different values
- Try the variation above to add more calculations
- You've completed all exercises! Great work! 🎉

