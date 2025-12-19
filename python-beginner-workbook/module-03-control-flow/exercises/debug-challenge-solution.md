# Debug Challenge Solution

## 🐛 Errors Found

1. **Missing closing parenthesis** - Line 1: `input("Enter age: ")` missing `)`
2. **Missing colon** - Line 2: `if age >= 18:` missing `:`
3. **Missing indentation** - Line 3: `print("Adult")` not indented
4. **Missing colon** - Line 4: `else:` missing `:`
5. **Missing colon** - Line 8: `while count < 5:` missing `:`
6. **Infinite loop** - Missing `count += 1` to update counter
7. **Missing indentation** - Line 12: `print(i)` not indented

## ✅ Fixed Code

```python
age = int(input("Enter age: "))
if age >= 18:
    print("Adult")
else:
    print("Minor")

count = 0
while count < 5:
    print(count)
    count += 1  # Added increment

for i in range(5):
    print(i)
```

## 💡 Common Mistakes

- Missing colons after if/else/while/for
- Missing indentation (Python uses spaces!)
- Forgetting to update loop counters
- Missing closing parentheses

