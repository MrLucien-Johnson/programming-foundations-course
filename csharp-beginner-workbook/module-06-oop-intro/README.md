# Module 6: Intro to Object-Oriented Programming

## 🎯 What You'll Learn

By the end of this module, you will be able to:
- Understand what classes and objects are using simple analogies
- Create your own classes to model real-world things
- Define properties (characteristics) and methods (behaviors) in classes
- Create constructors to initialize objects
- Create objects (instances) from classes
- Use objects in your programs
- **Build something real:** A Task class for task management, a Product class for inventory, and a Customer class for customer management

## 🌍 Real-World Connection

Object-Oriented Programming (OOP) is how professional developers organize code. It lets you model real-world things as code:
- A "Task" class represents tasks (like in task management systems)
- A "Product" class represents products (like in e-commerce systems)
- A "Customer" class represents customers (like in CRM systems)

**Real-world analogy:** Think of OOP like this:
- **Class** = A blueprint for a car (defines what a car has and can do)
- **Object** = An actual car built from that blueprint (a specific car you can use)
- **Properties** = Characteristics (color, model, year)
- **Methods** = Actions (start engine, drive, brake)

This approach:
- Makes code easier to understand (matches how we think about things)
- Makes code reusable (create many tasks from one Task class)
- Makes code maintainable (change the Task class, all tasks update)
- Is used in almost all professional software

By learning OOP, you're learning the same patterns used in:
- Business applications (customer management, order processing)
- Web applications (user accounts, product catalogs)
- Mobile apps (contacts, tasks, settings)
- Game development (characters, items, levels)

## 💪 Welcome & Motivation

Congratulations on completing Module 5! You've learned to work with collections. Now we're going to learn to **organize data and behavior together** - this is how professional software is built.

Think of OOP like this:
- **Without OOP:** Like having a pile of papers with customer names, and separately a list of instructions for what to do with customers
- **With OOP:** Like having organized customer files where each file contains the customer's information AND the actions you can take with that customer

This is where your code starts looking professional. Instead of scattered variables and methods, you'll organize everything into logical units - classes that represent real things.

**Real-world impact:** Every business thinks in terms of "things":
- Tasks (with names, due dates, completion status)
- Products (with names, prices, stock levels)
- Customers (with names, emails, purchase history)
- Orders (with items, totals, dates)

OOP lets you code these "things" exactly as businesses think about them!

## 📖 Part 1: Understanding Classes and Objects

### What is a Class?

A **class** is a blueprint or template. It defines what something **has** (properties) and what it **can do** (methods).

**Real-world analogy:** 
- **Class** = Recipe for chocolate chip cookies
- The recipe defines: ingredients needed (properties) and steps to follow (methods)
- You can use the same recipe to make many batches of cookies

**Code analogy:**
- **Class** = Blueprint for a car
- Defines: color, model, year (properties) and start engine, drive, brake (methods)
- You can create many cars from the same blueprint

### What is an Object?

An **object** is a specific instance created from a class. It's a real thing you can use.

**Real-world analogy:**
- **Object** = An actual batch of cookies you baked using the recipe
- **Object** = A specific car (like "my red Toyota from 2020")

**Code example:**
- **Class** = `Task` (the blueprint)
- **Object** = `task1` (a specific task: "Email client")
- **Object** = `task2` (another specific task: "Finish report")

### Simple Example: Task Class

```csharp
class TaskItem
{
    public string Title { get; set; }
    public bool IsCompleted { get; set; }
}
```

**Breaking it down:**
- `class TaskItem` - This is a class called TaskItem
- `public string Title` - A property (characteristic) - the task's title
- `public bool IsCompleted` - A property - whether the task is done
- `{ get; set; }` - Allows getting and setting the value

**Creating objects from the class:**
```csharp
TaskItem task1 = new TaskItem();
task1.Title = "Email client";
task1.IsCompleted = false;

TaskItem task2 = new TaskItem();
task2.Title = "Finish report";
task2.IsCompleted = true;
```

**Real-world connection:** This is exactly how task management systems work - they have a Task class, and create many Task objects (one for each task).

## 📖 Part 2: Properties - Characteristics of Objects

### What are Properties?

Properties are characteristics that describe an object. Like a car's color, or a task's title.

