# Module 2 Quiz Answers

## Question 1: What data type would you use to store someone's age?
**Answer: B** - `int`

**Explanation:** Age is a whole number (like 25, 30, 45), so we use `int` (integer). We wouldn't use `double` unless we needed decimals (like 25.5 years, which doesn't make sense for age), and we wouldn't use `string` because we might want to do math with ages.

---

## Question 2: What does `Console.ReadLine()` do?
**Answer: B** - Gets text input from the user

**Explanation:** `Console.ReadLine()` waits for the user to type something and press Enter, then returns what they typed as a string. It's how programs get information from users.

---

## Question 3: How do you convert a string to an integer?
**Answer: B** - `int.Parse(text)`

**Explanation:** `int.Parse()` takes a string (like "25") and converts it to an integer (25). This is necessary because `Console.ReadLine()` always returns a string, even if the user types a number.

**Example:**
```csharp
string ageText = "25";
int age = int.Parse(ageText);  // Converts "25" to 25
```

---

## Question 4: What is string interpolation?
**Answer: B** - A way to insert variables into text strings

**Explanation:** String interpolation lets you put variables directly into strings using `$"text {variable}"` syntax. It's cleaner and easier to read than concatenation.

**Example:**
```csharp
string name = "Sarah";
Console.WriteLine($"Hello, {name}!");  // Outputs: Hello, Sarah!
```

---

## Question 5: What does the `$` symbol do in `$"Hello {name}"`?
**Answer: B** - It enables string interpolation

**Explanation:** The `$` at the start of a string tells C# "this string contains variables that should be inserted." Without it, `{name}` would be treated as literal text.

**Example:**
```csharp
string name = "Sarah";
Console.WriteLine($"Hello, {name}!");    // ✅ Outputs: Hello, Sarah!
Console.WriteLine("Hello, {name}!");     // ❌ Outputs: Hello, {name}!
```

---

## True or False: `Console.ReadLine()` always returns a string, even if the user types a number.
**Answer: True**

**Explanation:** `Console.ReadLine()` always returns a `string` type. If the user types "25", you get the string "25", not the number 25. That's why you need `int.Parse()` or `double.Parse()` to convert it to a number.

---

## True or False: You can do math directly with the result of `Console.ReadLine()` without converting it first.
**Answer: False**

**Explanation:** Since `Console.ReadLine()` returns a string, you cannot do math with it directly. You must first convert it to a number using `int.Parse()` or `double.Parse()`.

**Example:**
```csharp
// WRONG - This won't work!
string input = Console.ReadLine();
int result = input + 5;  // Error: can't add string and number

// CORRECT - Convert first!
string input = Console.ReadLine();
int number = int.Parse(input);
int result = number + 5;  // ✅ This works!
```

---

## True or False: String interpolation is the only way to combine text and variables in C#.
**Answer: False**

**Explanation:** String interpolation is one way, but you can also use concatenation with `+`. String interpolation is generally preferred because it's cleaner and easier to read.

**Example:**
```csharp
string name = "Sarah";
int age = 25;

// Method 1: String interpolation (preferred)
Console.WriteLine($"Hello, {name}! You are {age} years old.");

// Method 2: Concatenation (also works)
Console.WriteLine("Hello, " + name + "! You are " + age + " years old.");
```

---

## How Did You Do?

- **8/8 correct:** Excellent! You understand the basics of variables, input, and string formatting. Ready for Module 3! 🎉
- **5-7/8 correct:** Good work! Review the questions you missed, especially around data types and conversions. You're on the right track! 👍
- **0-4/8 correct:** No worries! Re-read Module 2, focusing on:
  - How variables work (different types)
  - How `Console.ReadLine()` works (always returns string)
  - How to convert strings to numbers (`int.Parse`, `double.Parse`)
  - How string interpolation works (`$"text {variable}"`)
  
  Take your time - these concepts build on each other! 💪

---

## Key Takeaways

1. **Variables store information** - Use the right type (`int`, `double`, `string`, `bool`)
2. **Console.ReadLine() always returns a string** - Convert to numbers when needed
3. **String interpolation is your friend** - Use `$"text {variable}"` for clean output
4. **Practice makes perfect** - Keep coding and these concepts will become natural!

**Remember:** Every expert was once a beginner. Keep practicing! 🚀

