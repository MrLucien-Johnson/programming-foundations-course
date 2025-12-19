# Debug Challenge: Find the Errors

## 🎯 Your Task

Look at this broken `CompleteTask` method from `TaskManager.cs` and find **all the errors**. Fix them so it works correctly!

## 🐛 The Broken Code

```csharp
public void CompleteTask(int taskNumber)
{
    int index = taskNumber;  // Should convert to 0-based index
    
    if (index > tasks.Count)  // Wrong condition
    {
        tasks[index].MarkComplete();
        Console.WriteLine($"Task completed!");
    }
    else
    {
        Console.WriteLine("Task already completed!");  // Wrong message
    }
}
```

## 📝 Steps

1. **Read the code carefully**

2. **Find all the mistakes:**
   - Error 1: _______________
   - Error 2: _______________
   - Error 3: _______________
   - Error 4: _______________

3. **Write the corrected version**

4. **Test it** - Make sure it works correctly

## 💡 Hints

- Think about index conversion (user sees 1, 2, 3... list uses 0, 1, 2...)
- Check the condition logic
- Check what happens in each branch
- Consider edge cases (already completed, invalid number)

## 🎓 Learning Goals

By completing this challenge, you'll practice:
- Understanding index conversion
- Finding logic errors
- Fixing conditional statements
- Debugging OOP code

## ✅ Success Criteria

Your fixed method should:
- ✅ Convert task number correctly (1-based to 0-based)
- ✅ Check if index is valid
- ✅ Check if task is already completed
- ✅ Mark task as complete correctly
- ✅ Show appropriate messages

## 🔍 Check Your Work

After you've found and fixed the errors, check `solutions/debug-challenge-solution.md` to see:
- What each error was
- Why it was wrong
- How to fix it
- Tips for avoiding these mistakes

**Remember:** Debugging is a crucial skill! Every programmer spends a lot of time fixing bugs. You're learning a valuable skill! 💪

