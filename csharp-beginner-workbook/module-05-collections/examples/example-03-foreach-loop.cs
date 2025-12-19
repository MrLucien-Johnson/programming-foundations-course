// Example 3: Foreach Loop
// This demonstrates using foreach to loop through collections easily

List<string> customers = new List<string>();
customers.Add("Sarah Johnson");
customers.Add("Mike Chen");
customers.Add("Emma Davis");
customers.Add("David Wilson");
customers.Add("Lisa Anderson");

Console.WriteLine("=== Customer List ===");

// Foreach loop - easier than for loop!
int customerNumber = 1;
foreach (string customer in customers)
{
    Console.WriteLine($"{customerNumber}. {customer}");
    customerNumber++;
}

Console.WriteLine($"\nTotal customers: {customers.Count}");

// Example with tasks
List<string> tasks = new List<string>();
tasks.Add("Buy groceries");
tasks.Add("Finish report");
tasks.Add("Call client");
tasks.Add("Review proposal");

Console.WriteLine("\n=== Task Reminders ===");
foreach (string task in tasks)
{
    Console.WriteLine($"Reminder: Don't forget to {task}!");
}

// Example with array (foreach works with arrays too!)
string[] products = { "Widget A", "Widget B", "Widget C" };

Console.WriteLine("\n=== Product Catalog ===");
int productIndex = 1;
foreach (string product in products)
{
    Console.WriteLine($"Product {productIndex}: {product}");
    productIndex++;
}

