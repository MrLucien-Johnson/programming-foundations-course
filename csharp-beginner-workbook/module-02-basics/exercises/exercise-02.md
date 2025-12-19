# Exercise 2: VAT Calculator

## 🎯 Your Task

Build a calculator that asks for a base price and tax rate, then calculates and displays the final price with tax.

## 📝 Learning Goals

By completing this exercise, you'll practice:
- Getting numeric input from users
- Converting strings to decimal numbers (`double.Parse()`)
- Performing calculations (multiplication and addition)
- Formatting numbers for display (`F2` for currency)
- Building a practical calculator tool

## 🚀 Steps

1. **Create a new project:**
   ```bash
   dotnet new console -o VatCalculator
   cd VatCalculator
   ```

2. **Open `Program.cs` in Cursor or VS Code**

3. **Write a program that:**
   - Asks for the base price (before tax)
   - Asks for the tax rate (as a decimal, e.g., 0.20 for 20%)
   - Calculates the tax amount (price × tax rate)
   - Calculates the total (price + tax)
   - Displays all three values nicely formatted

## 💡 Hints

- Use `double.Parse()` to convert price and tax rate (they're decimals)
- Tax amount = base price × tax rate
- Total = base price + tax amount
- Use `{variable:F2}` in string interpolation to format currency with 2 decimal places
- Display the breakdown clearly (base price, tax, total)

## 📋 Example Input/Output

**Example run:**
```
Enter the base price: $100.00
Enter the tax rate (e.g., 0.20 for 20%): 0.20
Base Price: $100.00
Tax: $20.00
Total: $120.00
```

**Another example:**
```
Enter the base price: $29.99
Enter the tax rate (e.g., 0.20 for 20%): 0.15
Base Price: $29.99
Tax: $4.50
Total: $34.49
```

## ✅ Tips

- Make your prompts clear about the format (especially for tax rate)
- Use currency formatting (`F2`) for all money values
- Show the calculation breakdown so users can see how the total was calculated
- Test with different prices and tax rates

## 🎓 Real-World Connection

This is exactly what cash registers and e-commerce sites do! They calculate tax and show customers the breakdown. This is a real-world skill used in retail, accounting, and online shopping systems.

## 🔍 Check Your Work

Once you've written your program:
1. Test it with different prices and tax rates
2. Verify the calculations are correct (use a calculator to double-check)
3. Make sure the output is formatted nicely
4. Check the solution in `exercise-02-solution.md` to see one possible approach

**Remember:** The math should be: tax = price × rate, total = price + tax. If your program does this correctly, you've succeeded! 🎉

