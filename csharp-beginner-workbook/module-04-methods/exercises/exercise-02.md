# Exercise 2: Discount Calculation Method

## 🎯 Your Task

Create a method that calculates and returns a discounted price. The method should take the original price and discount percentage as parameters.

## 📝 Learning Goals

By completing this exercise, you'll practice:
- Creating methods with parameters
- Creating methods that return values
- Performing calculations inside methods
- Building a reusable calculation tool

## 🚀 Steps

1. **Create a new project:**
   ```bash
   dotnet new console -o DiscountMethod
   cd DiscountMethod
   ```

2. **Open `Program.cs` in Cursor or VS Code**

3. **Write a program that:**
   - Creates a method called `CalculateDiscount()` (or similar)
   - The method should take two parameters:
     - `double originalPrice` - the original price
     - `double discountPercent` - the discount percentage (e.g., 0.20 for 20%)
   - The method should calculate the discount amount
   - The method should return the final price after discount
   - Call the method from your main program with different prices and discounts
   - Display the results

## 💡 Hints

- Use `static double` for the return type (since prices are decimals)
- Calculate discount: `discountAmount = originalPrice * discountPercent`
- Calculate final price: `finalPrice = originalPrice - discountAmount`
- Use `return` to send the result back
- Format currency output with `F2` for 2 decimal places

## 📋 Example Input/Output

```
Enter original price: $100.00
Enter discount percentage (e.g., 0.20 for 20%): 0.15
Original Price: $100.00
Discount (15%): $15.00
Final Price: $85.00
```

## ✅ Tips

- Make parameter names clear and descriptive
- Calculate discount amount first, then subtract from original
- Test with different discount percentages
- Format all currency values consistently

## 🎓 Real-World Connection

This is exactly how e-commerce discount systems work! Every time a customer applies a discount code or qualifies for a sale, the system uses a method like this to calculate the final price. Used in:
- Online shopping carts
- Point-of-sale systems
- Promotional campaigns
- Membership discount programs

## 🔍 Bonus Challenge

After completing the basic version, try:
- Adding validation (discount can't be negative or over 100%)
- Creating a method that also displays the breakdown
- Adding multiple discount tiers (if price > X, apply Y% discount)
- Calculating savings amount separately

## 🔍 Check Your Work

Once you've written your program:
1. Test with different prices and discount percentages
2. Verify the calculations are correct (use a calculator to double-check)
3. Make sure the method returns the correct value
4. Check the solution in `exercise-02-solution.md` to see one possible approach

**Remember:** If your method correctly calculates discounted prices and returns the result, you've succeeded! 🎉

