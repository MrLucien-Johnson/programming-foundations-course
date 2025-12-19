# Exercise 1: Print Header Method

## 🎯 Your Task

Create a method that prints a standard header for a report. The method should display a formatted header with a title.

## 📝 Learning Goals

By completing this exercise, you'll practice:
- Creating a simple `void` method (no parameters, no return)
- Calling methods from your main program
- Organizing code into reusable blocks
- Building a practical formatting tool

## 🚀 Steps

1. **Create a new project:**
   ```bash
   dotnet new console -o HeaderMethod
   cd HeaderMethod
   ```

2. **Open `Program.cs` in Cursor or VS Code**

3. **Write a program that:**
   - Creates a method called `DisplayHeader()` (or similar name)
   - The method should print a formatted header with:
     - A line of equal signs or dashes
     - A title (like "SALES REPORT" or "MONTHLY SUMMARY")
     - Another line of equal signs or dashes
   - Call the method from your main program
   - Call it multiple times to show it's reusable

## 💡 Hints

- Use `static void` for methods that don't return anything
- Use `Console.WriteLine()` to print lines
- Make the header look professional with consistent formatting
- Call the method by writing its name followed by `()`

## 📋 Example Output

```
========================================
         SALES REPORT
========================================

[Your report content here]

========================================
         SALES REPORT
========================================
```

## ✅ Tips

- Choose a clear, descriptive method name
- Make the header visually appealing
- Test by calling the method multiple times
- Keep the formatting consistent

## 🎓 Real-World Connection

This is exactly how report generators work! Every report needs a header, and instead of writing the header code every time, you create a method and call it. This is used in:
- Business reports
- Financial statements
- Data exports
- Document generation systems

## 🔍 Bonus Challenge

After completing the basic version, try:
- Adding a parameter so you can pass different titles
- Adding a date parameter to show when the report was generated
- Creating a matching footer method
- Adding company name or logo area

## 🔍 Check Your Work

Once you've written your program:
1. Verify the method displays correctly
2. Test calling it multiple times
3. Make sure the formatting looks professional
4. Check the solution in `exercise-01-solution.md` to see one possible approach

**Remember:** If your method displays a formatted header and you can call it multiple times, you've succeeded! 🎉

