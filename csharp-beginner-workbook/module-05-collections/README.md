# Module 5: Collections

## 🎯 What You'll Learn

By the end of this module, you will be able to:
- Store multiple items using arrays (fixed-size collections)
- Use `List<T>` to work with dynamic collections that grow and shrink
- Add, remove, and count items in collections
- Access items by their position (index)
- Loop through collections using `for` and `foreach`
- Search for items in collections
- **Build something real:** A customer management system, a task list manager, a shopping list, and a simple inventory tracker

## 🌍 Real-World Connection

Collections let you work with groups of related data - something you do constantly in real work:
- Lists of customers
- Inventories of products
- Queues of tasks
- Records of transactions
- Shopping lists
- Employee rosters

**Real-world analogy:** Think of collections like:
- **Arrays** = Shelves with a fixed number of slots (like a storage unit with numbered compartments)
- **Lists** = A flexible checklist that can grow or shrink (like a to-do list you can add to or cross off)

Almost every business application uses collections. By learning them, you're gaining skills used in:
- Customer relationship management (CRM) systems
- Inventory management
- Task tracking applications
- E-commerce shopping carts
- Data processing tools

## 💪 Welcome & Motivation

Congratulations on completing Module 4! You've learned to organize code with methods. Now we're going to learn to work with **groups of data** - something every real application needs.

Think of collections like this:
- **Without collections:** Like trying to remember 100 customer names in your head
- **With collections:** Like having a well-organized filing cabinet where you can store, find, and manage all customer information

This is where your programs start handling real-world data. Instead of working with one thing at a time, you'll work with lists of things - customers, products, tasks, orders. This makes your programs:
- More useful (handle multiple items)
- More realistic (match how real work happens)
- More powerful (process data in bulk)

**Real-world impact:** Collections are used in:
- E-commerce (product catalogs, shopping carts)
- Business systems (customer databases, order lists)
- Task management (to-do lists, project tasks)
- Inventory systems (product lists, stock tracking)

## 📖 Part 1: Understanding Arrays

### What is an Array?

An array is a **fixed-size collection** - like a row of numbered boxes. Once you create it with a certain size, that size doesn't change.

**Real-world analogy:** Like a storage unit with 10 numbered compartments. You can put one item in each compartment, but you can't add an 11th compartment.

### Creating Arrays

```csharp
string[] tasks = { "Buy groceries", "Finish report", "Call client" };
```

**Breaking it down:**
- `string[]` - This is an array of strings
- `tasks` - The name of the array
- `{ ... }` - The items in the array

### Accessing Items by Index

Each item in an array has a **position number** called an **index**. Indexes start at 0 (not 1!).

```csharp
string[] tasks = { "Buy groceries", "Finish report", "Call client" };

Console.WriteLine(tasks[0]);  // Prints "Buy groceries" (first item)
Console.WriteLine(tasks[1]);  // Prints "Finish report" (second item)
Console.WriteLine(tasks[2]);  // Prints "Call client" (third item)
```

**Important:** Indexes start at 0, not 1!
- First item = index 0
- Second item = index 1
- Third item = index 2

**Real-world example:** Like apartment numbers - the first apartment is #1, but in arrays, the first item is at position 0.

### Array Length

Find out how many items are in an array:

```csharp
string[] tasks = { "Buy groceries", "Finish report", "Call client" };
int count = tasks.Length;  // count is 3
Console.WriteLine($"You have {count} tasks.");
```

### When to Use Arrays

Use arrays when:
- You know exactly how many items you need
- The size won't change
- You want simple, fast access

**Real-world examples:**
- Days of the week (always 7)
- Months of the year (always 12)
- Fixed-size product categories

## 📖 Part 2: Understanding Lists

### What is a List?

A `List<T>` is a **dynamic collection** - it can grow and shrink. You can add items, remove items, and it automatically adjusts its size.

**Real-world analogy:** Like a flexible checklist - you can add new items, cross off completed ones, and the list adjusts automatically.

### Creating Lists

