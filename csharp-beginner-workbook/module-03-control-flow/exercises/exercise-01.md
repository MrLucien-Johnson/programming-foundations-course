# Exercise 1: Grade Classifier

## 🎯 Your Task

Create a program that asks for a test score and classifies it as a letter grade (A, B, C, D, or F) using if/else statements.

## 📝 Learning Goals

By completing this exercise, you'll practice:
- Using if/else if/else statements
- Comparing values with comparison operators
- Making decisions based on numeric ranges
- Building a practical classification system

## 🚀 Steps

1. **Create a new project:**
   ```bash
   dotnet new console -o GradeClassifier
   cd GradeClassifier
   ```

2. **Open `Program.cs` in Cursor or VS Code**

3. **Write a program that:**
   - Asks for a test score (0-100)
   - Uses if/else if/else to classify the score:
     - 90-100: Grade A
     - 80-89: Grade B
     - 70-79: Grade C
     - 60-69: Grade D
     - Below 60: Grade F
   - Displays the grade

## 💡 Hints

- Use `>=` and `<=` to check ranges (e.g., `score >= 90 && score <= 100`)
- Check highest grades first (start with A, then B, etc.)
- You can use `else if` to check multiple conditions
- Make sure your ranges don't overlap!

## 📋 Example Input/Output

**Example run:**
```
Enter test score (0-100): 85
Grade: B
```

**Another example:**
```
Enter test score (0-100): 92
Grade: A
```

**Another example:**
```
Enter test score (0-100): 58
Grade: F
```

## ✅ Tips

- Start with the highest grade (A) and work your way down
- Use clear comparison operators (`>=`, `<=`)
- Test with boundary values (90, 80, 70, 60)
- Make your output clear and friendly

## 🎓 Real-World Connection

This is exactly how grading systems work in schools, universities, and online learning platforms. Many applications classify data into categories based on ranges - this is a common pattern!

## 🔍 Bonus Challenge

After completing the basic version, try adding:
- Validation to ensure score is between 0 and 100
- A message for each grade (e.g., "Excellent!" for A, "Needs improvement" for F)
- Support for plus/minus grades (A+, A-, B+, etc.)

## 🔍 Check Your Work

Once you've written your program:
1. Test it with different scores (try boundary values like 90, 80, 70, 60)
2. Make sure each range gives the correct grade
3. Verify that scores outside 0-100 are handled (bonus)
4. Check the solution in `exercise-01-solution.md` to see one possible approach

**Remember:** If your program correctly classifies scores into grades, you've succeeded! 🎉

