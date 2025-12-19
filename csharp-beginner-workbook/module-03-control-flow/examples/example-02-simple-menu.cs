// Example 2: Simple Menu Loop
// This demonstrates a while loop that creates an interactive menu

string choice = "";

while (choice != "3")
{
    Console.WriteLine("\n=== Task Manager ===");
    Console.WriteLine("1. View Tasks");
    Console.WriteLine("2. Add Task");
    Console.WriteLine("3. Quit");
    Console.Write("Enter your choice (1-3): ");
    
    choice = Console.ReadLine();
    
    if (choice == "1")
    {
        Console.WriteLine("\nYour current tasks:");
        Console.WriteLine("- Buy groceries");
        Console.WriteLine("- Finish report");
        Console.WriteLine("- Call client");
    }
    else if (choice == "2")
    {
        Console.Write("Enter task name: ");
        string task = Console.ReadLine();
        Console.WriteLine($"✓ Added task: {task}");
    }
    else if (choice == "3")
    {
        Console.WriteLine("\nGoodbye! Have a productive day!");
    }
    else
    {
        Console.WriteLine("\nInvalid choice. Please enter 1, 2, or 3.");
    }
}

