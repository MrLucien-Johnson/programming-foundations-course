# Module 3: Control Flow

## 🎯 What You'll Learn

By the end of this module, you will be able to:
- Make decisions in your programs using `if`, `elif`, and `else`
- Use comparison operators (`>`, `<`, `==`, `!=`, `>=`, `<=`)
- Use logical operators (`and`, `or`, `not`)
- Repeat actions using `for` loops
- Repeat actions using `while` loops
- Loop through collections
- **Build something real:** Age verification systems, discount calculators, menu systems, and list processors

## 🌍 Real-World Connection

Control flow is how programs make decisions and repeat tasks - just like in real work:
- **Decisions:** "If customer spends over £100, apply discount"
- **Repeating:** "Process each item in the order list"
- **Menus:** "Show menu until user chooses exit"
- **Validation:** "Check password until correct or 3 attempts"

By the end of this module, you'll build programs that make smart decisions and handle repetitive tasks automatically - exactly what real applications do.

## 💪 Welcome & Motivation

Congratulations on completing Module 2! You can now store data and get user input. Now we're going to make your programs **smart** and **efficient**.

In this module, you'll learn to:
- Make decisions (if/else)
- Repeat tasks (loops)
- Process lists automatically
- Create interactive menus

Think of it like teaching your program to think and work efficiently - instead of doing everything manually, your program will make decisions and repeat tasks automatically!

**Career connection:** Every application uses control flow. Forms validate input, systems process lists, menus guide users. You're learning the logic that powers all software!

## 📖 Part 1: Making Decisions with if/elif/else

### What is Control Flow?

Control flow is how your program decides what to do next. Think of it like a flowchart:
- "If this is true, do that"
- "Otherwise, do something else"
- "Keep doing this until something happens"

### The `if` Statement

The simplest decision: "If something is true, do this."

```python
age = 18
if age >= 18:
    print("You are an adult!")
```

**How it works:**
- `if` - Start of the decision
- `age >= 18` - The condition (is age greater than or equal to 18?)
- `:` - Colon means "here's what to do if true"
- Indented code - What happens if condition is true

**⚠️ IMPORTANT:** Python uses **indentation** (spaces) to show what code belongs to the `if` statement. Use 4 spaces (or 1 tab) for indentation!

### Comparison Operators

Python uses these to compare values:

- `>` - Greater than
- `<` - Less than
- `>=` - Greater than or equal to
- `<=` - Less than or equal to
- `==` - Equal to (note: double equals!)
- `!=` - Not equal to

**Common mistake:** Using `=` instead of `==` for comparison. `=` assigns, `==` compares!

### The `else` Statement

"What to do if the condition is false."

```python
age = 16
if age >= 18:
    print("You are an adult!")
else:
    print("You are a minor.")
```

### The `elif` Statement

"Check another condition if the first one is false."

```python
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: F")
```

**How it works:**
1. Check first condition (score >= 90)
2. If false, check second condition (score >= 80)
3. If false, check third condition (score >= 70)
4. If all false, do else

### Logical Operators

Combine multiple conditions:

- `and` - Both must be true
- `or` - At least one must be true
- `not` - Reverse the condition

```python
age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive!")
    
if age < 18 or not has_license:
    print("You cannot drive.")
```

### Real-World Example: Discount Calculator

```python
total = float(input("Enter order total: £"))

if total >= 100:
    discount = total * 0.10  # 10% discount
    final_total = total - discount
    print(f"Discount applied: £{discount:.2f}")
    print(f"Final total: £{final_total:.2f}")
else:
    print(f"No discount. Total: £{total:.2f}")
```

## 📖 Part 2: Repeating with Loops

### The `for` Loop

Repeat something a specific number of times or for each item in a list.

```python
# Count from 1 to 5
for i in range(1, 6):
    print(i)
```

**Output:**
```
1
2
3
4
5
```

**`range()` function:**
- `range(5)` - 0, 1, 2, 3, 4 (stops before 5)
- `range(1, 6)` - 1, 2, 3, 4, 5 (from 1 to 5)
- `range(0, 10, 2)` - 0, 2, 4, 6, 8 (step by 2)

### Looping Through Lists

```python
tasks = ["Buy groceries", "Finish report", "Call client"]

for task in tasks:
    print(f"Task: {task}")
```

**Output:**
```
Task: Buy groceries
Task: Finish report
Task: Call client
```