**Real-world analogy:** 
- Car properties: color, model, year, mileage
- Task properties: title, description, due date, completion status
- Customer properties: name, email, phone number

### Defining Properties

```csharp
class Product
{
    public string Name { get; set; }
    public double Price { get; set; }
    public int StockQuantity { get; set; }
}
```

**Breaking it down:**
- `public` - Can be accessed from outside the class
- `string Name` - Property type and name
- `{ get; set; }` - Can get the value and set (change) the value

**Using properties:**
```csharp
Product apple = new Product();
apple.Name = "Red Apple";
apple.Price = 0.99;
apple.StockQuantity = 50;

Console.WriteLine($"Product: {apple.Name}");
Console.WriteLine($"Price: ${apple.Price}");
```

**Real-world connection:** E-commerce systems use Product classes with properties like this to manage inventory.

## 📖 Part 3: Constructors - Creating Objects Properly

### What is a Constructor?

A **constructor** is a special method that runs when you create an object. It sets up the object with initial values.

**Real-world analogy:** Like filling out a form when you start a new job - you provide your name, department, and start date, and that information is set up for your employee record.

### Creating a Constructor

```csharp
class Product
{
    public string Name { get; set; }
    public double Price { get; set; }
    
    // Constructor - same name as class, no return type
    public Product(string name, double price)
    {
        Name = name;
        Price = price;
    }
}
```

**Breaking it down:**
- `public Product(...)` - Same name as class, this is the constructor
- `string name, double price` - Parameters (information needed to create the object)
- Inside `{ }` - Sets the properties with the provided values

**Using the constructor:**
```csharp
Product apple = new Product("Red Apple", 0.99);
// Name is automatically set to "Red Apple"
// Price is automatically set to 0.99
```

**Why constructors are useful:**
- Ensures objects are created with required information
- Prevents creating incomplete objects
- Makes code cleaner and safer

**Real-world connection:** When you create a new customer account, you must provide name and email - constructors enforce this requirement.

## 📖 Part 4: Methods in Classes - Actions Objects Can Do

### What are Methods in Classes?

Methods inside classes are actions that objects can perform. They belong to the object and can use the object's properties.

**Real-world analogy:**
- Car methods: StartEngine(), Drive(), Brake()
- Task methods: MarkComplete(), DisplayInfo()
- Customer methods: UpgradeToVip(), DisplayProfile()

### Adding Methods to Classes

```csharp
class TaskItem
{
    public string Title { get; set; }
    public bool IsCompleted { get; set; }
    
    // Method that belongs to the class
    public void MarkComplete()
    {
        IsCompleted = true;
    }
    
    public void DisplayInfo()
    {
        string status = IsCompleted ? "✓ Complete" : "○ Incomplete";
        Console.WriteLine($"{Title} - {status}");
    }
}
```

**Using the methods:**
```csharp
TaskItem task = new TaskItem();
task.Title = "Email client";
task.MarkComplete();  // Calls the method
task.DisplayInfo();   // Calls the method
```

**Real-world connection:** Task management systems have methods like MarkComplete(), SetPriority(), AddNote() - all actions you can take with a task.

## 🎓 Step-by-Step Mini Programs

### Mini Program 1: Simple Class

Let's create a simple TaskItem class with properties.

**Step 1:** Create a new project
```bash
dotnet new console -o SimpleClass
cd SimpleClass
```

**Step 2:** Write the program in `Program.cs`:
```csharp
// Define the class
class TaskItem
{
    public string Title { get; set; }
    public bool IsCompleted { get; set; }
}

// Create objects from the class
TaskItem task1 = new TaskItem();
task1.Title = "Buy groceries";
task1.IsCompleted = false;

TaskItem task2 = new TaskItem();
task2.Title = "Finish report";
task2.IsCompleted = true;

// Use the objects
Console.WriteLine("=== Tasks ===");
Console.WriteLine($"Task 1: {task1.Title} - {(task1.IsCompleted ? "Done" : "Todo")}");
Console.WriteLine($"Task 2: {task2.Title} - {(task2.IsCompleted ? "Done" : "Todo")}");
```

**Step 3:** Run it
```bash
dotnet run
```

**What happens:** You create two Task objects, each with its own title and completion status. Notice how you can create many tasks from one Task class!

**Real-world connection:** This is how task management apps store tasks - each task is an object with its own properties.

