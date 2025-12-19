# Debug Challenge: Find the Errors

## 🎯 Your Task

Look at this broken code and find **all the errors**. Fix them so the program runs correctly!

## 🐛 The Broken Code

```csharp
void CalculateTotal(price, quantity)
{
    double total = price * quantity;
    return total;
}

double result = CalculateTotal(10.50, 3);
Console.WriteLine("Total: " + result);
```

## 📝 Steps

1. **Create a new project:**
   ```bash
   dotnet new console -o DebugChallenge
   cd DebugChallenge
   ```

2. **Try to type this code into `Program.cs`**

3. **Look for errors** - Cursor or VS Code might show red squiggly lines!

4. **Find all the mistakes:**
   - Error 1: _______________
   - Error 2: _______________
   - Error 3: _______________

5. **Fix the errors** and run the program: `dotnet run`

6. **Verify it works** - The program should calculate and display the total

## 💡 Hints

- Check method declaration syntax
- Check parameter types
- Check return type
- Look at each line carefully

## 🎓 Learning Goals

By completing this challenge, you'll practice:
- Reading error messages
- Finding method syntax errors
- Understanding parameter types
- Understanding return types
- Debugging skills

## ✅ Success Criteria

Your program is fixed when:
- ✅ It compiles without errors
- ✅ It runs successfully
- ✅ It correctly calculates the total
- ✅ It displays the result
- ✅ You can explain what each error was

## 🔍 Check Your Work

After you've found and fixed the errors, check `debug-challenge-solution.md` to see:
- What each error was
- Why it was wrong
- How to fix it
- Tips for avoiding these mistakes

## 🎉 Bonus Challenge

After fixing the code, try:
- Adding a method that calculates tax
- Creating a method that formats the output
- Adding validation (check if price and quantity are positive)
- Making the method more flexible

**Remember:** Finding and fixing errors is a superpower! Every programmer does this constantly. You're learning a valuable skill! 💪