### The `while` Loop

Repeat while a condition is true.

```python
count = 0
while count < 5:
    print(f"Count: {count}")
    count = count + 1  # Important: update the counter!
```

**⚠️ WARNING:** Make sure your condition eventually becomes false, or you'll have an **infinite loop**!

### Real-World Example: Menu Loop

```python
running = True

while running:
    print("\n=== Menu ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")
    
    choice = input("Enter choice: ")
    
    if choice == "1":
        print("Adding task...")
    elif choice == "2":
        print("Viewing tasks...")
    elif choice == "3":
        running = False
        print("Goodbye!")
    else:
        print("Invalid choice!")
```

## 📖 Part 3: Common Mistakes and Tips

### Indentation Errors

Python uses indentation to show code structure. Common mistakes:

```python
# ❌ WRONG - No indentation
if age >= 18:
print("Adult")

# ✅ CORRECT - Proper indentation
if age >= 18:
    print("Adult")
```

### Infinite Loops

```python
# ❌ WRONG - Infinite loop!
count = 0
while count < 5:
    print(count)
    # Missing: count = count + 1

# ✅ CORRECT - Updates counter
count = 0
while count < 5:
    print(count)
    count = count + 1
```

### Using `=` Instead of `==`

```python
# ❌ WRONG - This assigns, not compares!
if age = 18:
    print("Adult")

# ✅ CORRECT - This compares
if age == 18:
    print("Adult")
```

## 💻 Step-by-Step Mini Programs

### Mini Program 1: Age Verification

```python
# Get user's age
age = int(input("Enter your age: "))

# Check age and display message
if age >= 18:
    print("You are an adult.")
    print("You can vote and drive!")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
    print("Enjoy being young!")

print("\nThanks for using our age checker!")
```

### Mini Program 2: Discount Calculator

```python
# Get order total
total = float(input("Enter order total: £"))

# Calculate discount based on total
if total >= 200:
    discount_rate = 0.15  # 15% discount
    discount_amount = total * discount_rate
    final_total = total - discount_amount
    print(f"\n🎉 You qualify for 15% discount!")
elif total >= 100:
    discount_rate = 0.10  # 10% discount
    discount_amount = total * discount_rate
    final_total = total - discount_amount
    print(f"\n🎉 You qualify for 10% discount!")
else:
    discount_amount = 0
    final_total = total
    print(f"\nNo discount available.")

# Display results
print(f"Original Total: £{total:.2f}")
if discount_amount > 0:
    print(f"Discount: £{discount_amount:.2f}")
print(f"Final Total: £{final_total:.2f}")
```

### Mini Program 3: Simple Menu Loop

```python
# Menu loop
running = True

while running:
    print("\n=== Task Manager ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Exit")
    
    choice = input("\nEnter your choice (1-3): ")
    
    if choice == "1":
        task = input("Enter task name: ")
        print(f"✓ Added: {task}")
    elif choice == "2":
        print("Your tasks will appear here...")
    elif choice == "3":
        running = False
        print("Goodbye!")
    else:
        print("❌ Invalid choice. Please enter 1, 2, or 3.")
```

## 🎓 Exercises

Now it's time to practice! Try these exercises to build your confidence.

### Exercise 1: Grade Classifier
Create a program that classifies grades using if/elif/else.

**See:** `exercises/exercise-01.md`

### Exercise 2: Login Attempt Limit
Create a program that limits login attempts using a while loop.

**See:** `exercises/exercise-02.md`

### Exercise 3: Task Reminder Loop
Create a program that loops through tasks using a for loop.

**See:** `exercises/exercise-03.md`

## 🐛 Debug Challenge

Here's some broken code. Can you find and fix the errors?

**See:** `exercises/debug-challenge.md`

## 🧪 Mini Quiz

Test your understanding with these questions:

**See:** `exercises/quiz.md`

## 🎉 What's Next?

Congratulations! You've completed Module 3. You can now:
- ✅ Make decisions with if/elif/else
- ✅ Use comparison and logical operators
- ✅ Create for loops
- ✅ Create while loops
- ✅ Build interactive menus

**Next up:** Module 4 - Functions
- Organize code into reusable blocks
- Pass data to functions
- Get results back from functions

You're building real programming skills! 🚀

---

**Remember:** Control flow is the logic that makes programs smart. You've learned a fundamental skill used in every application! Keep going! 💪
