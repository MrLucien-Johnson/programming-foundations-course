# Module 3 Quiz Answers

## Question 1: What does an if statement do?
**Answer: B** - Makes a decision based on a condition

**Explanation:** An if statement checks a condition (like `age >= 18`) and executes code only if that condition is true. It's how programs make decisions.

**Example:**
```csharp
if (age >= 18)
{
    Console.WriteLine("You can vote!");
}
```

---

## Question 2: When would you use a for loop vs a while loop?
**Answer: A** - Use `for` when you know how many times to repeat, `while` when you don't

**Explanation:** 
- **For loops** are great when you know exactly how many times to repeat (e.g., "do this 10 times", "process each item in this list of 5 items")
- **While loops** are better when you don't know how many times (e.g., "keep asking until user enters valid input", "process until queue is empty")

**Example:**
```csharp
// For loop - we know we want to count to 10
for (int i = 1; i <= 10; i++)
{
    Console.WriteLine(i);
}

// While loop - we don't know how many times
while (password != correctPassword)
{
    Console.Write("Enter password: ");
    password = Console.ReadLine();
}
```

---

## Question 3: What is the difference between `==` and `=` in C#?
**Answer: A** - `==` compares values, `=` assigns values

**Explanation:**
- `=` is the **assignment operator** - it puts a value into a variable: `age = 25` (put 25 into age)
- `==` is the **equality operator** - it checks if two values are equal: `age == 25` (is age equal to 25?)

**Example:**
```csharp
int age = 25;        // Assign 25 to age
if (age == 25)       // Check if age equals 25
{
    Console.WriteLine("You're 25!");
}
```

**Common mistake:** Using `=` instead of `==` in conditions:
```csharp
// WRONG - This assigns instead of comparing!
if (age = 25)  // Error! This assigns 25 to age, doesn't compare
```

---

## Question 4: How do you make a loop repeat forever (until broken)?
**Answer: B** - `while (true)`

**Explanation:** `while (true)` creates a loop that runs forever because `true` is always true. You use `break` to exit it when needed.

**Example:**
```csharp
while (true)
{
    Console.Write("Enter command (or 'quit' to exit): ");
    string command = Console.ReadLine();
    
    if (command == "quit")
    {
        break;  // Exit the loop
    }
    
    // Process command...
}
```

**Note:** `for (;;)` also works (empty for loop), but `while (true)` is clearer and more common.

---

## Question 5: What does `break` do in a loop?
**Answer: B** - Stops the loop immediately

**Explanation:** `break` immediately exits the loop, regardless of the loop condition. The program continues with the code after the loop.

**Example:**
```csharp
for (int i = 1; i <= 10; i++)
{
    if (i == 5)
    {
        break;  // Exit loop when i is 5
    }
    Console.WriteLine(i);
}
// Output: 1, 2, 3, 4 (stops at 5)
```

**Note:** `continue` skips to the next iteration, `break` exits the loop entirely.

---

## True or False: An if statement must always have an else clause.
**Answer: False**

**Explanation:** An `else` clause is optional. You can have an `if` statement without an `else`.

**Example:**
```csharp
// This is perfectly valid - no else needed
if (age >= 18)
{
    Console.WriteLine("You can vote!");
}
// Code continues here whether condition was true or false
```

---

## True or False: A while loop will run at least once, even if the condition is false.
**Answer: False**

**Explanation:** A `while` loop checks the condition **before** running. If the condition is false from the start, the loop never runs.

**Example:**
```csharp
int count = 10;

while (count < 5)  // Condition is false (10 is not < 5)
{
    Console.WriteLine(count);  // This never runs!
    count++;
}
```

**Note:** A `do-while` loop runs at least once because it checks the condition **after** running.

---

## True or False: You can nest if statements inside other if statements.
**Answer: True**

**Explanation:** You can put if statements inside other if statements. This is called "nesting" and is very common.

**Example:**
```csharp
if (age >= 18)
{
    if (hasLicense)
    {
        Console.WriteLine("You can drive!");
    }
    else
    {
        Console.WriteLine("You need a license to drive.");
    }
}
else
{
    Console.WriteLine("You're too young to drive.");
}
```

---

## How Did You Do?

- **8/8 correct:** Excellent! You understand control flow. Ready for Module 4! 🎉
- **5-7/8 correct:** Good work! Review the questions you missed, especially around loop types and operators. You're on the right track! 👍
- **0-4/8 correct:** No worries! Re-read Module 3, focusing on:
  - How if/else statements work
  - The difference between `=` and `==`
  - When to use `for` vs `while` loops
  - How `break` works
  
  Take your time - these concepts build on each other! 💪

---

## Key Takeaways

1. **If statements make decisions** - They check conditions and execute code accordingly
2. **Loops repeat code** - `for` when you know how many times, `while` when you don't
3. **`==` compares, `=` assigns** - Don't mix them up!
4. **`break` exits loops** - Use it when you need to stop early
5. **You can nest statements** - If inside if, loops inside loops, etc.

**Remember:** Every expert was once a beginner. Keep practicing! 🚀

