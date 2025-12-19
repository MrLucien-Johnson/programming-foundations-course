# Module 4: Functions

## 🎯 What You'll Learn

By the end of this module, you will be able to:
- Create reusable functions using `def`
- Pass information to functions using parameters
- Get results back from functions using `return`
- Understand function scope (where variables work)
- Organize code into logical, reusable sections
- **Build something real:** Reusable helpers for calculations, validations, and formatting

## 🌍 Real-World Connection

Functions are like reusable recipes or Standard Operating Procedures (SOPs):
- Write once, use many times
- Save time and reduce mistakes
- Make code easier to understand and fix
- Used in every professional application

**Real-world analogy:** Like a recipe card - write it once, follow it whenever you need that dish, use different ingredients (parameters) each time.

## 💪 Welcome & Motivation

Congratulations on completing Module 3! Now we're going to make your code **organized** and **reusable**.

Think of functions like this:
- **Without functions:** Writing the same code over and over
- **With functions:** Write once, reuse everywhere

This makes your programs shorter, easier to fix, and less error-prone!

## 📖 Part 1: Creating Functions

### Basic Function Syntax

```python
def say_hello():
    print("Hello!")
    print("Welcome to Python!")

# Call the function
say_hello()
```

**How it works:**
- `def` - Define a function
- `say_hello` - Function name
- `()` - Parameters go here (empty for now)
- `:` - Colon starts the function body
- Indented code - What the function does

### Functions with Parameters

```python
def greet(name):
    print(f"Hello, {name}!")

greet("Sarah")  # Output: Hello, Sarah!
greet("Bob")    # Output: Hello, Bob!
```

### Functions with Return Values

```python
def add_numbers(a, b):
    result = a + b
    return result

total = add_numbers(5, 3)
print(total)  # Output: 8
```

**Key points:**
- `return` sends a value back
- Function stops when it hits `return`
- You can use the returned value

### Real-World Example: Price Calculator

```python
def calculate_total(price, tax_rate=0.20):
    """Calculate total price with tax."""
    tax = price * tax_rate
    total = price + tax
    return total

# Use the function
order1 = calculate_total(100.00)
order2 = calculate_total(150.00, 0.15)  # Different tax rate
print(f"Order 1: £{order1:.2f}")
print(f"Order 2: £{order2:.2f}")
```

## 📖 Part 2: Function Scope

Variables inside functions are **local** - they only exist inside that function:

```python
def calculate():
    x = 10  # Local variable
    return x * 2

result = calculate()
# print(x)  # ❌ Error! x doesn't exist here
```

## 💻 Step-by-Step Mini Programs

### Mini Program 1: Simple Header Function

```python
def print_header(title):
    print("=" * 40)
    print(title)
    print("=" * 40)

print_header("Order Summary")
print_header("Customer Information")
```

### Mini Program 2: Discount Calculator Function

```python
def calculate_discount(price, discount_percent):
    discount_amount = price * (discount_percent / 100)
    final_price = price - discount_amount
    return final_price

original = 100.00
discounted = calculate_discount(original, 15)
print(f"Original: £{original:.2f}")
print(f"After 15% discount: £{discounted:.2f}")
```

### Mini Program 3: Validation Function

```python
def is_valid_password(password):
    """Check if password is at least 8 characters."""
    if len(password) >= 8:
        return True
    else:
        return False

password = input("Enter password: ")
if is_valid_password(password):
    print("✓ Password is valid!")
else:
    print("❌ Password must be at least 8 characters.")
```

## 🎓 Exercises

- **Exercise 1:** Print Header Function
- **Exercise 2:** Discount Calculation Function
- **Exercise 3:** Password Validation Function

See `exercises/` folder for details.

## 🐛 Debug Challenge

Find errors in broken function code. See `exercises/debug-challenge.md`

## 🧪 Quiz

Test your understanding. See `exercises/quiz.md`

## 🎉 What's Next?

**Next:** Module 5 - Collections (Lists & Dictionaries)

---

**Remember:** Functions make code reusable and organized. You're writing professional-style code! 💪
