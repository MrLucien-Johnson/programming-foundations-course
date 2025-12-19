# Exercise 2: VAT Calculator

## 🎯 Your Task

Create a calculator that adds VAT (Value Added Tax) to a base price. In the UK, VAT is typically 20%.

## 📝 Steps

1. Create a new file called `vat_calculator.py`

2. Write code that:
   - Asks for the base price (before VAT)
   - Calculates the VAT amount (20% of base price)
   - Calculates the total price (base + VAT)
   - Displays a breakdown showing base price, VAT amount, and total

## 💡 Example Output

```
Enter the base price: £100

=== Price Breakdown ===
Base Price: £100.00
VAT (20%): £20.00
Total Price: £120.00
```

## ✅ Tips

- Use `float(input())` to get the price (allows decimals)
- VAT rate is 0.20 (which is 20%)
- Calculate VAT: `vat_amount = base_price * vat_rate`
- Calculate total: `total = base_price + vat_amount`
- Use f-strings with `:.2f` to show 2 decimal places: `f"£{price:.2f}"`
- Save and run: `python vat_calculator.py`

## 🎓 Learning Goals

By completing this exercise, you'll practice:
- Getting numeric input (`float()`)
- Performing calculations
- Formatting currency output
- Using variables to store intermediate results

## 🔍 Check Your Work

Once you've written your program and it runs successfully, check the solution in `exercise-02-solution.md` to see one possible approach.

**Remember:** This is a real-world calculation used in every shop and business! You're building practical skills! 💪

