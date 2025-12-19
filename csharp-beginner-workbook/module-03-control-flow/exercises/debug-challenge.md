# Debug Challenge: Find the Errors

## 🎯 Your Task

Look at this broken code and find **all the errors**. Fix them so the program runs correctly!

## 🐛 The Broken Code

```csharp
int age = 25;
if age >= 18
{
    Console.WriteLine("Adult");
}
else
    Console.WriteLine("Minor");
}

for (int i = 0; i < 5; i++)
    Console.WriteLine(i);
}
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
   - Error 4: _______________

5. **Fix the errors** and run the program: `dotnet run`

6. **Verify it works** - The program should check age and count from 0 to 4

## 💡 Hints

- Check if statements - are they formatted correctly?
- Check for missing punctuation
- Check for extra or missing braces `{ }`
- Look at each line carefully

## 🎓 Learning Goals

By completing this challenge, you'll practice:
- Reading error messages
- Finding syntax errors
- Understanding C# if statement and loop syntax
- Debugging skills

## ✅ Success Criteria

Your program is fixed when:
- ✅ It compiles without errors
- ✅ It runs successfully
- ✅ It correctly checks the age
- ✅ It correctly counts from 0 to 4
- ✅ You can explain what each error was

## 🔍 Check Your Work

After you've found and fixed the errors, check `debug-challenge-solution.md` to see:
- What each error was
- Why it was wrong
- How to fix it
- Tips for avoiding these mistakes

## 🎉 Bonus Challenge

After fixing the code, try:
- Adding more conditions to the if statement
- Changing the loop to count backwards
- Adding a message after the loop completes
- Making the age come from user input

**Remember:** Finding and fixing errors is a superpower! Every programmer does this constantly. You're learning a valuable skill! 💪

