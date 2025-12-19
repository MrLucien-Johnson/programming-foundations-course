# Module 2: C# Basics

## 🎯 What You'll Learn

By the end of this module, you will be able to:
- Store information using variables (like labeled boxes)
- Understand different data types (numbers, text, true/false)
- Get input from users and use it in your programs
- Perform calculations with numbers
- Format strings beautifully using string interpolation
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
- Ask users for information (input)
- Do calculations (math)
- Display results nicely (formatting)

Think of it like learning to have a conversation with your program - you ask questions, get answers, do some work, and show results. This is how real applications work!

## 📖 Part 1: Understanding Variables

### What is a Variable?

Think of a variable like a **labeled box**. You can:
- Put something in it (store a value)
- Look at what's inside (read the value)
- Change what's inside (update the value)
- Give it a name so you remember what it's for

**Real-world analogy:** Like a filing cabinet drawer labeled "Customer Names" - you can put names in, take them out, and change them.

### Creating Variables in C#

To create a variable, you need:
1. **Type** - What kind of information it holds
2. **Name** - What you call it
3. **Value** - What you put in it (optional at first)

```csharp
string customerName = "Sarah";
```

Let's break this down:
- `string` - The type (this box holds text)
- `customerName` - The name (the label on the box)
- `"Sarah"` - The value (what's inside the box)
- `=` - Means "put this value into the variable"
- `;` - End of the statement

### Basic Data Types

C# has different types of "boxes" for different kinds of information:

#### 1. `int` - Whole Numbers
```csharp
int age = 25;
int quantity = 100;
int temperature = -5;
```
- Use for: ages, counts, quantities, IDs
- **Real-world:** Customer age, order quantity, employee ID

#### 2. `double` - Decimal Numbers
```csharp
double price = 29.99;
double weight = 1.5;
double temperature = 98.6;
```
- Use for: prices, measurements, percentages
- **Real-world:** Product prices, weights, tax rates

#### 3. `string` - Text
```csharp
string name = "John";
string email = "john@example.com";
string message = "Hello, World!";
```
- Use for: names, addresses, messages, any text
- **Real-world:** Customer names, product descriptions, email addresses

#### 4. `bool` - True or False
```csharp
bool isVip = true;
bool isComplete = false;
bool hasDiscount = true;
```
- Use for: yes/no questions, on/off states, flags
- **Real-world:** Is customer a VIP? Is order complete? Does product have discount?

### Example: Storing Customer Information

```csharp
string customerName = "Sarah Johnson";
int customerAge = 32;
double orderTotal = 149.99;
bool isVip = true;
```

**Real-world connection:** This is exactly how customer databases store information - each piece of data has a type and a value.

## 📖 Part 2: Getting Input from Users

### Console.ReadLine() - Asking for Information

So far, your programs only display messages. Now let's make them **ask questions** and **remember the answers**.

`Console.ReadLine()` waits for the user to type something and press Enter, then gives you what they typed.

### Example 1: Asking for a Name

```csharp
Console.Write("Enter your name: ");
string name = Console.ReadLine();
Console.WriteLine($"Hello, {name}!");
```

**What happens:**
1. Program displays: "Enter your name: "
2. Program waits (cursor blinks)
3. User types: "Sarah" and presses Enter
4. Program stores "Sarah" in the `name` variable
5. Program displays: "Hello, Sarah!"

**Try it yourself:**
1. Create a new project: `dotnet new console -o NameGreeting`
2. Replace `Program.cs` with the code above
3. Run it: `dotnet run`
4. Type your name when prompted!

### Example 2: Asking for Numbers

Here's the tricky part: `Console.ReadLine()` always gives you **text** (a string), even if the user types a number. You need to **convert** it to a number.

```csharp
Console.Write("Enter your age: ");
string ageText = Console.ReadLine();
int age = int.Parse(ageText);
Console.WriteLine($"You are {age} years old.");
```

**What's happening:**
- `Console.ReadLine()` gives us text (like "25")
- `int.Parse()` converts that text into a number (25)
- Now we can do math with it!

**For decimal numbers:**
```csharp
Console.Write("Enter the price: ");
string priceText = Console.ReadLine();
double price = double.Parse(priceText);
Console.WriteLine($"The price is ${price}");
```

### Real-World Example: Customer Registration

```csharp
Console.Write("What's your name? ");
string name = Console.ReadLine();

Console.Write("How old are you? ");
string ageText = Console.ReadLine();
int age = int.Parse(ageText);

Console.Write("What's your email? ");
string email = Console.ReadLine();

Console.WriteLine($"Welcome, {name}! Age: {age}, Email: {email}");
```

**Real-world connection:** This is how registration forms work - they ask questions and store the answers.

## 📖 Part 3: Doing Calculations

### Basic Math Operations

C# can do all the math you need:

```csharp
int a = 10;
int b = 5;

int sum = a + b;        // 15 (addition)
int difference = a - b; // 5 (subtraction)
int product = a * b;    // 50 (multiplication)
int quotient = a / b;   // 2 (division)
int remainder = a % b;  // 0 (remainder/modulo)
```

### Example: Price Calculator

```csharp
double price = 29.99;
int quantity = 3;
double total = price * quantity;
Console.WriteLine($"Total: ${total}");
```

**Output:** `Total: $89.97`

### Example: Adding Tax

```csharp
double subtotal = 100.00;
double taxRate = 0.20;  // 20% tax
double tax = subtotal * taxRate;
double total = subtotal + tax;
Console.WriteLine($"Subtotal: ${subtotal}");
Console.WriteLine($"Tax (20%): ${tax}");
Console.WriteLine($"Total: ${total}");
```

**Output:**
```
Subtotal: $100
Tax (20%): $20
Total: $120
```

**Real-world connection:** This is exactly how cash registers calculate totals!

### Example: Wage Calculator

```csharp
Console.Write("Enter hours worked: ");
string hoursText = Console.ReadLine();
double hours = double.Parse(hoursText);

Console.Write("Enter hourly rate: $");
string rateText = Console.ReadLine();
double rate = double.Parse(rateText);

double pay = hours * rate;
Console.WriteLine($"Your pay: ${pay}");
```

**Real-world connection:** Payroll systems use this exact pattern!

## 📖 Part 4: String Interpolation - Beautiful Output

### The Old Way (Concatenation)

```csharp
string name = "Sarah";
int age = 25;
Console.WriteLine("Hello, " + name + "! You are " + age + " years old.");
```

This works, but it's hard to read and easy to make mistakes.

### The Better Way (String Interpolation)

```csharp
string name = "Sarah";
int age = 25;
Console.WriteLine($"Hello, {name}! You are {age} years old.");
```

Much cleaner! The `$` at the start tells C# "this string has variables in it", and `{variableName}` inserts the value.

### Formatting Numbers

You can format numbers to look professional:

```csharp
double price = 29.99;
Console.WriteLine($"Price: ${price:F2}");  // Always 2 decimal places
```

**Output:** `Price: $29.99`

- `F2` means "format as a number with 2 decimal places"
- Useful for prices, money, percentages

### Complete Example: Order Summary

```csharp
string productName = "Wireless Mouse";
double price = 29.99;
int quantity = 2;
double subtotal = price * quantity;
double tax = subtotal * 0.20;
double total = subtotal + tax;

Console.WriteLine("=== Order Summary ===");
Console.WriteLine($"Product: {productName}");
Console.WriteLine($"Price: ${price:F2}");
Console.WriteLine($"Quantity: {quantity}");
Console.WriteLine($"Subtotal: ${subtotal:F2}");
Console.WriteLine($"Tax: ${tax:F2}");
Console.WriteLine($"Total: ${total:F2}");
```

**Output:**
```
=== Order Summary ===
Product: Wireless Mouse
Price: $29.99
Quantity: 2
Subtotal: $59.98
Tax: $11.99
Total: $71.97
```

**Real-world connection:** This is how e-commerce sites display order summaries!

## 🎓 Step-by-Step Mini Programs

### Mini Program 1: Name & Age Summary

Let's build a simple program that asks for information and displays it nicely.

**Step 1:** Create a new project
```bash
dotnet new console -o NameAgeSummary
cd NameAgeSummary
```

**Step 2:** Write the program in `Program.cs`:
```csharp
Console.Write("What's your name? ");
string name = Console.ReadLine();

Console.Write("How old are you? ");
string ageText = Console.ReadLine();
int age = int.Parse(ageText);

Console.WriteLine($"Hello, {name}! You are {age} years old.");
```

**Step 3:** Run it
```bash
dotnet run
```

**Try it:** Enter your name and age, and see the personalized message!

### Mini Program 2: VAT Calculator

Build a calculator that adds tax to a price.

**Step 1:** Create project
```bash
dotnet new console -o VatCalculator
cd VatCalculator
```

**Step 2:** Write the program:
```csharp
Console.Write("Enter the base price: $");
string priceText = Console.ReadLine();
double price = double.Parse(priceText);

Console.Write("Enter tax rate (e.g., 0.20 for 20%): ");
string taxText = Console.ReadLine();
double taxRate = double.Parse(taxText);

double tax = price * taxRate;
double total = price + tax;

Console.WriteLine($"Base Price: ${price:F2}");
Console.WriteLine($"Tax: ${tax:F2}");
Console.WriteLine($"Total: ${total:F2}");
```

**Step 3:** Run and test with different prices and tax rates!

**Real-world connection:** This is how pricing works in retail and e-commerce.

### Mini Program 3: Weekly Pay Estimator

Calculate weekly pay from hours and hourly rate.

**Step 1:** Create project
```bash
dotnet new console -o PayEstimator
cd PayEstimator
```

**Step 2:** Write the program:
```csharp
Console.Write("Enter hours worked this week: ");
string hoursText = Console.ReadLine();
double hours = double.Parse(hoursText);

Console.Write("Enter your hourly rate: $");
string rateText = Console.ReadLine();
double rate = double.Parse(rateText);

double weeklyPay = hours * rate;

Console.WriteLine($"Hours: {hours}");
Console.WriteLine($"Rate: ${rate:F2} per hour");
Console.WriteLine($"Weekly Pay: ${weeklyPay:F2}");
```

**Step 3:** Run it and calculate your pay!

**Real-world connection:** Payroll and time-tracking systems use this exact calculation.

## 📚 Key Concepts Summary

1. **Variables** - Labeled boxes that store information
   - `int` for whole numbers
   - `double` for decimal numbers
   - `string` for text
   - `bool` for true/false

2. **Console.ReadLine()** - Gets text input from the user
   - Always returns a string
   - Program waits until user presses Enter

3. **Converting Input** - Turn text into numbers
   - `int.Parse()` for whole numbers
   - `double.Parse()` for decimal numbers

4. **Calculations** - Math operations
   - `+` addition, `-` subtraction, `*` multiplication, `/` division, `%` remainder

5. **String Interpolation** - Beautiful output
   - Use `$"text {variable}"` format
   - `{variable:F2}` formats numbers with 2 decimal places

## 💻 Example Code Files

Study these example files in the `examples/` folder to see the concepts in action:

### Example 1: Variables and Data Types (`example-01-variables.cs`)
Shows how to create and use variables of different types (`string`, `int`, `double`, `bool`).

**To try it:**
1. Create a new project: `dotnet new console -o VariablesExample`
2. Copy the code from `examples/example-01-variables.cs` into `Program.cs`
3. Run it: `dotnet run`

### Example 2: Getting User Input (`example-02-user-input.cs`)
Demonstrates how to ask users for information and use it in your program.

**To try it:**
1. Create a new project: `dotnet new console -o InputExample`
2. Copy the code from `examples/example-02-user-input.cs` into `Program.cs`
3. Run it and enter your name and age when prompted!

### Example 3: Calculations and Formatting (`example-03-calculations.cs`)
Shows how to perform calculations and format output nicely.

**To try it:**
1. Create a new project: `dotnet new console -o CalculationExample`
2. Copy the code from `examples/example-03-calculations.cs` into `Program.cs`
3. Run it and enter a price and quantity to see the order summary!

**Tip:** Don't just copy-paste! Type the code yourself - it helps you learn.

## 🎓 Exercises

Now it's time to practice! Try these exercises to build your confidence. Each exercise has its own file in the `exercises/` folder with detailed instructions.

### Exercise 1: Name & Age Summary
Create a program that asks for the user's name and age, then prints a friendly summary.

**See:** `exercises/exercise-01.md` for full instructions.

### Exercise 2: VAT Calculator
Build a calculator that asks for base price and tax rate, then calculates and displays the final price with tax.

**See:** `exercises/exercise-02.md` for full instructions.

### Exercise 3: Weekly Pay Estimator
Create a program that asks for hours worked and hourly rate, then calculates and displays estimated weekly pay.

**See:** `exercises/exercise-03.md` for full instructions.

**Try each exercise yourself first!** Then check the solutions in the `exercises/` folder.

## 🧪 Quiz: Test Your Understanding

Answer these questions to check what you've learned. Answers are in `exercises/quiz-answers.md`.

### Question 1: What data type would you use to store someone's age?
A) `string`  
B) `int`  
C) `double`  
D) `bool`

