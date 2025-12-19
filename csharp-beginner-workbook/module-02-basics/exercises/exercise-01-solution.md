# Exercise 1 Solution: Name & Age Summary

## Solution Code

```csharp
Console.Write("What's your name? ");
string name = Console.ReadLine();

Console.Write("How old are you? ");
string ageText = Console.ReadLine();
int age = int.Parse(ageText);

Console.WriteLine($"Hello, {name}! You are {age} years old.");
```

## Explanation

This solution demonstrates:
1. **Getting text input** - `Console.ReadLine()` gets the name as text
2. **Getting numeric input** - Gets age as text, then converts it with `int.Parse()`
3. **String interpolation** - Uses `$"..."` to combine text and variables nicely

## Key Points

- `Console.ReadLine()` always returns a string, so we need `int.Parse()` for the age
- String interpolation (`$"..."`) makes the output clean and readable
- The prompts are clear and friendly

## Variations

You could also write it like this:

```csharp
// More detailed version
Console.Write("Please enter your name: ");
string name = Console.ReadLine();

Console.Write("Please enter your age: ");
string ageText = Console.ReadLine();
int age = int.Parse(ageText);

Console.WriteLine($"Welcome, {name}!");
Console.WriteLine($"You are {age} years old.");
```

Or with more formatting:

```csharp
Console.Write("Name: ");
string name = Console.ReadLine();

Console.Write("Age: ");
int age = int.Parse(Console.ReadLine());

Console.WriteLine($"=== Summary ===");
Console.WriteLine($"Name: {name}");
Console.WriteLine($"Age: {age}");
```

## Common Mistakes to Avoid

1. **Forgetting to convert age:**
   ```csharp
   // WRONG - This won't work!
   int age = Console.ReadLine();  // Error: can't convert string to int
   ```

2. **Missing the $ in string interpolation:**
   ```csharp
   // WRONG - This won't work!
   Console.WriteLine("Hello, {name}!");  // Will literally print "{name}"
   ```

3. **Forgetting semicolons:**
   ```csharp
   // WRONG - Missing semicolon
   string name = Console.ReadLine()  // Error: missing semicolon
   ```

## Try This

Modify the program to also ask for:
- Favorite color
- City where you live
- One interesting fact about yourself

Then display all the information in a nice summary!

