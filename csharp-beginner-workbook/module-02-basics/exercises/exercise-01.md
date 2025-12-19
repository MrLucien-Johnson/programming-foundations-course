# Exercise 1: Name & Age Summary

## 🎯 Your Task

Create a program that asks for the user's name and age, then prints a friendly summary.

## 📝 Learning Goals

By completing this exercise, you'll practice:
- Using `Console.ReadLine()` to get user input
- Creating variables (`string` and `int`)
- Converting string input to integers using `int.Parse()`
- Using string interpolation to display information
- Building an interactive program

## 🚀 Steps

1. **Create a new project:**
   ```bash
   dotnet new console -o NameAgeSummary
   cd NameAgeSummary
   ```

2. **Open `Program.cs` in Cursor or VS Code**

3. **Write a program that:**
   - Asks for the user's name
   - Stores it in a variable
   - Asks for the user's age
   - Converts the age to a number
   - Displays a friendly summary using both pieces of information

## 💡 Hints

- Use `Console.Write()` or `Console.WriteLine()` to ask questions
- Use `Console.ReadLine()` to get the answers
- Remember: `Console.ReadLine()` gives you text, so you'll need `int.Parse()` for the age
- Use string interpolation (`$"..."`) to combine text and variables

## 📋 Example Input/Output

**Example run:**
```
What's your name? Sarah
How old are you? 28
Hello, Sarah! You are 28 years old.
```

**Another example:**
```
What's your name? John
How old are you? 35
Hello, John! You are 35 years old.
```

## ✅ Tips

- Make your prompts friendly and clear
- Don't forget to convert the age from string to int
- Use string interpolation for clean output
- Test with different names and ages

## 🎓 Real-World Connection

This is like a simple customer information form - asking for basic details and displaying them. Many applications start with this pattern!

## 🔍 Check Your Work

Once you've written your program and it runs successfully:
1. Test it with different names and ages
2. Make sure it handles the input correctly
3. Check the solution in `exercise-01-solution.md` to see one possible approach

**Remember:** There are many ways to solve this! If your program asks for name and age, then displays them correctly, you've succeeded! 🎉

