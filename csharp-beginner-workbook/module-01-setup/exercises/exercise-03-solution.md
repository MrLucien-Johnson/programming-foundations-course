# Exercise 3 Solution: Predict the Output

## The Code

```csharp
Console.WriteLine("First line");
Console.WriteLine("Second line");
Console.WriteLine("Third line");
Console.WriteLine("First line");
```

## The Output

```
First line
Second line
Third line
First line
```

## Answers to the Questions

1. **How many lines will be printed?**  
   Answer: 4 lines

2. **Will "First line" appear twice?**  
   Answer: Yes, because it's printed twice in the code

3. **What order will they appear in?**  
   Answer: First line, Second line, Third line, First line (in that exact order)

## Key Learning Points

- Programs execute line by line, from top to bottom
- The same text can be printed multiple times
- The order of `Console.WriteLine` statements determines the output order
- Each `Console.WriteLine` creates a new line in the output

## Why This Matters

Understanding the order of execution is crucial for programming. Your programs will always run from top to bottom, one line at a time. This helps you:
- Predict what your program will do
- Debug problems (trace through line by line)
- Plan your code structure

## Try This

Predict what this will output, then run it:

```csharp
Console.WriteLine("Start");
Console.WriteLine("Middle");
Console.WriteLine("End");
Console.WriteLine("Start");
Console.WriteLine("End");
```

**Your prediction:** _______________

**Actual output:** _______________

