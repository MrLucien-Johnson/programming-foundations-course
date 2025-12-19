# Enhancement 1: Add Due Dates to Tasks

## 🎯 Your Task

Add due date functionality to your Task Tracker. Tasks should have a due date, and you should be able to see which tasks are due soon.

## 📝 Learning Goals

By completing this enhancement, you'll practice:
- Adding new properties to classes
- Working with dates (`DateTime`)
- Comparing dates
- Displaying date information

## 🚀 Steps

1. **Modify `TaskItem.cs`:**
   - Add a `DueDate` property of type `DateTime?` (nullable - optional)
   - Update the constructor to accept an optional due date
   - Update `DisplayInfo()` to show the due date if it exists

2. **Modify `TaskManager.cs`:**
   - Update `AddTask()` to ask for a due date (optional)
   - Add a method to show tasks due today or soon

3. **Modify `Program.cs`:**
   - Update the menu to include "Show tasks due soon"
   - Handle date input from the user

## 💡 Hints

- Use `DateTime?` for optional dates (nullable DateTime)
- Use `DateTime.Parse()` or `DateTime.TryParse()` to convert string input to dates
- Compare dates: `dueDate <= DateTime.Today` for overdue
- Format dates: `dueDate.ToString("yyyy-MM-dd")` or `dueDate.ToShortDateString()`

## 📋 Example Output

```
=== Your Tasks ===
1. Buy groceries - ○ Incomplete (Due: 2024-01-15)
2. Finish report - ○ Incomplete (Due: 2024-01-20)
3. Call client - ✓ Complete (Due: 2024-01-10)
```

## ✅ Tips

- Make due dates optional (not all tasks need due dates)
- Validate date input
- Show dates in a readable format
- Consider showing overdue tasks differently

## 🎓 Real-World Connection

Real task management systems always include due dates. This is a standard feature in professional applications.

## 🔍 Check Your Work

Once you've added due dates:
1. Verify you can create tasks with and without due dates
2. Check that dates display correctly
3. Test showing tasks due soon
4. Test with overdue tasks

**Remember:** This enhancement makes your project more professional and useful! 🎉

