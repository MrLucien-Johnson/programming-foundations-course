# Debug Challenge Solution: Find the Errors

## The Broken Code

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

## The Errors Found

### Error 1: Missing parentheses in if statement
```csharp
if age >= 18  // ❌ Missing parentheses around condition
```
**Problem:** If statements require parentheses around the condition.

**Should be:**
```csharp
if (age >= 18)  // ✅ Has parentheses
```

### Error 2: Missing braces for else clause
```csharp
else
    Console.WriteLine("Minor");  // ❌ Missing braces
}
```
**Problem:** While single-line else can work without braces, the closing brace `}` doesn't match anything because the if statement's opening brace is on a different line. Best practice is to always use braces.

**Should be:**
```csharp
else
{
    Console.WriteLine("Minor");  // ✅ Has braces
}
```

### Error 3: Extra closing brace after else
```csharp
else
    Console.WriteLine("Minor");
}  // ❌ Extra closing brace - doesn't match anything
```
**Problem:** There's an extra `}` that doesn't match any opening brace.

**Should be:** Remove this extra brace.

### Error 4: Extra closing brace after for loop
```csharp
for (int i = 0; i < 5; i++)
    Console.WriteLine(i);
}  // ❌ Extra closing brace - doesn't match anything
```
**Problem:** The for loop doesn't have an opening brace `{`, so the closing brace `}` doesn't match anything.

**Should be:** Either add opening brace, or remove closing brace.

## The Fixed Code

```csharp
int age = 25;
if (age >= 18)  // Fixed: Added parentheses
{
    Console.WriteLine("Adult");
}
else
{
    Console.WriteLine("Minor");  // Fixed: Added braces
}

for (int i = 0; i < 5; i++)
{
    Console.WriteLine(i);  // Fixed: Added braces
}
```

## Even Better: Consistent Style

```csharp
int age = 25;

if (age >= 18)
{
    Console.WriteLine("Adult");
}
else
{
    Console.WriteLine("Minor");
}

for (int i = 0; i < 5; i++)
{
    Console.WriteLine(i);
}
```

## Explanation of Common Errors

### 1. Missing Parentheses in If Statements
- **What it is:** If statements require `(condition)` - parentheses around the condition
- **Why it matters:** C# syntax requires parentheses for if statements
- **How to remember:** Always put conditions in parentheses: `if (condition)`

### 2. Missing or Mismatched Braces
- **What it is:** Braces `{ }` must come in matching pairs
- **Why it matters:** Braces define code blocks
- **How to remember:** Every opening `{` needs a closing `}`, and vice versa

### 3. Braces for Single-Line Statements
- **What it is:** While single-line if/else/for can work without braces, it's best practice to always use them
- **Why it matters:** Prevents errors when adding more code, makes code clearer
- **How to remember:** Always use braces, even for single statements

## Common Error Messages You Might See

If you run the broken code, you might see errors like:

```
error CS1002: ; expected
error CS1513: } expected
error CS1525: Invalid expression term
error CS1003: Syntax error, '(' expected
```

## Tips for Finding Errors

1. **Read error messages carefully** - They usually tell you what's wrong and where
2. **Check parentheses** - If statements need `(condition)`
3. **Count braces** - Make sure every `{` has a matching `}`
4. **Use VS Code/Cursor's matching** - Hover over a brace to see its match
5. **Format your code** - Proper indentation helps spot missing braces

## Practice

Try finding the errors in this code:

```csharp
int score = 85;
if score >= 90
{
    Console.WriteLine("Grade A");
else if score >= 80
    Console.WriteLine("Grade B");
}

for int i = 0; i < 10; i++
{
    Console.WriteLine(i);
}
```

**How many errors can you find?** (Answer: 5)

