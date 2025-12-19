# Exercise 3: Task Reminder Loop

## 🎯 Your Task

Create a program that uses `foreach` to display a list of tasks and remind the user about each one.

## 📝 Learning Goals

By completing this exercise, you'll practice:
- Using foreach loops to iterate through collections
- Working with arrays (we'll learn more in Module 5)
- Processing each item in a list
- Building a task management feature

## 🚀 Steps

1. **Create a new project:**
   ```bash
   dotnet new console -o TaskReminder
   cd TaskReminder
   ```

2. **Open `Program.cs` in Cursor or VS Code**

3. **Write a program that:**
   - Creates an array of 5 tasks (strings)
   - Uses a foreach loop to go through each task
   - For each task, displays a reminder message
   - Shows a summary at the end

## 💡 Hints

- Create an array like this: `string[] tasks = { "Task 1", "Task 2", "Task 3", "Task 4", "Task 5" };`
- Use `foreach (string task in tasks)` to loop through
- Display each task with a friendly reminder message
- Count how many tasks there are (use `tasks.Length`)

## 📋 Example Input/Output

**Example run:**
```
=== Daily Task Reminders ===

Reminder: Don't forget to Buy groceries!
Reminder: Don't forget to Finish report!
Reminder: Don't forget to Call client!
Reminder: Don't forget to Review proposal!
Reminder: Don't forget to Send email!

You have 5 tasks to complete today. Good luck!
```

## ✅ Tips

- Make your task names realistic and work-related
- Use friendly, encouraging messages
- Show the total number of tasks
- Format your output nicely

## 🎓 Real-World Connection

This is how task management applications work! They:
- Store lists of tasks
- Process each task
- Display reminders
- Show summaries

Used in project management tools, to-do apps, and productivity software.

## 🔍 Bonus Challenge

After completing the basic version, try adding:
- Ask the user if each task is complete (yes/no)
- Count completed vs incomplete tasks
- Show a completion percentage
- Add priority levels (High, Medium, Low) to each task

## 🔍 Check Your Work

Once you've written your program:
1. Verify all tasks are displayed
2. Check that each task gets its own reminder
3. Make sure the summary is correct
4. Test with different numbers of tasks
5. Check the solution in `exercise-03-solution.md` to see one possible approach

**Remember:** If your program displays all tasks using a foreach loop, you've succeeded! 🎉

