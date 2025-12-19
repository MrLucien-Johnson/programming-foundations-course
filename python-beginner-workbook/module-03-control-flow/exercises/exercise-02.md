# Exercise 2: Login Attempt Limit

## 🎯 Your Task

Create a program that limits login attempts using a while loop. Give the user 3 attempts to enter the correct password.

## 📝 Steps

1. Create a new file called `login_limit.py`

2. Write code that:
   - Sets a correct password (e.g., "password123")
   - Uses a while loop to give 3 attempts
   - Asks for password each time
   - Tells user if password is correct or wrong
   - Stops if password is correct or after 3 attempts

## 💡 Example Output

```
Enter password: wrong
❌ Incorrect password. Attempts remaining: 2
Enter password: also_wrong
❌ Incorrect password. Attempts remaining: 1
Enter password: password123
✓ Login successful!
```

## ✅ Tips

- Use a counter variable to track attempts
- Use `break` to exit loop early if password is correct
- Remember to update the counter each iteration
- Be careful not to create an infinite loop!

## 🎓 Learning Goals

By completing this exercise, you'll practice:
- Using while loops
- Tracking attempts with counters
- Using break to exit loops early
- Input validation

## 🔍 Check Your Work

Once you've written your program and it runs successfully, check the solution in `exercise-02-solution.md`.

**Remember:** This is how real login systems work! You're building practical skills! 💪

