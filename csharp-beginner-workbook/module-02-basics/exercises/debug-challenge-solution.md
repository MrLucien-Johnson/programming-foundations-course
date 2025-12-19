# Debug Challenge Solution: Find the Errors

## The Broken Code

```csharp
string name = Console.ReadLine();
int age = "25";
double price = 19.99
Console.WriteLine("Name: " + name "Age: " + age);
```

## The Errors Found

### Error 1: Wrong data type on line 2
```csharp
int age = "25";  // ❌ Can't assign a string to an int variable
```
**Problem:** `age` is declared as `int` (a number), but `"25"` is a string (text in quotes).

**Should be:**
```csharp
int age = 25;  // ✅ No quotes - it's a number
```
OR if you want to convert from string:
```csharp
int age = int.Parse("25");  // ✅ Convert string to int
```

### Error 2: Missing semicolon on line 3
```csharp
double price = 19.99  // ❌ Missing semicolon
```
**Problem:** Every statement in C# must end with a semicolon.

**Should be:**
```csharp
double price = 19.99;  // ✅ Has semicolon
```

### Error 3: Missing + operator on line 4
```csharp
Console.WriteLine("Name: " + name "Age: " + age);  // ❌ Missing + between name and "Age"
```
**Problem:** When concatenating strings, you need `+` between each part.

**Should be:**
```csharp
Console.WriteLine("Name: " + name + " Age: " + age);  // ✅ Has + between all parts
```

### Error 4: No prompt for user input
```csharp
string name = Console.ReadLine();  // ⚠️ Works, but user doesn't know what to enter
```
**Problem:** The program waits for input but doesn't tell the user what to type.

**Better:**
```csharp
Console.Write("Enter your name: ");  // ✅ Tell user what to do
string name = Console.ReadLine();
```

## The Fixed Code

```csharp
Console.Write("Enter your name: ");
string name = Console.ReadLine();

int age = 25;  // Fixed: removed quotes, or could use int.Parse()
double price = 19.99;  // Fixed: added semicolon

Console.WriteLine("Name: " + name + " Age: " + age);  // Fixed: added + operator
```

## Even Better: Using String Interpolation

```csharp
Console.Write("Enter your name: ");
string name = Console.ReadLine();

int age = 25;
double price = 19.99;

Console.WriteLine($"Name: {name} Age: {age}");  // Cleaner with string interpolation!
```

## Explanation of Common Errors

### 1. Type Mismatch
- **What it is:** Trying to put the wrong type of data into a variable
- **Why it matters:** C# is "type-safe" - it won't let you mix types incorrectly
- **How to remember:** Numbers don't have quotes, text does

### 2. Missing Semicolons
- **What it is:** Every statement must end with `;`
- **Why it matters:** Tells C# "this command is finished"
- **How to remember:** Like a period at the end of a sentence

### 3. Missing Operators
- **What it is:** When combining strings, you need `+` between each part
- **Why it matters:** C# needs to know you want to combine, not just put things next to each other
- **How to remember:** Use string interpolation (`$"..."`) - it's easier!

## Common Error Messages You Might See

If you run the broken code, you might see errors like:

```
error CS0029: Cannot implicitly convert type 'string' to 'int'
error CS1002: ; expected
error CS1003: Syntax error, '+' expected
```

## Tips for Finding Errors

1. **Read error messages carefully** - They usually tell you what's wrong and where
2. **Check data types** - Make sure types match (int vs string)
3. **Check punctuation** - Semicolons, quotes, operators
4. **Use VS Code/Cursor's red squiggles** - They highlight errors
5. **Read code line by line** - Go slowly and check each part

## Practice

Try finding the errors in this code:

```csharp
string productName = "Widget";
int quantity = "5";
double cost = 10.50
Console.WriteLine("Product: " + productName "Quantity: " + quantity);
```

**How many errors can you find?** (Answer: 3)

