# Exercise 1 Solution: Name & Age Summary

## ✅ Sample Solution

Here's one way to solve this exercise:

```python
# Get user's name
name = input("Enter your name: ")

# Get user's age (convert to integer)
age = int(input("Enter your age: "))

# Display summary
print(f"\nHello, {name}!")
print(f"You are currently {age} years old.")
print(f"In 10 years, you'll be {age + 10} years old.")
```

## 📝 Explanation

- **Line 2:** Gets the name using `input()` - returns a string
- **Line 5:** Gets the age and converts it to an integer using `int()`
- **Line 8:** Uses f-string to display greeting with name
- **Line 9:** Shows current age
- **Line 10:** Calculates and shows age in 10 years (`age + 10`)

## 💡 Important Points

- `input()` always returns a string, so we need `int()` to convert age
- f-strings make it easy to embed variables: `f"Hello, {name}!"`
- We can do math directly in f-strings: `{age + 10}`
- The `\n` creates a blank line for better formatting

## 🎯 Your Solution vs This Solution

**Remember:** There are many correct ways to solve this! Your solution might:
- Use different variable names
- Have different formatting
- Calculate age differently

**What matters:** Does your program run? Does it show the information correctly? If yes, you succeeded! 🎉

## 🚀 Try This Variation

Want to make it more interesting? Try this:

```python
name = input("Enter your name: ")
age = int(input("Enter your age: "))

print(f"\n=== Personal Summary ===")
print(f"Name: {name}")
print(f"Current Age: {age}")
print(f"Age in 10 years: {age + 10}")
print(f"Age in 20 years: {age + 20}")
print(f"Age in 50 years: {age + 50}")
```

## ✅ Next Steps

- Run your solution and make sure it works
- Try modifying it with different calculations
- Move on to Exercise 2 when you're ready!

