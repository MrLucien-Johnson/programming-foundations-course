# Module 3: Control Flow

## 🎯 What You'll Learn

By the end of this module, you will be able to:
- Make decisions in your programs using `if`, `else if`, and `else` statements
- Use comparison operators (`>`, `<`, `>=`, `<=`, `==`, `!=`) to check conditions
- Understand boolean expressions (true/false conditions)
- Use logical operators (`&&`, `||`) to combine conditions
- Repeat tasks using `for` loops
- Repeat tasks using `while` loops
- Process collections using `foreach` loops
- Validate user input and handle errors
- **Build something real:** A discount calculator, an age verification system, a task processor, and a simple menu system

## 🌍 Real-World Connection

Control flow is how programs make decisions and repeat tasks - just like you do at work:
- "If the customer is a VIP, apply a discount"
- "Process each item in the order"
- "Keep asking until we get valid input"
- "Check all tasks and mark completed ones"

These patterns appear in almost every real-world program. By mastering them, you're learning skills used in customer service systems, inventory management, and data processing tools.

## 💪 Welcome & Motivation

Congratulations on completing Module 2! You've learned to store information and do calculations. Now we're going to make your programs **smart** - they'll make decisions and repeat tasks automatically.

Think of control flow like this:
- **Decisions** - Like a security guard checking IDs: "If you're 18 or older, you can enter"
- **Loops** - Like processing a stack of papers: "For each paper, check it and file it"

This is where programming starts to feel powerful. Instead of writing the same code over and over, you'll write it once and let the computer repeat it. Instead of manually checking every condition, your program will decide what to do automatically.

**Real-world impact:** These skills are used in:
- E-commerce sites (apply discounts, check stock)
- Banking systems (verify balances, process transactions)
- Customer service tools (route requests, check status)
- Inventory systems (process orders, check quantities)

## 📖 Part 1: Making Decisions (if/else)

### What is a Decision?

A decision is like a fork in the road. Your program checks a condition and chooses which path to take.

**Real-world analogy:** Like a bouncer at a club - "If you're 18 or older, you can come in. Otherwise, sorry, you can't."

### Simple If Statement

The simplest decision: "If something is true, do this."

```csharp
int age = 20;

if (age >= 18)
{
    Console.WriteLine("You are an adult.");
}
```

**What happens:**
- Program checks: Is `age >= 18`? (Is age greater than or equal to 18?)
- If YES (true): Print "You are an adult."
- If NO (false): Do nothing, skip to next line

**Real-world example:** Age verification for website access.

### If/Else Statement

"If something is true, do this. Otherwise, do that."

```csharp
int age = 15;

if (age >= 18)
{
    Console.WriteLine("Access granted.");
}
else
{
    Console.WriteLine("Access denied. You must be 18 or older.");
}
```

**What happens:**
- If age is 18 or more: Print "Access granted."
- Otherwise: Print "Access denied."

**Real-world example:** Login systems, age-restricted content, permission checks.

### If/Else If/Else Statement

"Check multiple conditions, one at a time."

```csharp
double purchaseTotal = 150.00;

if (purchaseTotal > 1000)
{
    Console.WriteLine("You get 30% discount!");
}
else if (purchaseTotal > 500)
{
    Console.WriteLine("You get 20% discount!");
}
else if (purchaseTotal > 100)
{
    Console.WriteLine("You get 10% discount!");
}
else
{
    Console.WriteLine("No discount available.");
}
```

**What happens:**
- Check first condition: Is total > 1000? If yes, apply 30% discount.
- If no, check second: Is total > 500? If yes, apply 20% discount.
- If no, check third: Is total > 100? If yes, apply 10% discount.
- If none match: No discount.

**Real-world example:** Tiered discount systems in e-commerce.

### Comparison Operators

These let you compare values:

```csharp
int age = 25;

age > 18   // true (greater than)
age < 18   // false (less than)
age >= 18  // true (greater than or equal to)
age <= 18  // false (less than or equal to)
age == 18  // false (equal to)
age != 18  // true (not equal to)
```

**Common mistakes:**
- `=` is for assigning values: `age = 25` (put 25 into age)
- `==` is for comparing: `age == 25` (is age equal to 25?)

**Real-world example:** Checking if customer qualifies for VIP status, if order meets free shipping threshold.

### Boolean Expressions

A boolean expression is something that's either `true` or `false`.

