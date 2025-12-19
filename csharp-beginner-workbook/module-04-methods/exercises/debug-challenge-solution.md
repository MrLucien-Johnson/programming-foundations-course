# Debug Challenge Solution: Find the Errors

## The Broken Code

```csharp
void CalculateTotal(price, quantity)
{
    double total = price * quantity;
    return total;
}

double result = CalculateTotal(10.50, 3);
Console.WriteLine("Total: " + result);
```

## The Errors Found

### Error 1: Missing `static` keyword
```csharp
void CalculateTotal(price, quantity)  // ❌ Missing static
```
**Problem:** Methods need the `static` keyword (for now, just include it).

**Should be:**
```csharp
static void CalculateTotal(price, quantity)  // ✅ Has static
```

### Error 2: Missing parameter types
```csharp
void CalculateTotal(price, quantity)  // ❌ Missing types for parameters
```
**Problem:** Parameters must have their types specified (`double`, `int`, `string`, etc.).

**Should be:**
```csharp
void CalculateTotal(double price, int quantity)  // ✅ Has types
```

### Error 3: Wrong return type
```csharp
void CalculateTotal(...)  // ❌ Says void (returns nothing)
{
    return total;  // But tries to return a value!
}
```
**Problem:** Method declares `void` (returns nothing) but tries to return `total`. If you want to return a value, the return type must match (`double` in this case).

**Should be:**
```csharp
static double CalculateTotal(double price, int quantity)  // ✅ Returns double
{
    double total = price * quantity;
    return total;
}
```

## The Fixed Code

```csharp
static double CalculateTotal(double price, int quantity)
{
    double total = price * quantity;
    return total;
}

double result = CalculateTotal(10.50, 3);
Console.WriteLine("Total: " + result);
```

## Explanation of Common Errors

### 1. Missing `static` Keyword
- **What it is:** Methods need `static` keyword (for console applications)
- **Why it matters:** C# requires `static` for methods in console apps
- **How to remember:** Always start methods with `static`

### 2. Missing Parameter Types
- **What it is:** Every parameter must have a type (`double`, `int`, `string`, etc.)
- **Why it matters:** C# needs to know what type of data you're passing
- **How to remember:** Parameters are like variable declarations: `type name`

### 3. Return Type Mismatch
- **What it is:** If you use `return`, the method must declare a return type (not `void`)
- **Why it matters:** `void` means "returns nothing", so you can't return a value
- **How to remember:** 
  - `void` = no return value, no `return` statement needed
  - `double`, `int`, `bool`, etc. = returns that type, must have `return` statement

## Common Error Messages You Might See

If you run the broken code, you might see errors like:

```
error CS0106: The modifier 'static' is not valid for this item
error CS0246: The type or namespace name 'price' could not be found
error CS0127: Since 'CalculateTotal' returns void, a return keyword must not be followed by an object expression
```

## Tips for Finding Errors

1. **Read error messages carefully** - They usually tell you what's wrong and where
2. **Check method declaration** - Does it have `static`? Correct return type? Parameter types?
3. **Check return statements** - If method returns `void`, you can't use `return` with a value
4. **Use VS Code/Cursor's red squiggles** - They highlight errors
5. **Read code line by line** - Go slowly and check each part

## Practice

Try finding the errors in this code:

```csharp
string GreetUser(name)
{
    string message = "Hello, " + name;
    return message;
}

int AddNumbers(a, b)
{
    return a + b;
}

void DisplayTotal()
{
    double total = 100.50;
    return total;
}
```

**How many errors can you find?** (Answer: 6)

