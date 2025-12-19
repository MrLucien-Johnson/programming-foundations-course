# Exercise 2 Solution: Login Attempt Limit

## ✅ Sample Solution

```python
correct_password = "password123"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    password = input("Enter password: ")
    
    if password == correct_password:
        print("✓ Login successful!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"❌ Incorrect password. Attempts remaining: {remaining}")
        else:
            print("❌ Access denied. Too many failed attempts.")
```

## 📝 Explanation

- Uses `while` loop with attempt counter
- Checks password each iteration
- Uses `break` to exit early if correct
- Updates counter each time password is wrong
- Shows remaining attempts

## 💡 Key Points

- `attempts += 1` is same as `attempts = attempts + 1`
- `break` exits the loop immediately
- Counter prevents infinite loop