```csharp
bool isVip = true;
bool isComplete = false;

if (isVip)
{
    Console.WriteLine("Welcome, VIP customer!");
}
```

**Real-world example:** Checking if a task is complete, if a user is logged in, if an item is in stock.

### Logical Operators

Combine multiple conditions:

**`&&` (AND)** - Both conditions must be true
```csharp
int age = 25;
bool hasLicense = true;

if (age >= 18 && hasLicense)
{
    Console.WriteLine("You can drive!");
}
```

**`||` (OR)** - At least one condition must be true
```csharp
bool isVip = true;
double purchaseTotal = 150.00;

if (isVip || purchaseTotal > 100)
{
    Console.WriteLine("You get free shipping!");
}
```

**Real-world example:** "If customer is VIP OR purchase is over $100, apply free shipping."

## 📖 Part 2: Loops - Repeating Tasks

### What is a Loop?

A loop repeats code multiple times. Instead of writing the same code 100 times, you write it once and tell the computer to repeat it.

**Real-world analogy:** Like a factory assembly line - the same process repeats for each item.

### For Loops

Repeat a specific number of times.

```csharp
for (int i = 1; i <= 10; i++)
{
    Console.WriteLine($"Count: {i}");
}
```

**Breaking it down:**
- `int i = 1` - Start with i = 1
- `i <= 10` - Keep going while i is less than or equal to 10
- `i++` - After each loop, add 1 to i
- The code inside `{ }` runs for each value of i (1, 2, 3, ... 10)

**Output:**
```
Count: 1
Count: 2
Count: 3
...
Count: 10
```

**Real-world example:** Processing a batch of 10 orders, counting down a timer, generating numbered reports.

### While Loops

Repeat while a condition is true.

```csharp
string input = "";

while (input != "quit")
{
    Console.Write("Enter command (or 'quit' to exit): ");
    input = Console.ReadLine();
    Console.WriteLine($"You entered: {input}");
}
```

**What happens:**
- Check condition: Is input NOT equal to "quit"?
- If yes: Run the code inside, then check again
- If no: Stop looping

**Real-world example:** Keep asking for password until correct, keep processing until queue is empty, retry failed operations.

### Foreach Loops

Go through each item in a collection (like a list).

```csharp
string[] tasks = { "Buy groceries", "Finish report", "Call client" };

foreach (string task in tasks)
{
    Console.WriteLine($"Task: {task}");
}
```

**What happens:**
- For each item in the `tasks` array
- Put that item into the variable `task`
- Run the code inside with that task
- Move to next item

**Output:**
```
Task: Buy groceries
Task: Finish report
Task: Call client
```

**Real-world example:** Processing each order in a list, checking each item in inventory, sending emails to each customer.

**Note:** We'll learn more about collections (arrays, lists) in Module 5. For now, just know that `foreach` lets you go through each item.

## 📖 Part 3: Combining Concepts

### Nested If Statements

Put if statements inside other if statements.

```csharp
int age = 25;
bool isVip = true;

if (age >= 18)
{
    if (isVip)
    {
        Console.WriteLine("Welcome, VIP member!");
    }
    else
    {
        Console.WriteLine("Welcome!");
    }
}
else
{
    Console.WriteLine("Access denied.");
}
```

**Real-world example:** "If customer is old enough AND is VIP, give special treatment."

### Loops with Conditions

Use if statements inside loops.

```csharp
for (int i = 1; i <= 10; i++)
{
    if (i % 2 == 0)  // If i is even
    {
        Console.WriteLine($"{i} is even");
    }
    else
    {
        Console.WriteLine($"{i} is odd");
    }
}
```

**Real-world example:** Process only items that meet certain criteria, skip invalid entries.

### Input Validation

Keep asking until you get valid input.

```csharp
int age = 0;

while (age < 1 || age > 120)
{
    Console.Write("Enter your age (1-120): ");
    string ageText = Console.ReadLine();
    age = int.Parse(ageText);
    
    if (age < 1 || age > 120)
    {
        Console.WriteLine("Invalid age! Please try again.");
    }
}

Console.WriteLine($"Thank you! Your age is {age}.");
```

**Real-world example:** Form validation, ensuring data quality, preventing errors.

## 🎓 Step-by-Step Mini Programs

### Mini Program 1: Age Verification System

Let's build a program that checks if someone is old enough.

