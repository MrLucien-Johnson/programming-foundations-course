# Module 2: Python Basics

## 🎯 What You'll Learn

By the end of this module, you will be able to:
- Store information using variables (like labeled boxes)
- Understand different data types (numbers, text, true/false)
- Get input from users with `input()` and use it in your programs
- Perform calculations with numbers
- Format strings beautifully using f-strings
- **Build something real:** A price calculator with tax, a personalized greeting system, and a wage calculator

## 🌍 Real-World Connection

Variables are like labeled boxes where you store information. In real work, you constantly need to:
- Store customer names
- Calculate prices with tax
- Track quantities and inventory
- Remember user preferences
- Process orders and payments

By the end of this module, you'll build programs that do exactly these things - skills you'll use in almost every programming job. These are the building blocks that every application uses.

## 💪 Welcome & Motivation

Congratulations on completing Module 1! You've already created your first program. Now we're going to make your programs **interactive** and **useful**.

In this module, you'll learn to:
- Store information (variables)
- Ask users for information (`input()`)
- Do calculations (math)
- Display results nicely (f-strings)

Think of it like learning to have a conversation with your program - you ask questions, get answers, do some work, and show results. This is how real applications work!

**Career connection:** Every job application form, shopping cart, and calculator uses these exact skills. You're learning the fundamentals that power the digital world!

## 📖 Part 1: Understanding Variables

### What is a Variable?

Think of a variable like a **labeled box**. You can:
- Put something in it (store a value)
- Look at what's inside (read the value)
- Change what's inside (update the value)
- Give it a name so you remember what it's for

**Real-world analogy:** Like a filing cabinet drawer labeled "Customer Names" - you can put names in, take them out, and change them.

### Creating Variables in Python

Python makes creating variables simple! Unlike some languages, you don't need to declare the type upfront - Python figures it out automatically.

```python
customer_name = "Sarah"
```