### Mini Program 2: Class with Constructor

Build a Product class with a constructor that requires name and price.

**Step 1:** Create project
```bash
dotnet new console -o ConstructorExample
cd ConstructorExample
```

**Step 2:** Write the program:
```csharp
class Product
{
    public string Name { get; set; }
    public double Price { get; set; }
    
    // Constructor - requires name and price
    public Product(string name, double price)
    {
        Name = name;
        Price = price;
    }
}

// Create products using the constructor
Product apple = new Product("Red Apple", 0.99);
Product bread = new Product("Whole Wheat Bread", 2.50);
Product milk = new Product("Whole Milk", 3.99);

Console.WriteLine("=== Products ===");
Console.WriteLine($"{apple.Name}: ${apple.Price:F2}");
Console.WriteLine($"{bread.Name}: ${bread.Price:F2}");
Console.WriteLine($"{milk.Name}: ${milk.Price:F2}");
```

**Step 3:** Run and see how constructors make object creation easier!

**Real-world connection:** Inventory systems use constructors to ensure products always have a name and price when created.

### Mini Program 3: Class with Methods

Create a Customer class with a method that displays customer information.

**Step 1:** Create project
```bash
dotnet new console -o ClassWithMethod
cd ClassWithMethod
```

**Step 2:** Write the program:
```csharp
class Customer
{
    public string Name { get; set; }
    public string Email { get; set; }
    public bool IsVip { get; set; }
    
    // Method that displays customer info
    public void DisplayInfo()
    {
        string vipStatus = IsVip ? "VIP" : "Regular";
        Console.WriteLine($"Customer: {Name}");
        Console.WriteLine($"Email: {Email}");
        Console.WriteLine($"Status: {vipStatus}");
        Console.WriteLine();
    }
    
    // Method that upgrades customer to VIP
    public void UpgradeToVip()
    {
        IsVip = true;
        Console.WriteLine($"{Name} has been upgraded to VIP!");
    }
}

// Create customers
Customer customer1 = new Customer();
customer1.Name = "Sarah Johnson";
customer1.Email = "sarah@example.com";
customer1.IsVip = false;

Customer customer2 = new Customer();
customer2.Name = "Mike Chen";
customer2.Email = "mike@example.com";
customer2.IsVip = true;

// Use the methods
customer1.DisplayInfo();
customer2.DisplayInfo();

customer1.UpgradeToVip();
customer1.DisplayInfo();
```

**Step 3:** Run it and see how methods make objects more useful!

**Real-world connection:** CRM systems have methods like UpgradeToVip(), SendEmail(), UpdateProfile() - actions you can take with customer objects.

## 💻 Example Code Files

Study these example files in the `examples/` folder to see the concepts in action:

### Example 1: Simple Class (`example-01-simple-class.cs`)
Demonstrates creating a basic class with properties and creating objects from it.

**To try it:**
1. Create a new project: `dotnet new console -o SimpleClassExample`
2. Copy the code from `examples/example-01-simple-class.cs` into `Program.cs`
3. Run it: `dotnet run`

### Example 2: Constructor (`example-02-constructor.cs`)
Shows how to create a class with a constructor that initializes objects with required information.

**To try it:**
1. Create a new project: `dotnet new console -o ConstructorExample`
2. Copy the code from `examples/example-02-constructor.cs` into `Program.cs`
3. Run it to see constructors in action!

### Example 3: Class with Method (`example-03-class-with-method.cs`)
Demonstrates adding methods to classes so objects can perform actions.

**To try it:**
1. Create a new project: `dotnet new console -o MethodExample`
2. Copy the code from `examples/example-03-class-with-method.cs` into `Program.cs`
3. Run it to see how methods make objects more powerful!

**Tip:** Don't just copy-paste! Type the code yourself - it helps you learn.

## 📚 Key Concepts Summary

1. **Class** - A blueprint or template
   - Defines what something has (properties) and can do (methods)
   - Like a recipe or blueprint

2. **Object** - A specific instance created from a class
   - A real thing you can use
   - Created with `new ClassName()`

3. **Properties** - Characteristics of objects
   - `public string Name { get; set; }`
   - Store data about the object

4. **Constructors** - Special methods that create objects
   - Same name as class
   - Initialize object with required information
   - `public Product(string name, double price) { ... }`