**Step 1:** Create a new project
```bash
dotnet new console -o AgeVerification
cd AgeVerification
```

**Step 2:** Write the program in `Program.cs`:
```csharp
Console.Write("Enter your age: ");
string ageText = Console.ReadLine();
int age = int.Parse(ageText);

if (age >= 18)
{
    Console.WriteLine("Access granted. Welcome!");
}
else
{
    Console.WriteLine("Access denied. You must be 18 or older.");
}
```

**Step 3:** Run it
```bash
dotnet run
```

**Try it:** Enter different ages and see what happens!

**Real-world connection:** This is how age-restricted websites and services verify users.

### Mini Program 2: Discount Calculator

Build a calculator that applies discounts based on purchase amount.

**Step 1:** Create project
```bash
dotnet new console -o DiscountCalculator
cd DiscountCalculator
```

**Step 2:** Write the program:
```csharp
Console.Write("Enter purchase total: $");
string totalText = Console.ReadLine();
double total = double.Parse(totalText);

double discount = 0;
double discountPercent = 0;

if (total > 1000)
{
    discountPercent = 30;
    discount = total * 0.30;
}
else if (total > 500)
{
    discountPercent = 20;
    discount = total * 0.20;
}
else if (total > 100)
{
    discountPercent = 10;
    discount = total * 0.10;
}

double finalTotal = total - discount;

Console.WriteLine($"Original Price: ${total:F2}");
if (discount > 0)
{
    Console.WriteLine($"Discount ({discountPercent}%): ${discount:F2}");
}
else
{
    Console.WriteLine("No discount applied.");
}
Console.WriteLine($"Final Price: ${finalTotal:F2}");
```

**Step 3:** Run and test with different purchase amounts!

**Real-world connection:** E-commerce sites use this exact pattern for tiered discounts.

### Mini Program 3: Simple Menu System

Create a menu that repeats until the user chooses to quit.

**Step 1:** Create project
```bash
dotnet new console -o SimpleMenu
cd SimpleMenu
```

**Step 2:** Write the program:
```csharp
string choice = "";

while (choice != "3")
{
    Console.WriteLine("\n=== Menu ===");
    Console.WriteLine("1. View Tasks");
    Console.WriteLine("2. Add Task");
    Console.WriteLine("3. Quit");
    Console.Write("Enter your choice: ");
    
    choice = Console.ReadLine();
    
    if (choice == "1")
    {
        Console.WriteLine("Your tasks: Buy groceries, Finish report");
    }
    else if (choice == "2")
    {
        Console.Write("Enter task name: ");
        string task = Console.ReadLine();
        Console.WriteLine($"Added: {task}");
    }
    else if (choice == "3")
    {
        Console.WriteLine("Goodbye!");
    }
    else
    {
        Console.WriteLine("Invalid choice. Please try again.");
    }
}
```

**Step 3:** Run it and try the menu options!

**Real-world connection:** Command-line tools, simple applications, and interactive programs use this pattern.

## 💻 Example Code Files

Study these example files in the `examples/` folder to see the concepts in action:

### Example 1: If/Else Decisions (`example-01-if-else.cs`)
Demonstrates making decisions with if/else statements, including discount logic and age verification.

**To try it:**
1. Create a new project: `dotnet new console -o IfElseExample`
2. Copy the code from `examples/example-01-if-else.cs` into `Program.cs`
3. Run it: `dotnet run`

### Example 2: Simple Menu Loop (`example-02-simple-menu.cs`)
Shows how to create a menu system that repeats until the user chooses to exit.

**To try it:**
1. Create a new project: `dotnet new console -o MenuExample`
2. Copy the code from `examples/example-02-simple-menu.cs` into `Program.cs`
3. Run it and try the menu options!

### Example 3: Looping Through a List (`example-03-looping-through-list.cs`)
Demonstrates using `foreach` to process each item in a collection.

**To try it:**
1. Create a new project: `dotnet new console -o LoopExample`
2. Copy the code from `examples/example-03-looping-through-list.cs` into `Program.cs`
3. Run it to see how loops process multiple items!

**Tip:** Don't just copy-paste! Type the code yourself - it helps you learn.

## 📚 Key Concepts Summary

1. **If Statements** - Make decisions based on conditions
   - `if` - Do something if condition is true
   - `else` - Do something if condition is false
   - `else if` - Check another condition