### Question 2: What does `Console.ReadLine()` do?
A) Prints text to the screen  
B) Gets text input from the user  
C) Converts text to a number  
D) Saves data to a file

### Question 3: How do you convert a string to an integer?
A) `int.Convert(text)`  
B) `int.Parse(text)`  
C) `Convert.ToInt(text)`  
D) `text.ToInt()`

### Question 4: What is string interpolation?
A) A way to add numbers together  
B) A way to insert variables into text strings  
C) A way to read user input  
D) A way to format files

### Question 5: What does the `$` symbol do in `$"Hello {name}"`?
A) It's a dollar sign for money  
B) It enables string interpolation  
C) It's optional punctuation  
D) It creates a variable

## 🐛 Debug Challenge

Find the errors in this code! See `exercises/debug-challenge.md` for the full challenge.

```csharp
string name = Console.ReadLine();
int age = "25";
double price = 19.99
Console.WriteLine("Name: " + name "Age: " + age);
```

**How many errors can you find?** Check `exercises/debug-challenge-solution.md` when you're done.

## ✅ Module 2 Checklist

Before moving to Module 3, make sure you can:
- [ ] Create variables of different types (`int`, `double`, `string`, `bool`)
- [ ] Get input from users using `Console.ReadLine()`
- [ ] Convert strings to numbers using `int.Parse()` and `double.Parse()`
- [ ] Perform calculations (addition, subtraction, multiplication, division)
- [ ] Use string interpolation to format output
- [ ] Build a working price calculator
- [ ] Complete at least 3 exercises
- [ ] Answer the quiz questions correctly

## 🚀 What's Next?

In Module 3, you'll learn to make your programs **smart**:
- **If/else statements** - Make decisions (like "if customer is VIP, apply discount")
- **Loops** - Repeat tasks (like "process each item in the order")
- **Comparisons** - Check conditions (like "is age >= 18?")

You'll build programs that can:
- Check if someone is old enough
- Apply discounts based on purchase amount
- Process lists of items automatically
- Create simple menu systems

**Real-world connection:** Almost every application needs to make decisions and repeat tasks. These are fundamental skills used in customer service systems, inventory management, and data processing tools.

---

**Remember:** You're building real skills! Every concept you learn here is used in professional software. Keep practicing, and don't be afraid to experiment! 💪

---

## 🔗 Navigation

- **[Previous: Module 1 - Setup →](../module-01-setup/README.md)**
- **[Next: Module 3 - Control Flow →](../module-03-control-flow/README.md)**
- **[Back to C# Workbook →](../README.md)**
- **[Back to Course Home →](../../README.md)**
- **[Course Links →](../../COURSE-LINKS.md)**
- **[Examples →](examples/)** | **[Exercises →](exercises/)**