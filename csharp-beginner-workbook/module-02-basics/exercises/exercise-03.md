# Exercise 3: Weekly Pay Estimator

## 🎯 Your Task

Create a program that asks for hours worked and hourly rate, then calculates and displays estimated weekly pay.

## 📝 Learning Goals

By completing this exercise, you'll practice:
- Getting numeric input (hours and rate)
- Converting strings to decimal numbers
- Performing multiplication calculations
- Formatting currency output
- Building a practical payroll tool

## 🚀 Steps

1. **Create a new project:**
   ```bash
   dotnet new console -o PayEstimator
   cd PayEstimator
   ```

2. **Open `Program.cs` in Cursor or VS Code**

3. **Write a program that:**
   - Asks for hours worked this week
   - Asks for hourly rate
   - Calculates weekly pay (hours × rate)
   - Displays the information in a clear format

## 💡 Hints

- Use `double` for both hours and rate (they can be decimals, like 37.5 hours or $15.50/hour)
- Use `double.Parse()` to convert the input
- Weekly pay = hours worked × hourly rate
- Format currency with `F2` for two decimal places
- Display both the inputs and the result

## 📋 Example Input/Output

**Example run:**
```
Enter hours worked this week: 40
Enter your hourly rate: $15.50
Hours Worked: 40
Hourly Rate: $15.50
Weekly Pay: $620.00
```

**Another example:**
```
Enter hours worked this week: 37.5
Enter your hourly rate: $20.00
Hours Worked: 37.5
Hourly Rate: $20.00
Weekly Pay: $750.00
```

## ✅ Tips

- Handle decimal hours (like 37.5 or 40.0)
- Handle decimal rates (like $15.50 or $20.00)
- Format all money values consistently
- Show both inputs and the calculated result
- Test with different values

## 🎓 Real-World Connection

This is exactly how payroll systems calculate weekly pay! Time-tracking systems, HR software, and payroll applications use this exact calculation. This is a real skill used in accounting, HR, and business applications.

## 🔍 Bonus Challenge

After completing the basic version, try adding:
- Display monthly pay estimate (weekly pay × 4)
- Display annual pay estimate (weekly pay × 52)
- Format all values nicely

## 🔍 Check Your Work

Once you've written your program:
1. Test it with different hours and rates
2. Verify the math is correct (hours × rate = pay)
3. Make sure decimal values work correctly
4. Check the solution in `exercise-03-solution.md` to see one possible approach

**Remember:** If your program correctly calculates pay = hours × rate and displays it nicely, you've succeeded! 🎉