5. **Methods in Classes** - Actions objects can perform
   - Belong to the class
   - Can use the object's properties
   - `public void MarkComplete() { ... }`

6. **Creating Objects** - `ClassName objectName = new ClassName();`
   - Use `new` keyword
   - Can pass parameters to constructor if needed

## 🎓 Exercises

Now it's time to practice! Try these exercises to build your confidence. Each exercise has its own file in the `exercises/` folder with detailed instructions.

### Exercise 1: Create a TaskItem Class
Create a `TaskItem` class with `Title` and `IsCompleted` properties. Create multiple TaskItem objects and display them.

**See:** `exercises/exercise-01.md` for full instructions.

### Exercise 2: Create a Product Class with Constructor
Build a `Product` class with `Price` and `Description` properties, and a constructor that requires these values.

**See:** `exercises/exercise-02.md` for full instructions.

### Exercise 3: Create a Customer Class with Method
Create a `Customer` class with a method that prints a formatted customer profile.

**See:** `exercises/exercise-03.md` for full instructions.

**Try each exercise yourself first!** Then check the solutions in the `exercises/` folder.

## 🧪 Quiz: Test Your Understanding

Answer these questions to check what you've learned. Answers are in `exercises/quiz-answers.md`.

### Question 1: What is the difference between a class and an object?
A) A class is a variable, an object is a method  
B) A class is a blueprint, an object is an instance created from that blueprint  
C) They are the same thing  
D) A class stores data, an object performs actions

### Question 2: What is a constructor?
A) A method that returns a value  
B) A special method that creates and initializes an object  
C) A property of a class  
D) A way to delete an object

### Question 3: What is a property?
A) An action an object can perform  
B) A characteristic that describes an object  
C) A method that creates objects  
D) A type of loop

### Question 4: What does `new` do when creating an object?
A) Deletes the object  
B) Creates a new instance of a class  
C) Updates an existing object  
D) Calls a method

### Question 5: Why do we use classes instead of just variables?
A) Classes are faster  
B) Classes organize related data and behavior together, making code easier to understand and maintain  
C) Classes use less memory  
D) Classes are required in C#

## 🐛 Debug Challenge

Find the errors in this code! See `exercises/debug-challenge.md` for the full challenge.

```csharp
class Book
{
    public string Title
    public double Price
    
    public Book(title, price)
    {
        Title = title;
        Price = price;
    }
    
    public void DisplayInfo()
    {
        Console.WriteLine("Title: " + Title "Price: $" + Price);
    }
}

Book myBook = Book("C# Guide", 29.99);
myBook.DisplayInfo();
```

**How many errors can you find?** Check `exercises/debug-challenge-solution.md` when you're done.

## ✅ Module 6 Checklist

Before moving to Module 7, make sure you can:
- [ ] Understand what classes and objects are
- [ ] Create a class with properties
- [ ] Create a constructor
- [ ] Create objects from classes using `new`
- [ ] Add methods to classes
- [ ] Use objects and their properties/methods
- [ ] Build a program using multiple objects
- [ ] Complete at least 3 exercises
- [ ] Answer the quiz questions correctly

## 🚀 What's Next?

In Module 7, you'll combine **everything** you've learned to build a complete **Task Tracker** application!

This will be your **portfolio project** that demonstrates:
- Variables and data types
- Control flow (if/else, loops)
- Methods
- Collections (Lists)
- Object-Oriented Programming (Classes)

You'll build a real, working application that you can:
- Use in your daily work
- Show to potential employers
- Mention in job interviews
- Add to your portfolio

**Real-world connection:** This is exactly how professional developers build applications - combining all these concepts into a complete, useful program. You're ready to build something real! 🎉

---

## 🔗 Navigation

- **[Previous: Module 5 - Collections →](../module-05-collections/README.md)**
- **[Next: Module 7 - Task Tracker Project →](../module-07-task-tracker/README.md)**
- **[Back to C# Workbook →](../README.md)**
- **[Back to Course Home →](../../README.md)**
- **[Course Links →](../../COURSE-LINKS.md)**
- **[Examples →](examples/)** | **[Exercises →](exercises/)**

**Remember:** OOP is how professional software is organized. Every concept you learn here is used in real applications. Keep practicing, and don't be afraid to experiment! 💪
