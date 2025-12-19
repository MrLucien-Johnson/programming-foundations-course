# Exercise 1: Create a TaskItem Class

## 🎯 Your Task

Create a `TaskItem` class with `Title` and `IsCompleted` properties. Create multiple TaskItem objects and display them.

## 📝 Learning Goals

By completing this exercise, you'll practice:
- Defining a class
- Creating properties in a class
- Creating objects from a class
- Setting property values
- Using objects in your program

## 🚀 Steps

1. **Create a new project:**
   ```bash
   dotnet new console -o TaskItemClass
   cd TaskItemClass
   ```

2. **Open `Program.cs` in Cursor or VS Code**

3. **Write a program that:**
   - Defines a `TaskItem` class with:
     - `Title` property (string)
     - `IsCompleted` property (bool)
   - Creates at least 3 TaskItem objects
   - Sets the Title and IsCompleted for each
   - Displays all tasks in a formatted way

## 💡 Hints

- Start by defining the class: `class TaskItem { ... }`
- Add properties: `public string Title { get; set; }`
- Create objects: `TaskItem task1 = new TaskItem();`
- Set properties: `task1.Title = "Your task title";`
- Display using the properties

## 📋 Example Output

```
=== Task List ===
1. Buy groceries - ○ Incomplete
2. Finish report - ✓ Complete
3. Call client - ○ Incomplete
```

## ✅ Tips

- Choose clear, descriptive property names
- Create multiple tasks to see how one class creates many objects
- Format your output nicely
- Use conditional expressions to show "Complete" or "Incomplete"

## 🎓 Real-World Connection

This is exactly how task management systems work! They have a Task class, and create many Task objects (one for each task). Used in:
- Task management applications
- To-do list apps
- Project management tools
- Workflow systems

## 🔍 Bonus Challenge

After completing the basic version, try:
- Adding a `Description` property
- Adding a `DueDate` property
- Creating a method to display task info
- Creating a method to mark a task as complete

## 🔍 Check Your Work

Once you've written your program:
1. Verify the class is defined correctly
2. Check that you can create multiple TaskItem objects
3. Make sure each object has its own Title and IsCompleted values
4. Verify the display shows all tasks correctly
5. Check the solution in `exercise-01-solution.md` to see one possible approach

**Remember:** If your program defines a class, creates objects from it, and displays them, you've succeeded! 🎉

