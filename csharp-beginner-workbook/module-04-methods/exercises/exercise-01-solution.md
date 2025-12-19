# Exercise 1 Solution: Print Header Method

## Solution Code

```csharp
static void DisplayHeader()
{
    Console.WriteLine("========================================");
    Console.WriteLine("         SALES REPORT");
    Console.WriteLine("========================================");
    Console.WriteLine();
}

DisplayHeader();

Console.WriteLine("Report Content:");
Console.WriteLine("- Sales: $50,000");
Console.WriteLine("- Expenses: $30,000");
Console.WriteLine("- Profit: $20,000");

Console.WriteLine();
DisplayHeader();
```

## Explanation

This solution demonstrates:
1. **Simple void method** - No parameters, no return value
2. **Reusable code** - Write once, call multiple times
3. **Consistent formatting** - Same header format every time
4. **Clean organization** - Header logic separated from content

## Key Points

- `static void` - Method doesn't return anything, just does something
- Method name is clear and descriptive (`DisplayHeader`)
- Formatting is consistent and professional
- Can be called multiple times with the same result

## Variations

### Option 1: With Title Parameter
```csharp
static void DisplayHeader(string title)
{
    Console.WriteLine("========================================");
    Console.WriteLine($"         {title.ToUpper()}");
    Console.WriteLine("========================================");
    Console.WriteLine();
}

DisplayHeader("Sales Report");
DisplayHeader("Monthly Summary");
DisplayHeader("Annual Review");
```

### Option 2: With Date
```csharp
static void DisplayHeader(string title, string date)
{
    Console.WriteLine("========================================");
    Console.WriteLine($"         {title.ToUpper()}");
    Console.WriteLine($"         Generated: {date}");
    Console.WriteLine("========================================");
    Console.WriteLine();
}

DisplayHeader("Sales Report", "2024-01-15");
```

### Option 3: With Separator Character
```csharp
static void DisplayHeader(string title, char separator)
{
    string line = new string(separator, 40);
    Console.WriteLine(line);
    Console.WriteLine($"         {title}");
    Console.WriteLine(line);
    Console.WriteLine();
}

DisplayHeader("Sales Report", '=');
DisplayHeader("Monthly Summary", '-');
```

### Option 4: With Matching Footer
```csharp
static void DisplayHeader()
{
    Console.WriteLine("========================================");
    Console.WriteLine("         SALES REPORT");
    Console.WriteLine("========================================");
    Console.WriteLine();
}

static void DisplayFooter()
{
    Console.WriteLine();
    Console.WriteLine("========================================");
    Console.WriteLine("         End of Report");
    Console.WriteLine("========================================");
}

DisplayHeader();
Console.WriteLine("Report content here...");
DisplayFooter();
```

## Common Mistakes to Avoid

1. **Forgetting static keyword:**
   ```csharp
   // WRONG - Missing static
   void DisplayHeader()  // Error!
   {
       // ...
   }
   ```

2. **Not calling the method:**
   ```csharp
   // WRONG - Defined but never called
   static void DisplayHeader()
   {
       // ...
   }
   // Missing: DisplayHeader();
   ```

3. **Wrong method name when calling:**
   ```csharp
   // WRONG - Typo in method name
   static void DisplayHeader() { }
   
   DisplayHeadr();  // Error! Method doesn't exist
   ```

## Real-World Application

This pattern is used in:
- Report generation systems
- Document formatting
- Email templates
- Invoice generation
- Data export tools

## Try This

Modify the method to:
- Accept a title as a parameter
- Include the current date/time
- Add company name or logo area
- Create matching header and footer methods
- Add different header styles (simple, fancy, minimal)

