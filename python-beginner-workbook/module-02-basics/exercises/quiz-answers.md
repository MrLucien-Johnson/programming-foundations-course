# Module 2 Quiz Answers

## Question 1: What does `input()` always return?
**Answer: B** - A string (text)

**Explanation:** `input()` always returns a string, even if the user types a number. You must convert it using `int()` or `float()` if you need a number.

**Example:**
```python
age = input("Enter age: ")  # Returns string "25", not number 25
age = int(input("Enter age: "))  # Converts to integer 25
```

---

## Question 2: How do you convert a string to an integer in Python?
**Answer: B** - `int()`

**Explanation:** Use `int()` to convert a string to an integer (whole number). Use `float()` for decimal numbers.

**Example:**
```python
age_text = "25"
age = int(age_text)  # Converts "25" to 25
```

---

## Question 3: What is the correct way to create an f-string?
**Answer: B** - `f"Hello {name}"`

**Explanation:** f-strings start with `f` before the quotes, then use `{}` to embed variables.

**Example:**
```python
name = "Sarah"
message = f"Hello {name}"  # ✅ Correct
message = "Hello {name}"   # ❌ Wrong - no f, won't substitute
```

---

## Question 4: True or False: Python requires you to declare variable types before using them.
**Answer: False**

**Explanation:** Python is dynamically typed - you don't need to declare types. Python figures out the type automatically based on the value you assign.

**Example:**
```python
name = "Sarah"  # Python knows this is a string
age = 25        # Python knows this is an integer
```

**Note:** Some languages (like C#) require type declarations, but Python doesn't!

---

## Question 5: What happens if you try to do math with a string (like `"5" + 3`)?
**Answer: B** - You get an error

**Explanation:** You cannot do math operations between strings and numbers. Python will raise a `TypeError`. You must convert the string to a number first.

**Example:**
```python
result = "5" + 3  # ❌ TypeError!
result = int("5") + 3  # ✅ Works: 8
```

**Note:** `"5" + "3"` would give `"53"` (string concatenation), but that's not math!

---

## 🎯 How Did You Do?

- **5/5 correct:** Excellent! You understand the basics well. You're ready for Module 3! 🎉
- **3-4/5 correct:** Good work! Review the questions you missed. You're on the right track! 👍
- **0-2/5 correct:** No worries! Review Module 2 and try again. Understanding comes with practice. 💪

## 💡 Key Takeaways

1. **`input()` returns strings** - Always convert with `int()` or `float()` for numbers
2. **f-strings use `f` prefix** - Start with `f` before quotes
3. **Python is dynamically typed** - No need to declare types
4. **Type errors are common** - Convert strings before math operations
5. **Practice makes perfect** - Keep coding and you'll get better!

## 🚀 Next Steps

Now that you've completed Module 2:
- ✅ You understand variables and data types
- ✅ You can get input from users
- ✅ You can do calculations
- ✅ You can format output with f-strings
- ✅ You're ready for Module 3!

**Keep going!** Module 3 will teach you about control flow (if/else and loops). You're building a strong foundation! 💪