```csharp
List<string> tasks = new List<string>();
```

**Breaking it down:**
- `List<string>` - A list that holds strings
- `tasks` - The name of the list
- `new List<string>()` - Create a new empty list

### Adding Items to Lists

```csharp
List<string> tasks = new List<string>();

tasks.Add("Buy groceries");
tasks.Add("Finish report");
tasks.Add("Call client");
```

**Real-world example:** Like adding items to a shopping list - you keep adding until you're done.

### Removing Items from Lists

```csharp
tasks.Remove("Buy groceries");  // Remove by value
```

**Real-world example:** Like crossing off a completed task - it's removed from your active list.

### Counting Items in Lists

```csharp
int count = tasks.Count;  // How many items are in the list
Console.WriteLine($"You have {count} tasks.");
```

### Accessing Items by Index

Just like arrays, you can access list items by index:

```csharp
List<string> tasks = new List<string>();
tasks.Add("Buy groceries");
tasks.Add("Finish report");

Console.WriteLine(tasks[0]);  // Prints "Buy groceries"
Console.WriteLine(tasks[1]);  // Prints "Finish report"
```

### When to Use Lists

Use lists when:
- Number of items can change
- You need to add/remove items
- You want flexibility

**Real-world examples:**
- Shopping carts (items added/removed)
- Task lists (tasks added/completed)
- Customer databases (customers added over time)
- Order lists (orders come in continuously)

## 📖 Part 3: Looping Through Collections

### Using For Loops

Loop through a collection by index:

```csharp
string[] tasks = { "Buy groceries", "Finish report", "Call client" };

for (int i = 0; i < tasks.Length; i++)
{
    Console.WriteLine($"{i + 1}. {tasks[i]}");
}
```

**Output:**
```
1. Buy groceries
2. Finish report
3. Call client
```

**Important:** Use `<` not `<=` because indexes start at 0. If array has 3 items, indexes are 0, 1, 2 (not 0, 1, 2, 3).

### Using Foreach Loops

Loop through each item directly (easier!):

```csharp
List<string> tasks = new List<string>();
tasks.Add("Buy groceries");
tasks.Add("Finish report");
tasks.Add("Call client");

foreach (string task in tasks)
{
    Console.WriteLine($"Task: {task}");
}
```

**Output:**
```
Task: Buy groceries
Task: Finish report
Task: Call client
```

**Why foreach is easier:**
- No need to track index
- No risk of going out of bounds
- Cleaner, simpler code

**Real-world example:** Like going through a filing cabinet - you look at each file one by one, in order.

## 📖 Part 4: Common Operations

### Checking if an Item Exists

```csharp
List<string> tasks = new List<string>();
tasks.Add("Buy groceries");

if (tasks.Contains("Buy groceries"))
{
    Console.WriteLine("Task found!");
}
```

**Real-world example:** Checking if a customer is already in your database before adding them.

### Finding an Item's Index

```csharp
int index = tasks.IndexOf("Finish report");
if (index >= 0)
{
    Console.WriteLine($"Found at position {index}");
}
```

### Clearing All Items

```csharp
tasks.Clear();  // Remove all items
```

## 🎓 Step-by-Step Mini Programs

### Mini Program 1: Basic Array

Let's create a program that stores and displays a list of tasks using an array.

**Step 1:** Create a new project
```bash
dotnet new console -o BasicArray
cd BasicArray
```

**Step 2:** Write the program in `Program.cs`:
```csharp
string[] tasks = { "Buy groceries", "Finish report", "Call client", "Review proposal", "Send email" };

Console.WriteLine("=== Your Tasks ===");
for (int i = 0; i < tasks.Length; i++)
{
    Console.WriteLine($"{i + 1}. {tasks[i]}");
}

Console.WriteLine($"\nTotal tasks: {tasks.Length}");
```

**Step 3:** Run it
```bash
dotnet run
```

**What happens:** The program displays all tasks with numbers, then shows the total count.

**Real-world connection:** This is how task lists are displayed in many applications.