Let's break this down:
- `customer_name` - The name (the label on the box)
- `=` - Means "put this value into the variable"
- `"Sarah"` - The value (what's inside the box)

**Notice:** No semicolon needed! Python uses line breaks instead.

### Python's Dynamic Typing

Python is **dynamically typed** - this means Python figures out what type of data you're storing automatically. You don't need to tell it "this is text" or "this is a number" - Python knows!

```python
name = "Sarah"      # Python knows this is text (string)
age = 25            # Python knows this is a whole number (int)
price = 29.99       # Python knows this is a decimal number (float)
```

This makes Python easier to learn and write!

### Basic Data Types

Python has different types of "boxes" for different kinds of information:

#### 1. `int` - Whole Numbers
```python
age = 25
quantity = 100
temperature = -5
```
- Use for: ages, counts, quantities, IDs
- **Real-world:** Customer age, order quantity, employee ID

#### 2. `float` - Decimal Numbers
```python
price = 29.99
weight = 1.5
temperature = 98.6
```
- Use for: prices, measurements, percentages
- **Real-world:** Product prices, weights, tax rates

#### 3. `str` - Text (Strings)
```python
name = "John"
email = "john@example.com"
message = "Hello, World!"
```
- Use for: names, addresses, messages, any text
- **Real-world:** Customer names, product descriptions, email addresses
- **Note:** Can use single `'` or double `"` quotes - both work!

#### 4. `bool` - True or False
```python
is_vip = True
is_complete = False
has_discount = True
```
- Use for: yes/no questions, on/off states, flags
- **Real-world:** Is customer a VIP? Is order complete? Does product have discount?
- **Note:** Must be `True` or `False` (capital T and F!)

### Example: Storing Customer Information

```python
customer_name = "Sarah Johnson"
customer_age = 32
order_total = 149.99
is_vip = True
```

**Real-world connection:** This is exactly how customer databases store information - each piece of data has a type and a value.

## 📖 Part 2: Getting Input from Users

### `input()` - Asking for Information

So far, your programs only display messages. Now let's make them **ask questions** and **remember the answers**.

`input()` waits for the user to type something and press Enter, then gives you what they typed as a string.

### Example 1: Asking for a Name

```python
name = input("Enter your name: ")
print(f"Hello, {name}!")
```

**What happens:**
1. Program displays: "Enter your name: "
2. Program waits (cursor blinks)
3. User types: "Sarah" and presses Enter
4. Program stores "Sarah" in the `name` variable
5. Program displays: "Hello, Sarah!"

**Try it yourself:**
1. Create a new file: `greeting.py`
2. Type the code above
3. Run it: `python greeting.py`
4. Type your name when prompted!

### Example 2: Asking for Numbers

Here's the important part: `input()` always gives you **text** (a string), even if the user types a number. You need to **convert** it to a number.

```python
age_text = input("Enter your age: ")
age = int(age_text)  # Convert text to whole number
print(f"You are {age} years old.")
```

**Or more simply:**
```python
age = int(input("Enter your age: "))
print(f"You are {age} years old.")
```

**Converting types:**
- `int()` - Converts to whole number
- `float()` - Converts to decimal number
- `str()` - Converts to text (usually automatic)

### Handling Input Errors

What if the user types something that's not a number? Your program will crash with an error. For now, we'll assume users type correctly. Later modules will teach you to handle errors gracefully.

## 📖 Part 3: Doing Calculations

Python can do all the math you need:

### Basic Math Operations

```python
# Addition
total = 10 + 5          # Result: 15

# Subtraction
difference = 20 - 8      # Result: 12

# Multiplication
product = 6 * 7          # Result: 42

# Division
quotient = 15 / 3        # Result: 5.0 (always gives float)

# Integer division (whole number result)
whole_division = 15 // 3  # Result: 5

# Remainder (modulo)
remainder = 15 % 4       # Result: 3 (15 divided by 4 = 3 remainder 3)

# Power (exponent)
power = 2 ** 3           # Result: 8 (2 to the power of 3)
```

### Order of Operations

Python follows math rules: multiplication and division happen before addition and subtraction. Use parentheses to control order:

```python
result1 = 2 + 3 * 4      # Result: 14 (3*4=12, then +2)
result2 = (2 + 3) * 4    # Result: 20 (2+3=5, then *4)
```

### Real-World Example: Calculating Total Price

```python
price = 29.99
tax_rate = 0.20  # 20% VAT
tax_amount = price * tax_rate
total = price + tax_amount
print(f"Price: £{price:.2f}")
print(f"VAT (20%): £{tax_amount:.2f}")
print(f"Total: £{total:.2f}")
```

## 📖 Part 4: Formatting Strings with f-strings

f-strings (formatted string literals) are Python's way of embedding variables in text. They're easy to read and write!

### Basic f-string

```python
name = "Sarah"
age = 25
message = f"My name is {name} and I'm {age} years old."
print(message)
# Output: My name is Sarah and I'm 25 years old.
```

**How it works:**
- Start with `f` before the quotes
- Put variables inside `{}` curly braces
- Python replaces them with actual values

### Formatting Numbers

```python
price = 29.99
print(f"Price: £{price:.2f}")  # Shows 2 decimal places
# Output: Price: £29.99

total = 1234.5
print(f"Total: £{total:,.2f}")  # Adds commas for thousands
# Output: Total: £1,234.50
```

**Common formatting:**
- `:.2f` - 2 decimal places
- `:,` - Add commas for thousands
- `:d` - Integer (whole number)

### Real-World Example: Order Summary

```python
customer_name = input("Enter customer name: ")
item_price = float(input("Enter item price: £"))
quantity = int(input("Enter quantity: "))

subtotal = item_price * quantity
vat_rate = 0.20
vat_amount = subtotal * vat_rate
total = subtotal + vat_amount

print("\n=== Order Summary ===")
print(f"Customer: {customer_name}")
print(f"Item Price: £{item_price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: £{subtotal:.2f}")
print(f"VAT (20%): £{vat_amount:.2f}")
print(f"Total: £{total:.2f}")
```

## 💻 Step-by-Step Mini Programs

### Mini Program 1: Name & Age Summary

Let's build a program that asks for a name and age, then displays a friendly summary.

**Create a file called `name_age.py`:**

```python
# Get user's name
name = input("Enter your name: ")

# Get user's age (convert to integer)
age = int(input("Enter your age: "))

# Display summary
print(f"\nHello, {name}!")
print(f"You are {age} years old.")
print(f"In 10 years, you'll be {age + 10} years old.")
```

**Run it:**
```bash
python name_age.py
```

**Example output:**
```
Enter your name: Sarah
Enter your age: 25

Hello, Sarah!
You are 25 years old.
In 10 years, you'll be 35 years old.
```

### Mini Program 2: VAT Calculator

Let's build a calculator that adds VAT (Value Added Tax) to a price.

**Create a file called `vat_calculator.py`:**

```python
# Get base price from user
base_price = float(input("Enter the base price: £"))

# Calculate VAT (20% in UK)
vat_rate = 0.20
vat_amount = base_price * vat_rate

# Calculate total
total = base_price + vat_amount

# Display results
print("\n=== Price Breakdown ===")
print(f"Base Price: £{base_price:.2f}")
print(f"VAT (20%): £{vat_amount:.2f}")
print(f"Total Price: £{total:.2f}")
```

**Run it:**
```bash
python vat_calculator.py
```

**Example output:**
```
Enter the base price: £100

=== Price Breakdown ===
Base Price: £100.00
VAT (20%): £20.00
Total Price: £120.00
```

### Mini Program 3: Weekly Pay Estimator

Let's build a calculator that estimates weekly pay from hours worked and hourly rate.

**Create a file called `pay_estimator.py`:**

```python
# Get hours worked
hours = float(input("Enter hours worked this week: "))

# Get hourly rate
rate = float(input("Enter hourly rate: £"))

# Calculate gross pay
gross_pay = hours * rate

# Display results
print("\n=== Weekly Pay Estimate ===")
print(f"Hours Worked: {hours}")
print(f"Hourly Rate: £{rate:.2f}")
print(f"Gross Pay: £{gross_pay:.2f}")
```

**Run it:**
```bash
python pay_estimator.py
```

**Example output:**
```
Enter hours worked this week: 40
Enter hourly rate: £15.50

=== Weekly Pay Estimate ===
Hours Worked: 40.0
Hourly Rate: £15.50
Gross Pay: £620.00
```

## 🎓 Exercises

Now it's time to practice! Try these exercises to build your confidence.

### Exercise 1: Name & Age Summary
Create a program that asks for name and age, then displays a friendly summary.

**See:** `exercises/exercise-01.md`

### Exercise 2: VAT Calculator
Create a calculator that adds VAT to a base price.

**See:** `exercises/exercise-02.md`

### Exercise 3: Weekly Pay Estimator
Create a calculator that estimates weekly pay from hours and rate.

**See:** `exercises/exercise-03.md`

## 🐛 Debug Challenge

Here's some broken code. Can you find and fix the errors?

**See:** `exercises/debug-challenge.md`

## 🧪 Mini Quiz

Test your understanding with these questions:

**See:** `exercises/quiz.md`

## 🎉 What's Next?

Congratulations! You've completed Module 2. You can now:
- ✅ Store data in variables
- ✅ Get input from users
- ✅ Do calculations
- ✅ Format output with f-strings

**Next up:** Module 3 - Control Flow
- Make decisions (if/else)
- Repeat tasks (loops)
- Create interactive menus

You're building real skills! 🚀

---

**Remember:** Every expert was once a beginner. You just learned to make programs interactive - that's huge progress! Keep going! 💪
