# Module 5: Collections

## 🎯 What You'll Learn

By the end of this module, you will be able to:
- Work with lists (ordered collections)
- Work with dictionaries (key-value pairs)
- Add, remove, and access items
- Loop through collections
- Handle common errors (IndexError, KeyError)
- **Build something real:** Shopping lists, customer databases, task managers

## 🌍 Real-World Connection

Collections store groups of data - essential in real work:
- **Lists:** Task lists, customer names, product catalogs
- **Dictionaries:** Customer records, product details, settings
- **Processing:** "Show all customers", "Find product by ID"

## 💪 Welcome & Motivation

Congratulations on completing Module 4! Now we'll learn to work with **groups of data**.

Think of collections like filing cabinets:
- **Lists** = Drawers with numbered folders
- **Dictionaries** = Drawers with labeled folders

## 📖 Part 1: Lists

### Creating Lists

```python
tasks = ["Buy groceries", "Finish report", "Call client"]
numbers = [1, 2, 3, 4, 5]
mixed = ["Alice", 25, True]  # Can mix types
```

### Accessing Items

```python
tasks = ["Buy groceries", "Finish report", "Call client"]
print(tasks[0])  # First item: "Buy groceries"
print(tasks[1])  # Second item: "Finish report"
```

**⚠️ Lists start at 0!** First item is index 0, not 1.

### Adding and Removing

```python
tasks = []
tasks.append("New task")      # Add to end
tasks.insert(0, "First task") # Insert at position
tasks.remove("New task")      # Remove by value
tasks.pop(0)                  # Remove by index
```

### Looping Through Lists

```python
tasks = ["Buy groceries", "Finish report", "Call client"]
for task in tasks:
    print(task)

# With index
for i, task in enumerate(tasks):
    print(f"{i+1}. {task}")
```

## 📖 Part 2: Dictionaries

### Creating Dictionaries

```python
customer = {
    "name": "Sarah",
    "age": 32,
    "email": "sarah@example.com"
}
```

### Accessing Values

```python
print(customer["name"])   # "Sarah"
print(customer["age"])    # 32

# Safe access (won't crash if key doesn't exist)
email = customer.get("email", "No email")
```

### Adding and Updating

```python
customer["phone"] = "123-456-7890"  # Add new key
customer["age"] = 33                # Update existing
```

### Common Errors

```python
# ❌ KeyError if key doesn't exist
print(customer["address"])  # Error!

# ✅ Safe way
address = customer.get("address", "Not provided")
```

## 💻 Step-by-Step Mini Programs

### Mini Program 1: Basic Task List

```python
tasks = ["Buy groceries", "Finish report", "Call client"]
print("=== Your Tasks ===")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")
```

### Mini Program 2: List Manager

```python
shopping_list = []
shopping_list.append("Milk")
shopping_list.append("Bread")
shopping_list.append("Eggs")

print(f"You have {len(shopping_list)} items:")
for item in shopping_list:
    print(f"- {item}")
```

### Mini Program 3: Customer Dictionary

```python
customer = {
    "name": "Sarah",
    "email": "sarah@example.com",
    "phone": "123-456-7890"
}

print("=== Customer Info ===")
print(f"Name: {customer['name']}")
print(f"Email: {customer['email']}")
print(f"Phone: {customer.get('phone', 'Not provided')}")
```

## 🎓 Exercises

- **Exercise 1:** Shopping List
- **Exercise 2:** Customer List with Count
- **Exercise 3:** Dictionary Lookup

See `exercises/` folder for details.

## 🐛 Debug Challenge

Find errors in collection code. See `exercises/debug-challenge.md`

## 🧪 Quiz

Test your understanding. See `exercises/quiz.md`

## 🎉 What's Next?

**Next:** Module 6 - Object-Oriented Programming

---

**Remember:** Collections are how you manage groups of data. Essential for real applications! 💪
