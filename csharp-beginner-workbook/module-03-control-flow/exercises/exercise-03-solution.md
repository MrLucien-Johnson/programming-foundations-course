# Exercise 3 Solution: Task Reminder Loop

## Solution Code

```csharp
string[] tasks = { 
    "Buy groceries", 
    "Finish report", 
    "Call client", 
    "Review proposal", 
    "Send email" 
};

Console.WriteLine("=== Daily Task Reminders ===\n");

foreach (string task in tasks)
{
    Console.WriteLine($"Reminder: Don't forget to {task}!");
}

Console.WriteLine($"\nYou have {tasks.Length} tasks to complete today. Good luck!");
```

## Explanation

This solution demonstrates:
1. **Array creation** - Creates an array of 5 task strings
2. **Foreach loop** - Iterates through each task in the array
3. **Processing each item** - Displays a reminder for each task
4. **Summary** - Shows total number of tasks using `tasks.Length`

## Key Points

- Arrays hold multiple values of the same type
- `foreach` automatically goes through each item
- `tasks.Length` gives you the number of items
- Each iteration processes one task

## Variations

### Option 1: With Task Numbers
```csharp
string[] tasks = { 
    "Buy groceries", 
    "Finish report", 
    "Call client", 
    "Review proposal", 
    "Send email" 
};

Console.WriteLine("=== Daily Task Reminders ===\n");

int taskNumber = 1;
foreach (string task in tasks)
{
    Console.WriteLine($"Task {taskNumber}: {task}");
    taskNumber++;
}

Console.WriteLine($"\nYou have {tasks.Length} tasks to complete today. Good luck!");
```

### Option 2: Using For Loop Instead
```csharp
string[] tasks = { 
    "Buy groceries", 
    "Finish report", 
    "Call client", 
    "Review proposal", 
    "Send email" 
};

Console.WriteLine("=== Daily Task Reminders ===\n");

for (int i = 0; i < tasks.Length; i++)
{
    Console.WriteLine($"Reminder: Don't forget to {tasks[i]}!");
}

Console.WriteLine($"\nYou have {tasks.Length} tasks to complete today. Good luck!");
```

### Option 3: With Completion Tracking
```csharp
string[] tasks = { 
    "Buy groceries", 
    "Finish report", 
    "Call client", 
    "Review proposal", 
    "Send email" 
};

int completedCount = 0;

Console.WriteLine("=== Task Reminder and Tracker ===\n");

foreach (string task in tasks)
{
    Console.WriteLine($"Reminder: Don't forget to {task}!");
    Console.Write("Is this task complete? (yes/no): ");
    string answer = Console.ReadLine();
    
    if (answer.ToLower() == "yes")
    {
        completedCount++;
        Console.WriteLine("✓ Marked as complete!\n");
    }
    else
    {
        Console.WriteLine("Keep working on it!\n");
    }
}

Console.WriteLine($"\n=== Summary ===");
Console.WriteLine($"Completed: {completedCount} / {tasks.Length}");
Console.WriteLine($"Remaining: {tasks.Length - completedCount}");
```

### Option 4: With Priorities
```csharp
string[] tasks = { 
    "Buy groceries", 
    "Finish report", 
    "Call client", 
    "Review proposal", 
    "Send email" 
};

string[] priorities = { "High", "High", "Medium", "Low", "Medium" };

Console.WriteLine("=== Task Reminder with Priorities ===\n");

for (int i = 0; i < tasks.Length; i++)
{
    Console.WriteLine($"[{priorities[i]}] Reminder: Don't forget to {tasks[i]}!");
}

Console.WriteLine($"\nYou have {tasks.Length} tasks to complete today. Good luck!");
```

## Common Mistakes to Avoid

1. **Wrong loop syntax:**
   ```csharp
   // WRONG - Missing 'in' keyword
   foreach (string task tasks)  // Error!
   {
       // ...
   }
   ```

2. **Trying to modify array in foreach:**
   ```csharp
   // WRONG - Can't modify array while iterating
   foreach (string task in tasks)
   {
       task = "New task";  // This won't work!
   }
   ```

3. **Using wrong variable name:**
   ```csharp
   // WRONG - Variable name doesn't match
   foreach (string task in tasks)
   {
       Console.WriteLine(item);  // Should be 'task', not 'item'
   }
   ```

## Real-World Application

This pattern is used in:
- Task management applications
- Project management tools
- To-do list apps
- Notification systems
- Batch processing systems
- Report generators

## Try This

Modify the program to:
- Add completion status to each task
- Show tasks grouped by priority
- Add due dates to tasks
- Filter tasks (show only high priority)
- Sort tasks alphabetically
- Add new tasks dynamically (advanced)

