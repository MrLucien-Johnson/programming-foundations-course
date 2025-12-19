# Exercise 1 Solution: Grade Classifier

## ✅ Sample Solution

```python
# Get student score
score = int(input("Enter student score: "))

# Classify grade
if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print(f"Grade: {grade}")
```

## 📝 Explanation

- Uses `elif` to check multiple conditions in order
- Checks from highest to lowest (90+, then 80+, etc.)
- Uses `else` for scores below 60
- Stores grade in variable for clarity

## 💡 Alternative Approach

```python
score = int(input("Enter student score: "))

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")
```

Both approaches work! Choose what's clearer to you.