2. **Comparison Operators** - Compare values
   - `>` greater than, `<` less than
   - `>=` greater than or equal, `<=` less than or equal
   - `==` equal to, `!=` not equal to

3. **Logical Operators** - Combine conditions
   - `&&` AND - both must be true
   - `||` OR - at least one must be true

4. **For Loops** - Repeat a specific number of times
   - `for (int i = 0; i < 10; i++)`

5. **While Loops** - Repeat while condition is true
   - `while (condition)`

6. **Foreach Loops** - Go through each item in a collection
   - `foreach (item in collection)`

## 🎓 Exercises

Now it's time to practice! Try these exercises to build your confidence. Each exercise has its own file in the `exercises/` folder with detailed instructions.

### Exercise 1: Grade Classifier
Create a program that asks for a test score and classifies it as A, B, C, D, or F using if/else statements.

**See:** `exercises/exercise-01.md` for full instructions.

### Exercise 2: Login Attempt Limit
Build a program that gives users 3 attempts to enter the correct password using a while loop.

**See:** `exercises/exercise-02.md` for full instructions.

### Exercise 3: Task Reminder Loop
Create a program that uses foreach to display a list of tasks and remind the user about each one.

**See:** `exercises/exercise-03.md` for full instructions.

**Try each exercise yourself first!** Then check the solutions in the `exercises/` folder.

## 🧪 Quiz: Test Your Understanding

Answer these questions to check what you've learned. Answers are in `exercises/quiz-answers.md`.

### Question 1: What does an if statement do?
A) Repeats code multiple times  
B) Makes a decision based on a condition  
C) Stores information  
D) Gets input from the user

### Question 2: When would you use a for loop vs a while loop?
A) Use `for` when you know how many times to repeat, `while` when you don't  
B) Use `for` for decisions, `while` for loops  
C) They're the same thing  
D) Use `for` for text, `while` for numbers

### Question 3: What is the difference between `==` and `=` in C#?
A) `==` compares values, `=` assigns values  
B) `==` assigns values, `=` compares values  
C) They're the same  
D) `==` is for strings, `=` is for numbers

### Question 4: How do you make a loop repeat forever (until broken)?
A) `for (;;)`  
B) `while (true)`  
C) `foreach (item in items)`  
D) You can't do this

### Question 5: What does `break` do in a loop?
A) Starts the loop over  
B) Stops the loop immediately  
C) Skips to the next iteration  
D) Continues the loop

## 🐛 Debug Challenge

Find the errors in this code! See `exercises/debug-challenge.md` for the full challenge.

```csharp
int age = 25;
if age >= 18
{
    Console.WriteLine("Adult");
}
else
    Console.WriteLine("Minor");
}

for (int i = 0; i < 5; i++)
    Console.WriteLine(i);
}
```

**How many errors can you find?** Check `exercises/debug-challenge-solution.md` when you're done.

## ✅ Module 3 Checklist

Before moving to Module 4, make sure you can:
- [ ] Write if/else statements
- [ ] Use comparison operators (`==`, `!=`, `<`, `>`, `<=`, `>=`)
- [ ] Use logical operators (`&&`, `||`)
- [ ] Write for loops
- [ ] Write while loops
- [ ] Write foreach loops
- [ ] Validate user input using loops
- [ ] Build a working menu system
- [ ] Complete at least 3 exercises
- [ ] Answer the quiz questions correctly

## 🚀 What's Next?

In Module 4, you'll learn about **Methods** - reusable blocks of code that save time and reduce mistakes.

Methods let you:
- Write code once and use it many times
- Organize your programs better
- Make your code easier to understand and fix
- Build more complex programs step by step

**Real-world connection:** Methods are like tools in a toolbox - you create them once, then use them whenever you need that specific job done. Professional developers use methods constantly to keep code organized and reusable.

---

## 🔗 Navigation

- **[Previous: Module 2 - C# Basics →](../module-02-basics/README.md)**
- **[Next: Module 4 - Methods →](../module-04-methods/README.md)**
- **[Back to C# Workbook →](../README.md)**
- **[Back to Course Home →](../../README.md)**
- **[Course Links →](../../COURSE-LINKS.md)**
- **[Examples →](examples/)** | **[Exercises →](exercises/)**

**Remember:** You're building real skills! Every concept you learn here is used in professional software. Keep practicing, and don't be afraid to experiment! 💪
