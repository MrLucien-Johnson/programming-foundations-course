# Exercise 1 Solution: Grade Classifier

## Solution Code

```csharp
Console.Write("Enter test score (0-100): ");
string scoreText = Console.ReadLine();
int score = int.Parse(scoreText);

string grade;

if (score >= 90 && score <= 100)
{
    grade = "A";
}
else if (score >= 80 && score < 90)
{
    grade = "B";
}
else if (score >= 70 && score < 80)
{
    grade = "C";
}
else if (score >= 60 && score < 70)
{
    grade = "D";
}
else
{
    grade = "F";
}

Console.WriteLine($"Grade: {grade}");
```

## Explanation

This solution demonstrates:
1. **Getting numeric input** - Reads score and converts to integer
2. **Multiple conditions** - Uses `else if` to check different ranges
3. **Range checking** - Uses `>=` and `<` to define grade boundaries
4. **Default case** - Uses `else` for scores below 60 (Grade F)

## Key Points

- Check highest grades first (A, then B, then C, etc.)
- Use `>=` for lower bound and `<` for upper bound (or `<=` for inclusive)
- The `else` handles all scores below 60
- Store the grade in a variable, then display it

## Variations

### Option 1: Simplified (without upper bound check)
```csharp
if (score >= 90)
{
    grade = "A";
}
else if (score >= 80)
{
    grade = "B";
}
else if (score >= 70)
{
    grade = "C";
}
else if (score >= 60)
{
    grade = "D";
}
else
{
    grade = "F";
}
```

This works because we check from highest to lowest - if score is 85, it's not >= 90, so it checks >= 80, which is true, so it stops there.

### Option 2: With Validation
```csharp
if (score < 0 || score > 100)
{
    Console.WriteLine("Invalid score! Score must be between 0 and 100.");
}
else
{
    // Grade classification code here
}
```

### Option 3: With Messages
```csharp
if (score >= 90)
{
    grade = "A";
    Console.WriteLine("Excellent work!");
}
else if (score >= 80)
{
    grade = "B";
    Console.WriteLine("Good job!");
}
// ... etc
```

## Common Mistakes to Avoid

1. **Checking ranges in wrong order:**
   ```csharp
   // WRONG - This won't work correctly!
   if (score >= 60)  // This catches scores 60-100!
   {
       grade = "D";
   }
   else if (score >= 70)  // This never runs!
   {
       grade = "C";
   }
   ```

2. **Overlapping ranges:**
   ```csharp
   // WRONG - Score of 90 matches both conditions!
   if (score >= 90 && score <= 100)
   {
       grade = "A";
   }
   if (score >= 80 && score <= 100)  // Should be < 90
   {
       grade = "B";
   }
   ```

3. **Using = instead of ==:**
   ```csharp
   // WRONG - This assigns, not compares!
   if (score = 90)  // Error!
   {
       grade = "A";
   }
   ```

## Real-World Application

This pattern is used in:
- Educational systems (grading)
- Performance rating systems
- Classification systems (good/better/best)
- Tiered pricing systems

## Try This

Modify the program to:
- Add plus/minus grades (A+, A, A-, B+, etc.)
- Show percentage ranges for each grade
- Add validation for scores outside 0-100
- Calculate GPA based on letter grade

