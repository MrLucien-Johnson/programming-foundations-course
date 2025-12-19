# Exercise 3: Task Printer

## 🎯 Your Task

Create a program that uses a `foreach` loop to display a list of tasks in a formatted way.

## 📝 Learning Goals

By completing this exercise, you'll practice:
- Creating a list of tasks
- Using `foreach` loops to process each item
- Formatting output nicely
- Building a task display system

## 🚀 Steps

1. **Create a new project:**
   ```bash
   dotnet new console -o TaskPrinter
   cd TaskPrinter
   ```

2. **Open `Program.cs` in Cursor or VS Code**

3. **Write a program that:**
   - Creates a `List<string>` with at least 5 tasks
   - Uses a `foreach` loop to go through each task
   - Displays each task with a formatted message (e.g., "Task: Buy groceries" or "Reminder: Finish report")
   - Shows a summary at the end

## 💡 Hints

- Create the list and add tasks
- Use `foreach (string task in tasks)` to loop
- Format each task nicely (add prefixes, formatting)
- Display a summary after the loop

## 📋 Example Output

```
=== Daily Tasks ===

Task: Buy groceries
Task: Finish report
Task: Call client
Task: Review proposal
Task: Send email

You have 5 tasks to complete today. Good luck!
```

**Or with reminders:**

```
=== Task Reminders ===

Reminder: Don't forget to Buy groceries!
Reminder: Don't forget to Finish report!
Reminder: Don't forget to Call client!
Reminder: Don't forget to Review proposal!
Reminder: Don't forget to Send email!

Total reminders: 5
```

## ✅ Tips

- Use realistic, work-related tasks
- Make the formatting consistent
- Add a header and summary
- Use `foreach` - it's perfect for this!

## 🎓 Real-World Connection

This is exactly how task management systems display tasks! They:
- Store tasks in lists
- Loop through each task
- Display formatted reminders
- Show summaries and counts

Used in:
- Task management applications
- To-do list apps
- Project management tools
- Reminder systems

## 🔍 Bonus Challenge

After completing the basic version, try:
- Adding priority levels to tasks
- Grouping tasks by category
- Marking tasks as complete
- Filtering tasks (show only high priority)
- Adding due dates to tasks

## 🔍 Check Your Work

Once you've written your program:
1. Verify all tasks are displayed
2. Check that the formatting is consistent
3. Make sure the summary is correct
4. Test with different numbers of tasks
5. Check the solution in `exercise-03-solution.md` to see one possible approach

**Remember:** If your program uses `foreach` to display tasks in a formatted way, you've succeeded! 🎉

