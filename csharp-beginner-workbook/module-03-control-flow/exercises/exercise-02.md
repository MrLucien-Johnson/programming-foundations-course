# Exercise 2: Login Attempt Limit

## 🎯 Your Task

Build a program that gives users 3 attempts to enter the correct password using a while loop.

## 📝 Learning Goals

By completing this exercise, you'll practice:
- Using while loops to repeat actions
- Counting attempts
- Checking conditions to control loop execution
- Building a security/validation system

## 🚀 Steps

1. **Create a new project:**
   ```bash
   dotnet new console -o LoginAttempts
   cd LoginAttempts
   ```

2. **Open `Program.cs` in Cursor or VS Code**

3. **Write a program that:**
   - Sets a correct password (e.g., "secret123")
   - Uses a while loop to give the user up to 3 attempts
   - Asks for the password each time
   - Checks if the password is correct
   - If correct: Display success message and exit
   - If incorrect: Show remaining attempts and try again
   - After 3 failed attempts: Display "Access denied" message

## 💡 Hints

- Use a counter variable to track attempts (start at 0 or 1)
- Use `while (attempts < 3)` to limit attempts
- Increment the counter after each attempt (`attempts++`)
- Use `break` to exit the loop early if password is correct
- Or use a boolean flag to control the loop

## 📋 Example Input/Output

**Successful login:**
```
Enter password: wrong
Incorrect! Attempts remaining: 2
Enter password: secret123
Access granted! Welcome!
```

**Failed login:**
```
Enter password: wrong1
Incorrect! Attempts remaining: 2
Enter password: wrong2
Incorrect! Attempts remaining: 1
Enter password: wrong3
Access denied. Too many failed attempts.
```

## ✅ Tips

- Keep track of attempts with a counter
- Show remaining attempts clearly
- Exit the loop immediately when password is correct
- Make your messages clear and helpful

## 🎓 Real-World Connection

This is exactly how login systems work! Most applications limit login attempts to prevent brute-force attacks. This pattern is used in:
- Banking applications
- Email systems
- Social media platforms
- Corporate security systems

## 🔍 Bonus Challenge

After completing the basic version, try adding:
- Lock the account after 3 failed attempts (show a message)
- Reset attempts counter after successful login
- Add a delay between attempts (simulate security)
- Track total failed attempts across sessions

## 🔍 Check Your Work

Once you've written your program:
1. Test with correct password on first try
2. Test with correct password on second try
3. Test with all 3 attempts incorrect
4. Verify the loop stops at exactly 3 attempts
5. Check the solution in `exercise-02-solution.md` to see one possible approach

**Remember:** If your program correctly limits attempts and checks the password, you've succeeded! 🎉

