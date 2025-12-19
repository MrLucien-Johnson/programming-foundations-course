# Enhancement 3: Delete Tasks

## 🎯 Your Task

Add the ability to delete tasks from the task list. Users should be able to remove tasks they no longer need.

## 📝 Learning Goals

By completing this enhancement, you'll practice:
- Removing items from collections
- Input validation for deletion
- Confirming actions before deleting
- Handling edge cases (empty list, invalid index)

## 🚀 Steps

1. **Modify `TaskManager.cs`:**
   - Add a `DeleteTask(int taskNumber)` method
   - Validate the task number
   - Remove the task from the list
   - Show confirmation message

2. **Modify `Program.cs`:**
   - Add menu option "Delete Task"
   - Show task list before deletion
   - Ask for confirmation before deleting
   - Handle the deletion

## 💡 Hints

- Use `tasks.RemoveAt(index)` to remove by index
- Convert user's task number (1-based) to index (0-based)
- Validate index before removing
- Consider asking "Are you sure?" before deleting

## 📋 Example Output

```
=== Your Tasks ===
1. Buy groceries - ○ Incomplete
2. Finish report - ○ Incomplete
3. Call client - ✓ Complete

Enter task number to delete: 2
Are you sure you want to delete 'Finish report'? (yes/no): yes
✓ Task 'Finish report' deleted successfully!
```

## ✅ Tips

- Always show the task list before asking which to delete
- Validate the task number exists
- Consider confirmation to prevent accidental deletion
- Show a message after successful deletion

## 🎓 Real-World Connection

Deletion is a standard feature in all data management applications. Users need to be able to remove items they no longer need.

## 🔍 Check Your Work

Once you've added deletion:
1. Verify you can delete tasks correctly
2. Check that invalid task numbers are handled
3. Test deleting from different positions
4. Test with empty list
5. Verify task numbers update correctly after deletion

**Remember:** Deletion makes your task tracker more complete and useful! 🎉

