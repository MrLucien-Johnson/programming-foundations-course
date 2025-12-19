# Debug Challenge Solution: Find the Errors

## 🐛 The Broken Code

```python
print("Hello World)
print("This is Python")
print('I'm learning to code')
```

## ❌ The Errors Found

### Error 1: Missing Closing Quote (Line 1)
```python
print("Hello World)  # ❌ Missing closing double quote
```

**Problem:** The string starts with a double quote `"` but ends with a closing parenthesis `)` instead of a closing double quote `"`.

**Should be:**
```python
print("Hello World")  # ✅ Properly closed quotes
```

### Error 2: Actually, Line 2 is correct!
```python
print("This is Python")  # ✅ This line is fine!
```

**Note:** Line 2 doesn't have an error - it's correct!

### Error 3: Quote Conflict (Line 3)
```python
print('I'm learning to code')  # ❌ Single quote conflict
```

**Problem:** The string uses single quotes `'`, but there's an apostrophe in "I'm" which is also a single quote. Python thinks the string ends at the apostrophe, causing an error.

**Solutions:**
- **Option 1:** Use double quotes for the outer string:
  ```python
  print("I'm learning to code")  # ✅ Double quotes outside
  ```

- **Option 2:** Escape the apostrophe:
  ```python
  print('I\'m learning to code')  # ✅ Escaped apostrophe
  ```

## ✅ The Fixed Code

Here's the corrected version:

```python
print("Hello World")
print("This is Python")
print("I'm learning to code")
```

## 📝 Explanation of Common Errors

### 1. Unmatched Quotes
- **What it is:** Starting a quote but not closing it
- **Why it happens:** Forgetting the closing quote
- **How to fix:** Always match opening and closing quotes

### 2. Quote Conflicts
- **What it is:** Using the same quote type inside and outside
- **Why it happens:** Apostrophes in text conflict with single quotes
- **How to fix:** Use double quotes for strings with apostrophes, or escape the apostrophe

## 💡 Tips for Avoiding These Errors

1. **Match your quotes** - If you start with `"`, end with `"`
2. **Use double quotes for text with apostrophes** - Easier than escaping
3. **Check each line** - Look for opening and closing quotes
4. **Use your editor's syntax highlighting** - It will show errors in red

## 🎯 Common Error Messages

If you run the broken code, you might see:

```
SyntaxError: EOL while scanning string literal
```

This means Python found the end of the line (`EOL` = End Of Line) while still looking for the closing quote.

## ✅ Practice

Try finding the errors in this code:

```python
print("Hello)
print('It's a beautiful day')
print("Goodbye")
```

**How many errors can you find?** (Answer: 2)