### Mini Program 2: List Basics

Build a program that lets you add and remove items from a list.

**Step 1:** Create project
```bash
dotnet new console -o ListBasics
cd ListBasics
```

**Step 2:** Write the program:
```csharp
List<string> shoppingList = new List<string>();

// Add items
shoppingList.Add("Milk");
shoppingList.Add("Bread");
shoppingList.Add("Eggs");
shoppingList.Add("Butter");

Console.WriteLine("=== Shopping List ===");
foreach (string item in shoppingList)
{
    Console.WriteLine($"- {item}");
}
Console.WriteLine($"Total items: {shoppingList.Count}");

// Remove an item
shoppingList.Remove("Bread");

Console.WriteLine("\n=== After Removing Bread ===");
foreach (string item in shoppingList)
{
    Console.WriteLine($"- {item}");
}
Console.WriteLine($"Total items: {shoppingList.Count}");
```

**Step 3:** Run and see how the list changes!

**Real-world connection:** This is exactly how shopping cart systems work - items added and removed dynamically.

### Mini Program 3: Customer List Manager

Create a simple customer list that you can add to and display.

**Step 1:** Create project
```bash
dotnet new console -o CustomerList
cd CustomerList
```

**Step 2:** Write the program:
```csharp
List<string> customers = new List<string>();

// Add some customers
customers.Add("Sarah Johnson");
customers.Add("Mike Chen");
customers.Add("Emma Davis");

Console.WriteLine("=== Customer List ===");
int customerNumber = 1;
foreach (string customer in customers)
{
    Console.WriteLine($"{customerNumber}. {customer}");
    customerNumber++;
}

Console.WriteLine($"\nTotal customers: {customers.Count}");
```

**Step 3:** Run it and see your customer list!

**Real-world connection:** CRM systems use lists like this to manage customer databases.

## 💻 Example Code Files

Study these example files in the `examples/` folder to see the concepts in action:

### Example 1: Basic Array (`example-01-basic-array.cs`)
Demonstrates creating an array, accessing items by index, and looping through with a for loop.

**To try it:**
1. Create a new project: `dotnet new console -o ArrayExample`
2. Copy the code from `examples/example-01-basic-array.cs` into `Program.cs`
3. Run it: `dotnet run`

### Example 2: List Basics (`example-02-list-basics.cs`)
Shows how to create a list, add items, remove items, and count items.

**To try it:**
1. Create a new project: `dotnet new console -o ListExample`
2. Copy the code from `examples/example-02-list-basics.cs` into `Program.cs`
3. Run it to see lists in action!

### Example 3: Foreach Loop (`example-03-foreach-loop.cs`)
Demonstrates using foreach to loop through collections and process each item.

**To try it:**
1. Create a new project: `dotnet new console -o ForeachExample`
2. Copy the code from `examples/example-03-foreach-loop.cs` into `Program.cs`
3. Run it to see how foreach makes looping easier!

**Tip:** Don't just copy-paste! Type the code yourself - it helps you learn.

## 📚 Key Concepts Summary

1. **Arrays** - Fixed-size collections
   - Created with `string[] items = { "item1", "item2" }`
   - Access with index: `items[0]`
   - Get length: `items.Length`
   - Use when size is fixed

2. **Lists** - Dynamic collections that grow/shrink
   - Created with `List<string> items = new List<string>()`
   - Add items: `items.Add("new item")`
   - Remove items: `items.Remove("item")`
   - Get count: `items.Count`
   - Use when size can change

3. **Indexes** - Position numbers (start at 0!)
   - First item = index 0
   - Second item = index 1
   - Last item = index (length - 1)

4. **For Loops** - Loop by index
   - `for (int i = 0; i < items.Length; i++)`
   - Access items with `items[i]`
   - Use `<` not `<=` to avoid out-of-range errors

5. **Foreach Loops** - Loop through each item
   - `foreach (string item in items)`
   - Easier and safer than for loops
   - No index to track

