# Exercise 3 Solution: Task Printer

## Solution Code

```csharp
List<string> tasks = new List<string>();

// Add tasks to the list
tasks.Add("Buy groceries");
tasks.Add("Finish report");
tasks.Add("Call client");
tasks.Add("Review proposal");
tasks.Add("Send email");

// Display tasks with foreach loop
Console.WriteLine("=== Daily Tasks ===\n");

foreach (string task in tasks)
{
    Console.WriteLine($"Task: {task}");
}

Console.WriteLine($"\nYou have {tasks.Count} tasks to complete today. Good luck!");
```

## Explanation

This solution demonstrates:
1. **Creating a task list** - `List<string> tasks = new List<string>();`
2. **Adding multiple tasks** - Using `Add()` method
3. **Foreach loop** - Easy way to process each task
4. **Formatted output** - Clear, readable display
5. **Summary** - Shows total count with encouraging message

## Key Points

- `foreach` is perfect for this - no index to track
- Simple, clean code
- Easy to add more tasks
- Professional formatting

## Variations

### Option 1: With Reminders
```csharp
List<string> tasks = new List<string>();
tasks.Add("Buy groceries");
tasks.Add("Finish report");
tasks.Add("Call client");
tasks.Add("Review proposal");
tasks.Add("Send email");

Console.WriteLine("=== Task Reminders ===\n");

foreach (string task in tasks)
{
    Console.WriteLine($"Reminder: Don't forget to {task}!");
}

Console.WriteLine($"\nTotal reminders: {tasks.Count}");
```

### Option 2: With Numbers
```csharp
List<string> tasks = new List<string>();
tasks.Add("Buy groceries");
tasks.Add("Finish report");
tasks.Add("Call client");
tasks.Add("Review proposal");
tasks.Add("Send email");

Console.WriteLine("=== Daily Tasks ===\n");

int taskNumber = 1;
foreach (string task in tasks)
{
    Console.WriteLine($"{taskNumber}. {task}");
    taskNumber++;
}

Console.WriteLine($"\nYou have {tasks.Count} tasks to complete today. Good luck!");
```

### Option 3: With Status Icons
```csharp
List<string> tasks = new List<string>();
tasks.Add("Buy groceries");
tasks.Add("Finish report");
tasks.Add("Call client");
tasks.Add("Review proposal");
tasks.Add("Send email");

Console.WriteLine("=== Daily Tasks ===\n");

foreach (string task in tasks)
{
    Console.WriteLine($"○ {task}");
}

Console.WriteLine($"\nYou have {tasks.Count} tasks to complete today. Good luck!");
```

### Option 4: With Priority Levels
```csharp
List<string> highPriorityTasks = new List<string>();
highPriorityTasks.Add("Finish report");
highPriorityTasks.Add("Call client");

List<string> normalTasks = new List<string>();
normalTasks.Add("Buy groceries");
normalTasks.Add("Review proposal");
normalTasks.Add("Send email");

Console.WriteLine("=== Daily Tasks ===\n");

Console.WriteLine("HIGH PRIORITY:");
foreach (string task in highPriorityTasks)
{
    Console.WriteLine($"  ⚠ {task}");
}

Console.WriteLine("\nNormal Priority:");
foreach (string task in normalTasks)
{
    Console.WriteLine($"  • {task}");
}

int totalTasks = highPriorityTasks.Count + normalTasks.Count;
Console.WriteLine($"\nTotal tasks: {totalTasks}");
```

## Common Mistakes to Avoid

1. **Trying to modify list during foreach:**
   ```csharp
   // WRONG - Can't modify list while iterating
   foreach (string task in tasks)
   {
       if (task == "Finish report")
       {
           tasks.Remove(task);  // Error! Can't modify during iteration
       }
   }
   ```

2. **Not using foreach when you should:**
   ```csharp
   // More complex than needed
   for (int i = 0; i < tasks.Count; i++)
   {
       Console.WriteLine(tasks[i]);  // Foreach would be simpler
   }
   ```

3. **Forgetting the summary:**
   ```csharp
   // Missing the count/summary at the end
   foreach (string task in tasks)
   {
       Console.WriteLine($"Task: {task}");
   }
   // Should add: Console.WriteLine($"\nTotal: {tasks.Count}");
   ```

## Real-World Application

This pattern is used in:
- Task management applications
- To-do list apps
- Project management tools
- Reminder systems
- Daily planner applications

## Try This

Modify the program to:
- Add tasks from user input
- Mark tasks as complete (remove from list)
- Add priority levels
- Group tasks by category
- Add due dates (requires more advanced concepts)

