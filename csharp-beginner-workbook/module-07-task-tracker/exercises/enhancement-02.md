# Enhancement 2: Add Task Categories

## 🎯 Your Task

Add category functionality to tasks. Tasks can belong to categories like "Work", "Personal", "Shopping", etc. Add ability to filter tasks by category.

## 📝 Learning Goals

By completing this enhancement, you'll practice:
- Adding properties to classes
- Filtering collections
- Using if/else for filtering
- Organizing data by category

## 🚀 Steps

1. **Modify `TaskItem.cs`:**
   - Add a `Category` property (string)
   - Update constructor to accept category
   - Update `DisplayInfo()` to show category

2. **Modify `TaskManager.cs`:**
   - Update `AddTask()` to ask for category
   - Add a method `ListTasksByCategory(string category)` to filter tasks
   - Update `ListTasks()` to optionally show category

3. **Modify `Program.cs`:**
   - Add menu option "Filter by Category"
   - Let user choose a category to filter by

## 💡 Hints

- Use a simple string for category (or create an enum for fixed categories)
- Filter using `foreach` and `if` statements
- Consider showing available categories
- Make category optional or provide a default

## 📋 Example Output

```
=== Your Tasks ===
1. Buy groceries - ○ Incomplete [Shopping]
2. Finish report - ○ Incomplete [Work]
3. Call client - ✓ Complete [Work]

=== Filter by Category ===
Enter category (or press Enter for all): Work

=== Work Tasks ===
2. Finish report - ○ Incomplete [Work]
3. Call client - ✓ Complete [Work]
```

## ✅ Tips

- Provide common categories as suggestions
- Allow filtering by "All" to show everything
- Make category display optional in the main list
- Consider case-insensitive category matching

## 🎓 Real-World Connection

Categorization is essential in task management. It helps users organize and find tasks quickly. Used in all professional task management systems.

## 🔍 Check Your Work

Once you've added categories:
1. Verify you can assign categories to tasks
2. Check that filtering works correctly
3. Test with multiple categories
4. Test filtering with no matches

**Remember:** Categories make your task tracker more organized and professional! 🎉

