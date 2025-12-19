// Example 3: Looping Through a List
// This demonstrates using foreach to process each item in a collection

// Array of tasks
string[] tasks = { "Buy groceries", "Finish report", "Call client", "Review proposal", "Send email" };

Console.WriteLine("=== Task Reminder ===");
Console.WriteLine($"You have {tasks.Length} tasks to complete:\n");

// Foreach loop - goes through each task
foreach (string task in tasks)
{
    Console.WriteLine($"Reminder: Don't forget to {task}!");
}

Console.WriteLine("\n=== Processing Tasks ===");

// For loop - process each task with a number
for (int i = 0; i < tasks.Length; i++)
{
    int taskNumber = i + 1;
    Console.WriteLine($"Task {taskNumber}: {tasks[i]}");
}

Console.WriteLine("\n=== Checking Completion ===");

// While loop example - keep asking until all tasks are done
int completedTasks = 0;
int totalTasks = tasks.Length;

while (completedTasks < totalTasks)
{
    Console.WriteLine($"\nCompleted: {completedTasks} / {totalTasks}");
    Console.Write("Mark a task as complete? (yes/no): ");
    string answer = Console.ReadLine();
    
    if (answer.ToLower() == "yes")
    {
        completedTasks++;
        Console.WriteLine($"Great! {completedTasks} task(s) completed.");
    }
    else
    {
        Console.WriteLine("Keep working!");
    }
}

Console.WriteLine("\n🎉 All tasks completed! Well done!");

