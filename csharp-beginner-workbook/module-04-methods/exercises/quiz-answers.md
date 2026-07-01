# Module 4 Quiz Answers

## Question 1: What is a method?
**Answer: B** - A named block of reusable code

**Explanation:** A method is a named block of code that performs a specific task. You write it once and can call it multiple times, making your code reusable and easier to maintain.

**Example:**
```csharp
static void SayHello()
{
    Console.WriteLine("Hello!");
}

SayHello();  // Call the method
SayHello();  // Call it again
```

---

## Question 2: What does `void` mean in a method declaration?
**Answer: A** - The method returns nothing

**Explanation:** `void` means the method doesn't return any value. It just performs an action (like printing something) but doesn't give you a result back.

**Example:**
```csharp
static void DisplayMessage()  // Returns nothing
{
    Console.WriteLine("Hello!");
}

static int GetAge()  // Returns an integer
{
    return 25;
}
```

---

## Question 3: What is a parameter?
**Answer: B** - Information you pass to a method

**Explanation:** A parameter is information you provide to a method when you call it. It's like giving someone ingredients to cook with - you pass in the data, and the method uses it.

**Example:**
```csharp
static void Greet(string name)  // name is a parameter
{
    Console.WriteLine($"Hello, {name}!");
}

Greet("Sarah");  // Pass "Sarah" as the parameter
Greet("John");   // Pass "John" as the parameter
```

---

## Question 4: What does `return` do?
**Answer: C** - Sends a value back from a method

**Explanation:** `return` sends a value back from a method to whoever called it. It's like giving someone a finished product after they gave you the materials.

**Example:**
```csharp
static int Add(int a, int b)
{
    int sum = a + b;
    return sum;  // Send sum back to caller
}

int result = Add(5, 3);  // result gets 8
```

---

## Question 5: Why should you use methods instead of repeating code?
**Answer: B** - Methods reduce mistakes and make code easier to maintain

**Explanation:** Methods help you:
- Write code once instead of many times
- Fix bugs in one place instead of many
- Make changes easily (change once, updates everywhere)
- Reduce copy-paste errors
- Make code more readable and organized

**Example:**
```csharp
// Without methods - repeated code, easy to make mistakes
double order1Total = 100.00 * 1.20;
double order2Total = 150.00 * 1.20;  // What if tax rate changes?
double order3Total = 75.00 * 1.20;   // Have to change everywhere!

// With methods - write once, use many times
static double AddTax(double amount)
{
    return amount * 1.20;
}

double order1Total = AddTax(100.00);
double order2Total = AddTax(150.00);
double order3Total = AddTax(75.00);
// Change tax rate in one place, updates everywhere!
```

---

## True or False: A method must always have parameters.
**Answer: False**

**Explanation:** Methods can have zero, one, or many parameters. Parameters are optional - some methods don't need any information to do their job.

**Example:**
```csharp
// Method with no parameters
static void DisplayWelcome()
{
    Console.WriteLine("Welcome!");
}

// Method with parameters
static void Greet(string name)
{
    Console.WriteLine($"Hello, {name}!");
}
```

---

## True or False: A method that returns `void` cannot have a `return` statement.
**Answer: False**

**Explanation:** A `void` method can include `return;` to exit early. It cannot return a value, but it can still use a return statement without a value.

**Example:**
```csharp
static void CheckAge(int age)
{
    if (age < 0)
    {
        return;  // Exit early, but no value returned
    }
    Console.WriteLine($"Age: {age}");
}

// This would be WRONG:
static void GetAge()
{
    return 25;  // Error! Can't return a value from void method
}
```

---

## True or False: Variables declared inside a method can be used outside that method.
**Answer: False**

**Explanation:** Variables declared inside a method are "local" to that method - they only exist inside it. This is called "scope". You cannot use them outside the method.

**Example:**
```csharp
static void Method1()
{
    int x = 10;  // x only exists inside Method1
    Console.WriteLine(x);  // ✅ This works
}

static void Method2()
{
    Console.WriteLine(x);  // ❌ Error! x doesn't exist here
}
```

---

## How Did You Do?

- **8/8 correct:** Excellent! You understand methods. Ready for Module 5! 🎉
- **5-7/8 correct:** Good work! Review the questions you missed, especially around return types and parameters. You're on the right track! 👍
- **0-4/8 correct:** No worries! Re-read Module 4, focusing on:
  - How to declare methods (`static [return type] [name]([parameters])`)
  - What `void` means (returns nothing)
  - What parameters are (information you pass in)
  - What `return` does (sends value back)
  - Why methods are useful (reduce repetition, easier to maintain)
  
  Take your time - these concepts build on each other! 💪

---

## Key Takeaways

1. **Methods are reusable blocks of code** - Write once, use many times
2. **`void` means no return value** - Method just does something, doesn't give result back
3. **Parameters are inputs** - Information you pass to the method
4. **`return` sends values back** - Methods can give you results
5. **Variables in methods are local** - They only exist inside that method
6. **Methods reduce mistakes** - Change code once, fixes everywhere

**Remember:** Every expert was once a beginner. Keep practicing! 🚀

