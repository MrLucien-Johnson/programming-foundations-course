# Exercise 3: Password Validation Method

## 🎯 Your Task

Create a method that checks whether an entered password meets simple length rules. The method should return true or false.

## 📝 Learning Goals

By completing this exercise, you'll practice:
- Creating methods that return boolean values (`bool`)
- Using if/else statements inside methods
- Building validation logic
- Creating reusable validation functions

## 🚀 Steps

1. **Create a new project:**
   ```bash
   dotnet new console -o PasswordValidation
   cd PasswordValidation
   ```

2. **Open `Program.cs` in Cursor or VS Code**

3. **Write a program that:**
   - Creates a method called `IsValidPassword()` (or similar)
   - The method should take one parameter: `string password`
   - The method should check if the password:
     - Has at least 8 characters
     - Has no more than 20 characters
   - The method should return `true` if valid, `false` if invalid
   - In your main program, ask the user for a password
   - Call the method and display whether the password is valid

## 💡 Hints

- Use `static bool` for the return type
- Use `password.Length` to get the password length
- Check if length is between 8 and 20 (inclusive)
- Return `true` if valid, `false` if invalid
- Use the method's return value in an if statement

## 📋 Example Input/Output

**Valid password:**
```
Enter a password: mypassword123
Password is valid!
```

**Too short:**
```
Enter a password: short
Password is invalid! Must be between 8 and 20 characters.
```

**Too long:**
```
Enter a password: thispasswordistoolongandexceedslimit
Password is invalid! Must be between 8 and 20 characters.
```

## ✅ Tips

- Use clear variable names
- Check both conditions (minimum and maximum length)
- Return boolean values (`true` or `false`)
- Use the return value to display appropriate messages

## 🎓 Real-World Connection

This is exactly how password validation works in real applications! Every registration form, login system, and account creation process uses methods like this to ensure passwords meet security requirements. Used in:
- User registration systems
- Account creation forms
- Password reset flows
- Security compliance systems

## 🔍 Bonus Challenge

After completing the basic version, try:
- Adding more validation rules (must contain a number, uppercase letter, etc.)
- Creating separate methods for each validation rule
- Showing which rule failed (too short, too long, etc.)
- Allowing configurable minimum and maximum lengths as parameters

## 🔍 Check Your Work

Once you've written your program:
1. Test with passwords of different lengths
2. Verify it correctly identifies valid passwords (8-20 characters)
3. Verify it correctly rejects invalid passwords
4. Test edge cases (exactly 8 characters, exactly 20 characters)
5. Check the solution in `exercise-03-solution.md` to see one possible approach

**Remember:** If your method correctly validates password length and returns true/false, you've succeeded! 🎉

