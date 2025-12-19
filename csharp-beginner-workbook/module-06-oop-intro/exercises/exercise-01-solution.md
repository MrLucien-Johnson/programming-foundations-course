# Exercise 1 Solution: Create a TaskItem Class

## Solution Code

```csharp
// Define the TaskItem class
class TaskItem
{
    public string Title { get; set; }
    public bool IsCompleted { get; set; }
}

// Create TaskItem objects
TaskItem task1 = new TaskItem();
task1.Title = "Buy groceries";
task1.IsCompleted = false;

TaskItem task2 = new TaskItem();
task2.Title = "Finish report";
task2.IsCompleted = true;

TaskItem task3 = new TaskItem();
task3.Title = "Call client";
task3.IsCompleted = false;

// Display tasks
Console.WriteLine("=== Task List ===");
Console.WriteLine($"1. {task1.Title} - {(task1.IsCompleted ? "✓ Complete" : "○ Incomplete")}");
Console.WriteLine($"2. {task2.Title} - {(task2.IsCompleted ? "✓ Complete" : "○ Incomplete")}");
Console.WriteLine($"3. {task3.Title} - {(task3.IsCompleted ? "✓ Complete" : "○ Incomplete")}");
```

## Explanation

This solution demonstrates:
1. **Class definition** - `class TaskItem { ... }` defines the blueprint
2. **Properties** - `Title` and `IsCompleted` are characteristics of tasks
3. **Object creation** - `new TaskItem()` creates instances
4. **Setting properties** - Each object gets its own values
5. **Using objects** - Display information from each object

## Key Points

- One class (`TaskItem`) can create many objects (`task1`, `task2`, `task3`)
- Each object has its own `Title` and `IsCompleted` values
- Objects are independent - changing `task1` doesn't affect `task2`
- Properties use `{ get; set; }` to allow reading and writing

## Variations

### Option 1: With a Display Method
```csharp
class TaskItem
{
    public string Title { get; set; }
    public bool IsCompleted { get; set; }
    
    public void DisplayInfo()
    {
        string status = IsCompleted ? "✓ Complete" : "○ Incomplete";
        Console.WriteLine($"{Title} - {status}");
    }
}

TaskItem task1 = new TaskItem();
task1.Title = "Buy groceries";
task1.IsCompleted = false;

task1.DisplayInfo();  // Uses the method
```

### Option 2: With More Properties
```csharp
class TaskItem
{
    public string Title { get; set; }
    public string Description { get; set; }
    public bool IsCompleted { get; set; }
    public int Priority { get; set; }  // 1 = Low, 2 = Medium, 3 = High
}

TaskItem task1 = new TaskItem();
task1.Title = "Buy groceries";
task1.Description = "Get milk, bread, and eggs";
task1.IsCompleted = false;
task1.Priority = 2;
```

### Option 3: Using a List
```csharp
class TaskItem
{
    public string Title { get; set; }
    public bool IsCompleted { get; set; }
}

List<TaskItem> tasks = new List<TaskItem>();

TaskItem task1 = new TaskItem();
task1.Title = "Buy groceries";
task1.IsCompleted = false;
tasks.Add(task1);

TaskItem task2 = new TaskItem();
task2.Title = "Finish report";
task2.IsCompleted = true;
tasks.Add(task2);

foreach (TaskItem task in tasks)
{
    Console.WriteLine($"{task.Title} - {(task.IsCompleted ? "Done" : "Todo")}");
}
```

## Common Mistakes to Avoid

1. **Forgetting `new` keyword:**
   ```csharp
   // WRONG - Missing new
   TaskItem task1 = TaskItem();  // Error!
   
   // CORRECT
   TaskItem task1 = new TaskItem();  // ✅
   ```

2. **Trying to set properties before creating object:**
   ```csharp
   // WRONG - Object doesn't exist yet
   task1.Title = "Buy groceries";  // Error! task1 not created
   TaskItem task1 = new TaskItem();
   
   // CORRECT - Create first, then set
   TaskItem task1 = new TaskItem();
   task1.Title = "Buy groceries";  // ✅
   ```

3. **Wrong property syntax:**
   ```csharp
   // WRONG - Missing { get; set; }
   public string Title;  // This is a field, not a property
   
   // CORRECT
   public string Title { get; set; }  // ✅ Property
   ```

4. **Using class name instead of object name:**
   ```csharp
   // WRONG - Can't set properties on the class
   TaskItem.Title = "Buy groceries";  // Error!
   
   // CORRECT - Set on the object
   TaskItem task1 = new TaskItem();
   task1.Title = "Buy groceries";  // ✅
   ```

## Real-World Application

This pattern is used in:
- Task management applications
- To-do list apps
- Project management tools
- Workflow systems
- Issue tracking systems

## Try This

Modify the program to:
- Add a `Description` property
- Add a `DueDate` property
- Create a method `MarkComplete()` that sets `IsCompleted = true`
- Create a method `DisplayInfo()` that shows all task details
- Store tasks in a list and loop through them

