// Example 1: Basic Array
// This demonstrates creating an array, accessing items by index, and looping through

string[] tasks = { "Buy groceries", "Finish report", "Call client", "Review proposal", "Send email" };

Console.WriteLine("=== Task List ===");

// Access individual items by index
Console.WriteLine($"First task: {tasks[0]}");
Console.WriteLine($"Second task: {tasks[1]}");
Console.WriteLine($"Last task: {tasks[tasks.Length - 1]}");

Console.WriteLine("\n=== All Tasks ===");

// Loop through array using for loop
for (int i = 0; i < tasks.Length; i++)
{
    Console.WriteLine($"{i + 1}. {tasks[i]}");
}

Console.WriteLine($"\nTotal tasks: {tasks.Length}");

// Example with numbers
int[] numbers = { 10, 20, 30, 40, 50 };

Console.WriteLine("\n=== Numbers Array ===");
for (int i = 0; i < numbers.Length; i++)
{
    Console.WriteLine($"Position {i}: {numbers[i]}");
}

