# Debug Challenge Solution: Find the Errors

## The Broken Code

```csharp
Console.WriteLine("Welcome to my program")
Console.WriteLine("This is line 2";
Console.Writeline("This is line 3");
```

## The Errors Found

### Error 1: Missing semicolon on line 1
```csharp
Console.WriteLine("Welcome to my program")  // ❌ Missing semicolon
```
**Should be:**
```csharp
Console.WriteLine("Welcome to my program");  // ✅ Has semicolon
```

### Error 2: Missing closing parenthesis on line 2
```csharp
Console.WriteLine("This is line 2";  // ❌ Missing closing parenthesis
```
**Should be:**
```csharp
Console.WriteLine("This is line 2");  // ✅ Has closing parenthesis
```

### Error 3: Wrong capitalization on line 3
```csharp
Console.Writeline("This is line 3");  // ❌ "Writeline" should be "WriteLine"
```
**Should be:**
```csharp
Console.WriteLine("This is line 3");  // ✅ Correct capitalization
```

## The Fixed Code

```csharp
Console.WriteLine("Welcome to my program");
Console.WriteLine("This is line 2");
Console.WriteLine("This is line 3");
```

## Explanation of Common Errors

### 1. Missing Semicolons
- **What it is:** Every statement in C# must end with a semicolon `;`
- **Why it matters:** The semicolon tells C# "this command is finished"
- **How to remember:** Think of it like a period at the end of a sentence

### 2. Missing Parentheses
- **What it is:** Parentheses `()` must come in pairs - opening `(` and closing `)`
- **Why it matters:** They tell C# what information to pass to the command
- **How to remember:** Like opening and closing a box

### 3. Case Sensitivity
- **What it is:** C# is case-sensitive - `WriteLine` is different from `Writeline`
- **Why it matters:** C# won't recognize commands with wrong capitalization
- **How to remember:** C# is picky about capital letters - they must match exactly

## Common Error Messages You Might See

If you run the broken code, you might see errors like:

```
error CS1002: ; expected
error CS1026: ) expected
error CS0117: 'Console' does not contain a definition for 'Writeline'
```

## Tips for Finding Errors

1. **Read error messages carefully** - They usually tell you what's wrong and where
2. **Check punctuation** - Semicolons, parentheses, quotes
3. **Check spelling and capitalization** - C# is very picky!
4. **Count your quotes** - Make sure every opening quote `"` has a closing quote `"`
5. **Use VS Code's red squiggles** - Red underlines usually mean errors

## Practice

Try finding the errors in this code:

```csharp
Console.WriteLine("Hello"
Console.Writeline("World");
Console.WriteLine("Test");
```

**How many errors can you find?** (Answer: 3)

