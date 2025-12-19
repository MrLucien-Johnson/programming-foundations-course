# Module 4: Methods

## 🎯 What You'll Learn

By the end of this module, you will be able to:
- Create reusable methods (functions) that save time and reduce mistakes
- Pass information to methods using parameters
- Get results back from methods using return values
- Understand the difference between `void` methods and methods that return values
- Organize your code into logical, reusable sections
- Understand method scope (where variables can be used)
- **Build something real:** A calculator with reusable operations, a validation helper library, and a formatted report generator

## 🌍 Real-World Connection

Methods are like reusable tools in your toolbox. Instead of writing the same code over and over:
- You write it once as a method
- You can use it anywhere in your program
- It saves time and reduces mistakes
- It makes your code easier to understand and fix

**Real-world analogy:** Think of methods like Standard Operating Procedures (SOPs) at work. Instead of figuring out how to do something every time, you have a written procedure you can follow. Methods are like that - written procedures your program can follow.

In real work, methods help you:
- Avoid repeating code (DRY principle - Don't Repeat Yourself)
- Organize complex programs into manageable pieces
- Test individual pieces separately
- Work with teams (others can use your methods)
- Fix bugs in one place instead of many

## 💪 Welcome & Motivation

Congratulations on completing Module 3! You've learned to make decisions and repeat tasks. Now we're going to make your code **organized** and **reusable**.

Think of methods like this:
- **Without methods:** Like writing the same instructions on every page of a manual
- **With methods:** Write the instructions once, then reference them whenever needed

This is where your code starts to look professional. Instead of copying and pasting the same code everywhere, you'll write it once and reuse it. This makes your programs:
- Shorter and easier to read
- Easier to fix (change it once, fixes everywhere)
- Less error-prone (test it once, works everywhere)

**Real-world impact:** Methods are used in:
- Business applications (calculate prices, validate data)
- Web applications (process forms, generate reports)
- Mobile apps (format data, check permissions)
- Every professional software project

## 📖 Part 1: What Are Methods?

### What is a Method?

A method is a **named block of code** that does a specific task. Think of it like a recipe:
- You write the recipe once (the method)
- You can follow it whenever you need that dish (call the method)
- You can use the same recipe with different ingredients (parameters)

**Real-world analogy:** Like a standard procedure at work:
- "How to process a refund" - written once, used many times
- "How to calculate tax" - written once, used for every order
- "How to format a report header" - written once, used on every report

### Why Use Methods?

**Problem without methods:**
```csharp
// Calculate tax for order 1
double order1Total = 100.00;
double order1Tax = order1Total * 0.20;
double order1Final = order1Total + order1Tax;

// Calculate tax for order 2 (copy-paste, easy to make mistakes!)
double order2Total = 150.00;
double order2Tax = order2Total * 0.20;  // What if we change tax rate? Have to change everywhere!
double order2Final = order2Total + order2Tax;

// Calculate tax for order 3 (more copy-paste...)
double order3Total = 75.00;
double order3Tax = order3Total * 0.20;
double order3Final = order3Total + order3Tax;
```

**Solution with methods:**
```csharp
// Write the calculation once
static double CalculateTax(double amount)
{
    return amount * 0.20;
}

// Use it everywhere
double order1Final = 100.00 + CalculateTax(100.00);
double order2Final = 150.00 + CalculateTax(150.00);
double order3Final = 75.00 + CalculateTax(75.00);
```

**Benefits:**
- Write once, use many times
- Change tax rate in one place, updates everywhere
- Less code, fewer mistakes
- Easier to test and fix

## 📖 Part 2: Creating Your First Method

### Simple Method (No Parameters, No Return)

Let's start with the simplest type of method - one that just does something.

```csharp
static void DisplayWelcome()
{
    Console.WriteLine("=== Welcome to Our System ===");
    Console.WriteLine("Please follow the instructions below.");
    Console.WriteLine("==============================");
}
```

**Breaking it down:**
- `static` - Don't worry about this for now, just include it
- `void` - This method doesn't return anything (it just does something)
- `DisplayWelcome` - The name of the method (you choose this)
- `()` - No parameters (nothing needed to run it)
- `{ }` - The code that runs when you call this method

**Calling the method:**
```csharp
DisplayWelcome();  // This runs all the code inside DisplayWelcome()
```

**Real-world example:** A method that prints a report header - you call it at the start of every report.

### Method with Parameters

Parameters are like placeholders - you fill them in each time you use the method.

```csharp
static void GreetUser(string name)
{
    Console.WriteLine($"Hello, {name}! Welcome!");
}
```

**Breaking it down:**
- `string name` - A parameter (information you pass in)
- The method uses `name` inside its code

**Calling the method:**
```csharp
GreetUser("Sarah");   // Prints: Hello, Sarah! Welcome!
GreetUser("John");    // Prints: Hello, John! Welcome!
GreetUser("Maria");   // Prints: Hello, Maria! Welcome!
```

**Real-world example:** A method that formats a customer name - you pass different names each time.

### Method with Return Value

Some methods calculate something and give you the result back.

```csharp
static double CalculateTotal(double price, int quantity)
{
    double total = price * quantity;
    return total;  // Give back the result
}
```

**Breaking it down:**
- `double` - This method returns a decimal number
- `return total` - This sends the result back to whoever called it

**Calling the method:**
```csharp
double result = CalculateTotal(29.99, 3);
Console.WriteLine($"Total: ${result}");  // Prints: Total: $89.97
```

**Real-world example:** A method that calculates order total - you pass price and quantity, it gives you back the total.

### Method with Parameters and Return Value

Combine both - take information in, give a result back.

```csharp
static double AddTax(double amount, double taxRate)
{
    double tax = amount * taxRate;
    double total = amount + tax;
    return total;
}
```

**Calling the method:**
```csharp
double finalPrice = AddTax(100.00, 0.20);  // 20% tax
Console.WriteLine($"Final price: ${finalPrice}");  // Prints: Final price: $120.00
```

**Real-world example:** A method that adds tax to a price - you pass the amount and tax rate, it gives you back the final price.

## 📖 Part 3: Understanding Method Parts

### Method Declaration

Every method has these parts:

```csharp
static [return type] [method name]([parameters])
{
    // Code here
}
```

**Example breakdown:**
```csharp
static double CalculateDiscount(double price, double discountPercent)
│      │      │                    │              │
│      │      │                    │              └─ Parameter 2
│      │      │                    └─ Parameter 1
│      │      └─ Method name
│      └─ Return type (what it gives back)
└─ static keyword (include this)
```

### Return Types

**`void`** - Method doesn't return anything (just does something)
```csharp
static void PrintHeader()
{
    Console.WriteLine("=== Report ===");
}
```

**Specific type** - Method returns that type of value
```csharp
static int GetAge()           // Returns an integer
static double GetPrice()      // Returns a decimal number
static string GetName()       // Returns text
static bool IsValid()         // Returns true or false
```

### Parameters

Parameters are like variables that get their values when you call the method.

```csharp
static void DisplayInfo(string name, int age, double salary)
{
    Console.WriteLine($"Name: {name}");
    Console.WriteLine($"Age: {age}");
    Console.WriteLine($"Salary: ${salary}");
}
```

**Calling with parameters:**
```csharp
DisplayInfo("Sarah", 32, 50000.00);
// name gets "Sarah"
// age gets 32
// salary gets 50000.00
```

### The `return` Statement

Use `return` to send a value back from a method.

```csharp
static int Add(int a, int b)
{
    int sum = a + b;
    return sum;  // Send sum back to caller
}
```

**Important:** Methods that don't return `void` must have a `return` statement.

## 📖 Part 4: Method Scope

### What is Scope?

Scope means "where can I use this variable?"

**Variables inside methods are local:**
```csharp
static void Method1()
{
    int x = 10;  // x only exists inside Method1
    Console.WriteLine(x);  // ✅ This works
}

static void Method2()
{
    Console.WriteLine(x);  // ❌ Error! x doesn't exist here
}
```

**Parameters are local to the method:**
```csharp
static void Greet(string name)  // name is a parameter
{
    Console.WriteLine($"Hello, {name}");  // ✅ Can use name here
}

// Outside the method:
Console.WriteLine(name);  // ❌ Error! name doesn't exist here
```

**Real-world analogy:** Like a private office - things inside the office stay in the office. Each method has its own "office" where its variables live.

### Why Scope Matters

Scope prevents mistakes:
- Variables with the same name in different methods don't conflict
- You can't accidentally use a variable from the wrong place
- Makes code easier to understand

## 🎓 Step-by-Step Mini Programs

### Mini Program 1: Simple Method

Let's create a method that displays a welcome message.

**Step 1:** Create a new project
```bash
dotnet new console -o SimpleMethod
cd SimpleMethod
```

**Step 2:** Write the program in `Program.cs`:
```csharp
static void DisplayWelcome()
{
    Console.WriteLine("=== Welcome to Our System ===");
    Console.WriteLine("Please follow the instructions.");
    Console.WriteLine("==============================");
}

DisplayWelcome();
Console.WriteLine("\nThis is the main program.");
DisplayWelcome();
```

**Step 3:** Run it
```bash
dotnet run
```

**What happens:** The `DisplayWelcome()` method runs twice - once at the start, once in the middle. Notice how we wrote it once but used it twice!

**Real-world connection:** This is how report headers work - write the header method once, call it at the start of every report.

### Mini Program 2: Method with Parameters

Build a method that calculates total price including tax.

**Step 1:** Create project
```bash
dotnet new console -o MethodWithParams
cd MethodWithParams
```

**Step 2:** Write the program:
```csharp
static double CalculateTotalWithTax(double price, double taxRate)
{
    double tax = price * taxRate;
    double total = price + tax;
    return total;
}

Console.Write("Enter price: $");
double price = double.Parse(Console.ReadLine());

Console.Write("Enter tax rate (e.g., 0.20 for 20%): ");
double taxRate = double.Parse(Console.ReadLine());

double finalPrice = CalculateTotalWithTax(price, taxRate);

Console.WriteLine($"Price: ${price:F2}");
Console.WriteLine($"Tax Rate: {taxRate:P0}");
Console.WriteLine($"Final Price: ${finalPrice:F2}");
```

**Step 3:** Run and test with different prices and tax rates!

**Real-world connection:** E-commerce sites use methods like this for every order calculation.

### Mini Program 3: Method with Return Value

Create a method that validates if a number is within a valid range.

**Step 1:** Create project
```bash
dotnet new console -o MethodWithReturn
cd MethodWithReturn
```

**Step 2:** Write the program:
```csharp
static bool IsValidAge(int age)
{
    if (age >= 0 && age <= 120)
    {
        return true;
    }
    else
    {
        return false;
    }
}

Console.Write("Enter your age: ");
int age = int.Parse(Console.ReadLine());

if (IsValidAge(age))
{
    Console.WriteLine("Valid age entered!");
}
else
{
    Console.WriteLine("Invalid age! Age must be between 0 and 120.");
}
```

**Step 3:** Run it and test with different ages!

**Real-world connection:** Form validation uses methods like this to check if input is valid before processing.

## 💻 Example Code Files

Study these example files in the `examples/` folder to see the concepts in action:

### Example 1: Simple Method (`example-01-simple-method.cs`)
Demonstrates a basic method with no parameters that displays a formatted header.

**To try it:**
1. Create a new project: `dotnet new console -o SimpleMethodExample`
2. Copy the code from `examples/example-01-simple-method.cs` into `Program.cs`
3. Run it: `dotnet run`

### Example 2: Method with Parameters (`example-02-method-with-parameters.cs`)
Shows how to pass information to a method and use it in calculations.

**To try it:**
1. Create a new project: `dotnet new console -o ParametersExample`
2. Copy the code from `examples/example-02-method-with-parameters.cs` into `Program.cs`
3. Run it and enter different values!

### Example 3: Method with Return Value (`example-03-method-with-return-value.cs`)
Demonstrates methods that calculate and return results.

**To try it:**
1. Create a new project: `dotnet new console -o ReturnValueExample`
2. Copy the code from `examples/example-03-method-with-return-value.cs` into `Program.cs`
3. Run it to see how methods return values!

**Tip:** Don't just copy-paste! Type the code yourself - it helps you learn.

## 📚 Key Concepts Summary

1. **Methods** - Named blocks of reusable code
   - Write once, use many times
   - Reduce mistakes and code duplication

2. **Method Declaration** - `static [return type] [name]([parameters])`
   - `static` - Include this keyword
   - Return type - `void` (nothing) or a type (`int`, `double`, `string`, etc.)
   - Name - What you call the method
   - Parameters - Information you pass in (optional)

3. **Calling Methods** - `MethodName()` or `MethodName(parameters)`
   - Use the method name followed by parentheses
   - Pass parameters inside the parentheses if needed

4. **Parameters** - Information passed to methods
   - Like placeholders you fill in each time
   - Can have multiple parameters separated by commas

5. **Return Values** - Results methods give back
   - Use `return` to send a value back
   - Methods with return types must return that type

6. **Scope** - Where variables can be used
   - Variables inside methods are local to that method
   - Parameters are local to the method

## 🎓 Exercises

Now it's time to practice! Try these exercises to build your confidence. Each exercise has its own file in the `exercises/` folder with detailed instructions.

### Exercise 1: Print Header Method
Create a method that prints a standard header for a report. The method should display a formatted header with a title.

**See:** `exercises/exercise-01.md` for full instructions.

### Exercise 2: Discount Calculation Method
Create a method that calculates and returns a discounted price. The method should take the original price and discount percentage as parameters.

**See:** `exercises/exercise-02.md` for full instructions.

### Exercise 3: Password Validation Method
Create a method that checks whether an entered password meets simple length rules. The method should return true or false.

**See:** `exercises/exercise-03.md` for full instructions.

**Try each exercise yourself first!** Then check the solutions in the `exercises/` folder.

## 🧪 Quiz: Test Your Understanding

Answer these questions to check what you've learned. Answers are in `exercises/quiz-answers.md`.

### Question 1: What is a method?
A) A variable that stores code  
B) A named block of reusable code  
C) A type of loop  
D) A way to get user input

