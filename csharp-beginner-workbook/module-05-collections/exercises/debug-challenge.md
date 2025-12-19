# Debug Challenge: Find the Errors

## 🎯 Your Task

Look at this broken code and find **all the errors**. Fix them so the program runs correctly!

## 🐛 The Broken Code

```csharp
List<string> names = new List<string>();
names.Add("Alice");
names.Add("Bob");
names.Add("Charlie");

for (int i = 0; i <= names.Count; i++)
{
    Console.WriteLine(names[i]);
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

5. **Fix the errors** and run the program: `dotnet run`

6. **Verify it works** - The program should display all three names without errors

## 💡 Hints

- Think about array/list bounds
- Remember: indexes start at 0
- What's the last valid index for a list with 3 items?
- Check the loop condition carefully

## 🎓 Learning Goals

By completing this challenge, you'll practice:
- Understanding index bounds
- Finding off-by-one errors
- Understanding how `Count` works
- Debugging loop errors

## ✅ Success Criteria

Your program is fixed when:
- ✅ It compiles without errors
- ✅ It runs successfully
- ✅ It displays all three names exactly once
- ✅ It doesn't crash with an out-of-range error
- ✅ You can explain what each error was

## 🔍 Check Your Work

After you've found and fixed the errors, check `debug-challenge-solution.md` to see:
- What each error was
- Why it was wrong
- How to fix it
- Tips for avoiding these mistakes

## 🎉 Bonus Challenge

After fixing the code, try:
- Using `foreach` instead of `for` loop (easier!)
- Adding more names to the list
- Displaying names with numbers (1. Alice, 2. Bob, etc.)
- Adding a count at the end

**Remember:** Finding and fixing errors is a superpower! Every programmer does this constantly. You're learning a valuable skill! 💪