6. **Common Operations**
   - `Contains()` - Check if item exists
   - `IndexOf()` - Find item's position
   - `Clear()` - Remove all items

## 🎓 Exercises

Now it's time to practice! Try these exercises to build your confidence. Each exercise has its own file in the `exercises/` folder with detailed instructions.

### Exercise 1: Shopping List
Create a program that manages a shopping list using `List<string>`. Add items, display the list, and show the count.

**See:** `exercises/exercise-01.md` for full instructions.

### Exercise 2: Customer List with Count
Build a program that stores customer names in a list, displays them, and shows the total count.

**See:** `exercises/exercise-02.md` for full instructions.

### Exercise 3: Task Printer
Create a program that uses a `foreach` loop to display a list of tasks in a formatted way.

**See:** `exercises/exercise-03.md` for full instructions.

**Try each exercise yourself first!** Then check the solutions in the `exercises/` folder.

## 🧪 Quiz: Test Your Understanding

Answer these questions to check what you've learned. Answers are in `exercises/quiz-answers.md`.

### Question 1: What is the difference between an array and a List?
A) Arrays are faster, Lists are slower  
B) Arrays have fixed size, Lists can grow and shrink  
C) Arrays hold numbers, Lists hold text  
D) There is no difference

### Question 2: How do you add an item to a List?
A) `list.AddItem("item")`  
B) `list.Add("item")`  
C) `list.Insert("item")`  
D) `list.Push("item")`

### Question 3: What does `foreach` do?
A) Counts items in a collection  
B) Loops through each item in a collection  
C) Adds items to a collection  
D) Removes items from a collection

### Question 4: How do you find the number of items in a collection?
A) `collection.Size()`  
B) `collection.Length` for arrays, `collection.Count` for lists  
C) `collection.Count()`  
D) `collection.Items()`

### Question 5: What is an index in a collection?
A) The value of an item  
B) The position number of an item (starts at 0)  
C) The name of the collection  
D) The type of items in the collection

## 🐛 Debug Challenge

Find the errors in this code! See `exercises/debug-challenge.md` for the full challenge.

```csharp
List<string> names = new List<string>();
names.Add("Alice");
names.Add("Bob");
names.Add("Charlie");

for (int i = 0; i <= names.Count; i++)
{
    Console.WriteLine(names[i]);
}
```

**How many errors can you find?** Check `exercises/debug-challenge-solution.md` when you're done.

## ✅ Module 5 Checklist

Before moving to Module 6, make sure you can:
- [ ] Create and use arrays
- [ ] Create and use Lists
- [ ] Add items to collections
- [ ] Remove items from collections
- [ ] Access items by index (remember indexes start at 0!)
- [ ] Loop through collections with `for` loops
- [ ] Loop through collections with `foreach` loops
- [ ] Count items in collections
- [ ] Check if an item exists in a collection
- [ ] Build a working list management system
- [ ] Complete at least 3 exercises
- [ ] Answer the quiz questions correctly

## 🚀 What's Next?

In Module 6, you'll learn about **Object-Oriented Programming** - organizing code using classes and objects.

OOP lets you:
- Model real-world things as code (like a `Task` class or `Customer` class)
- Combine data and behavior together
- Create reusable, organized code structures
- Build more complex applications

**Real-world connection:** Professional software uses classes and objects everywhere. You'll learn to create your own classes (like `Task`, `Product`, `Order`) that combine collections with methods to create powerful, organized programs.

---

**Remember:** Collections are fundamental to programming. Almost every application uses them. Keep practicing, and don't be afraid to experiment! 💪

---

## 🔗 Navigation

- **[Previous: Module 4 - Methods →](../module-04-methods/README.md)**
- **[Next: Module 6 - Intro to OOP →](../module-06-oop-intro/README.md)**
- **[Back to C# Workbook →](../README.md)**
- **[Back to Course Home →](../../README.md)**
- **[Course Links →](../../COURSE-LINKS.md)**
- **[Examples →](examples/)** | **[Exercises →](exercises/)**