### Question 2: What does `void` mean in a method declaration?
A) The method returns nothing  
B) The method returns a number  
C) The method has no parameters  
D) The method is empty

### Question 3: What is a parameter?
A) The value a method returns  
B) Information you pass to a method  
C) The name of a method  
D) A type of variable

### Question 4: What does `return` do?
A) Starts a method  
B) Stops a method  
C) Sends a value back from a method  
D) Calls a method

### Question 5: Why should you use methods instead of repeating code?
A) Methods are faster  
B) Methods reduce mistakes and make code easier to maintain  
C) Methods use less memory  
D) Methods are required in C#

## 🐛 Debug Challenge

Find the errors in this code! See `exercises/debug-challenge.md` for the full challenge.

```csharp
void CalculateTotal(price, quantity)
{
    double total = price * quantity;
    return total;
}

double result = CalculateTotal(10.50, 3);
Console.WriteLine("Total: " + result);
```

**How many errors can you find?** Check `exercises/debug-challenge-solution.md` when you're done.

## ✅ Module 4 Checklist

Before moving to Module 5, make sure you can:
- [ ] Create methods with no parameters (`void` methods)
- [ ] Create methods with parameters
- [ ] Create methods that return values
- [ ] Call methods from your main program
- [ ] Understand that variables inside methods are local
- [ ] Understand that parameters are local to the method
- [ ] Build a program using multiple methods
- [ ] Complete at least 3 exercises
- [ ] Answer the quiz questions correctly

## 🚀 What's Next?

In Module 5, you'll learn about **Collections** - ways to store and work with groups of data.

Collections let you:
- Store multiple items together (like a list of customers)
- Process groups of data efficiently
- Work with arrays and lists
- Loop through collections easily

**Real-world connection:** Almost every application uses collections - customer lists, product catalogs, order histories, task lists. You'll learn to manage and process these groups of data efficiently.

---

**Remember:** Methods are one of the most important concepts in programming. They help you write professional, maintainable code. Keep practicing, and don't be afraid to experiment! 💪

---

## 🔗 Navigation

- **[Previous: Module 3 - Control Flow →](../module-03-control-flow/README.md)**
- **[Next: Module 5 - Collections →](../module-05-collections/README.md)**
- **[Back to C# Workbook →](../README.md)**
- **[Back to Course Home →](../../README.md)**
- **[Course Links →](../../COURSE-LINKS.md)**
- **[Examples →](examples/)** | **[Exercises →](exercises/)**