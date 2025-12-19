// Example 1: Simple Class
// This demonstrates creating a basic class with properties and creating objects

// Define the TaskItem class
class TaskItem
{
    public string Title { get; set; }
    public bool IsCompleted { get; set; }
}

// Main program
TaskItem task1 = new TaskItem();
task1.Title = "Buy groceries";
task1.IsCompleted = false;

TaskItem task2 = new TaskItem();
task2.Title = "Finish report";
task2.IsCompleted = true;

TaskItem task3 = new TaskItem();
task3.Title = "Call client";
task3.IsCompleted = false;

Console.WriteLine("=== Task List ===");
Console.WriteLine($"1. {task1.Title} - {(task1.IsCompleted ? "✓ Done" : "○ Todo")}");
Console.WriteLine($"2. {task2.Title} - {(task2.IsCompleted ? "✓ Done" : "○ Todo")}");
Console.WriteLine($"3. {task3.Title} - {(task3.IsCompleted ? "✓ Done" : "○ Todo")}");

