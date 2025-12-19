# Debug Challenge Solution: Find the Errors

## The Broken Code

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

## The Errors Found

### Error 1: Missing `{ get; set; }` on Title property
```csharp
public string Title  // ❌ Missing { get; set; }
```
**Problem:** Properties need `{ get; set; }` to be complete properties.

**Should be:**
```csharp
public string Title { get; set; }  // ✅ Complete property
```

### Error 2: Missing `{ get; set; }` on Price property
```csharp
public double Price  // ❌ Missing { get; set; }
```
**Problem:** Same issue - properties need `{ get; set; }`.

**Should be:**
```csharp
public double Price { get; set; }  // ✅ Complete property
```

### Error 3: Missing parameter types in constructor
```csharp
public Book(title, price)  // ❌ Missing types
```
**Problem:** Constructor parameters must have types specified.

**Should be:**
```csharp
public Book(string title, double price)  // ✅ Has types
```

### Error 4: Missing `+` operator in string concatenation
```csharp
Console.WriteLine("Title: " + Title "Price: $" + Price);  // ❌ Missing + between Title and "Price"
```
**Problem:** When concatenating strings, you need `+` between each part.

**Should be:**
```csharp
Console.WriteLine("Title: " + Title + " Price: $" + Price);  // ✅ Has + between all parts
```

### Error 5: Missing `new` keyword when creating object
```csharp
Book myBook = Book("C# Guide", 29.99);  // ❌ Missing new
```
**Problem:** Must use `new` keyword to create an object.

**Should be:**
```csharp
Book myBook = new Book("C# Guide", 29.99);  // ✅ Has new keyword
```

## The Fixed Code

```csharp
class Book
{
    public string Title { get; set; }  // Fixed: Added { get; set; }
    public double Price { get; set; }   // Fixed: Added { get; set; }
    
    public Book(string title, double price)  // Fixed: Added parameter types
    {
        Title = title;
        Price = price;
    }
    
    public void DisplayInfo()
    {
        Console.WriteLine("Title: " + Title + " Price: $" + Price);  // Fixed: Added + operator
    }
}

Book myBook = new Book("C# Guide", 29.99);  // Fixed: Added new keyword
myBook.DisplayInfo();
```

## Even Better: Using String Interpolation

```csharp
class Book
{
    public string Title { get; set; }
    public double Price { get; set; }
    
    public Book(string title, double price)
    {
        Title = title;
        Price = price;
    }
    
    public void DisplayInfo()
    {
        Console.WriteLine($"Title: {Title} Price: ${Price:F2}");  // Cleaner with string interpolation!
    }
}

Book myBook = new Book("C# Guide", 29.99);
myBook.DisplayInfo();
```

## Explanation of Common Errors

### 1. Incomplete Properties
- **What it is:** Properties need `{ get; set; }` to be complete
- **Why it matters:** Without `{ get; set; }`, it's just a field declaration, not a property
- **How to remember:** Properties always have `{ get; set; }` after the type and name

### 2. Missing Parameter Types
- **What it is:** Constructor parameters must specify their types
- **Why it matters:** C# needs to know what type of data you're passing
- **How to remember:** Parameters are like variable declarations: `type name`

### 3. Missing Operators in String Concatenation
- **What it is:** When combining strings with `+`, you need `+` between each part
- **Why it matters:** C# needs to know you want to combine, not just put things next to each other
- **How to remember:** Use string interpolation (`$"..."`) - it's easier!

### 4. Missing `new` Keyword
- **What it is:** Must use `new` to create objects
- **Why it matters:** `new` tells C# to create a new instance
- **How to remember:** Always use `new ClassName()` when creating objects

## Common Error Messages You Might See

If you run the broken code, you might see errors like:

```
error CS1002: ; expected
error CS0246: The type or namespace name 'title' could not be found
error CS1003: Syntax error, '+' expected
error CS0119: 'Book' is a type, which is not valid in the given context
```

## Tips for Finding Errors

1. **Read error messages carefully** - They usually tell you what's wrong and where
2. **Check property syntax** - Must have `{ get; set; }`
3. **Check constructor parameters** - Must have types
4. **Check string concatenation** - Need `+` between parts
5. **Check object creation** - Must use `new` keyword
6. **Use VS Code/Cursor's red squiggles** - They highlight errors

## Practice

Try finding the errors in this code:

```csharp
class Employee
{
    public string Name
    public int Age
    
    public Employee(name, age)
    {
        Name = name;
        Age = age;
    }
    
    public void ShowInfo()
    {
        Console.WriteLine("Name: " + Name "Age: " + Age);
    }
}

Employee emp = Employee("John", 30);
emp.ShowInfo();
```

**How many errors can you find?** (Answer: 5)

