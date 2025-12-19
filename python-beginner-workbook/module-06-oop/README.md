# Module 6: Intro to Object-Oriented Programming

## 🎯 What You'll Learn

By the end of this module, you will be able to:
- Understand what classes and objects are
- Create your own classes using `class`
- Define properties (attributes) and methods
- Use `__init__` constructor
- Understand `self` parameter
- Create objects (instances) from classes
- **Build something real:** Task class, Product class, Customer class

## 🌍 Real-World Connection

OOP organizes code by modeling real things:
- **Class** = Blueprint (car design)
- **Object** = Instance (actual car)
- **Properties** = Characteristics (color, model)
- **Methods** = Actions (drive, brake)

Used in every professional application!

## 💪 Welcome & Motivation

Congratulations on completing Module 5! Now we'll learn to **organize data and behavior together**.

This is how professional developers write code - organized into classes that model real things.

## 📖 Part 1: Classes and Objects

### What is a Class?

A class is a blueprint for creating objects:

```python
class Task:
    def __init__(self, title):
        self.title = title
        self.is_completed = False
    
    def mark_complete(self):
        self.is_completed = True
    
    def display(self):
        status = "✓" if self.is_completed else "○"
        print(f"{status} {self.title}")
```

### Creating Objects

```python
# Create objects from the class
task1 = Task("Buy groceries")
task2 = Task("Finish report")

# Use the objects
task1.display()  # ○ Buy groceries
task1.mark_complete()
task1.display()  # ✓ Buy groceries
```

### Key Concepts

- `__init__` - Constructor (runs when object is created)
- `self` - Reference to the object itself
- Properties - Data stored in the object (`self.title`)
- Methods - Functions that belong to the object

## 💻 Step-by-Step Mini Programs

### Mini Program 1: Simple Task Class

```python
class Task:
    def __init__(self, title):
        self.title = title
        self.is_completed = False
    
    def mark_complete(self):
        self.is_completed = True

task = Task("Buy groceries")
print(task.title)  # Buy groceries
task.mark_complete()
print(task.is_completed)  # True
```

### Mini Program 2: Product Class

```python
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def display_info(self):
        print(f"{self.name}: £{self.price:.2f}")

product = Product("Laptop", 999.99)
product.display_info()  # Laptop: £999.99
```

### Mini Program 3: Customer Class

```python
class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display(self):
        print(f"Customer: {self.name} ({self.email})")

customer = Customer("Sarah", "sarah@example.com")
customer.display()
```

## 🎓 Exercises

- **Exercise 1:** TaskItem Class
- **Exercise 2:** Product Class with Constructor
- **Exercise 3:** Customer Class with Method

See `exercises/` folder for details.

## 🐛 Debug Challenge

Find errors in class code. See `exercises/debug-challenge.md`

## 🧪 Quiz

Test your understanding. See `exercises/quiz.md`

## 🎉 What's Next?

**Next:** Module 7 - Task Tracker Project (combines everything!)

---

**Remember:** OOP organizes code professionally. You're writing code like the pros! 💪
