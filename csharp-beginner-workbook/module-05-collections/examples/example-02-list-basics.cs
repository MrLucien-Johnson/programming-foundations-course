// Example 2: List Basics
// This demonstrates creating a list, adding items, removing items, and counting

List<string> shoppingList = new List<string>();

Console.WriteLine("=== Shopping List Manager ===\n");

// Add items to the list
Console.WriteLine("Adding items...");
shoppingList.Add("Milk");
shoppingList.Add("Bread");
shoppingList.Add("Eggs");
shoppingList.Add("Butter");
shoppingList.Add("Cheese");

Console.WriteLine($"Items in list: {shoppingList.Count}");

// Display all items
Console.WriteLine("\n=== Current Shopping List ===");
for (int i = 0; i < shoppingList.Count; i++)
{
    Console.WriteLine($"{i + 1}. {shoppingList[i]}");
}

// Remove an item
Console.WriteLine("\nRemoving 'Bread'...");
shoppingList.Remove("Bread");

Console.WriteLine($"Items in list: {shoppingList.Count}");

// Display updated list
Console.WriteLine("\n=== Updated Shopping List ===");
foreach (string item in shoppingList)
{
    Console.WriteLine($"- {item}");
}

// Check if item exists
Console.WriteLine("\n=== Checking Items ===");
if (shoppingList.Contains("Milk"))
{
    Console.WriteLine("✓ Milk is on the list");
}
else
{
    Console.WriteLine("✗ Milk is not on the list");
}

if (shoppingList.Contains("Bread"))
{
    Console.WriteLine("✓ Bread is on the list");
}
else
{
    Console.WriteLine("✗ Bread is not on the list (was removed)");
}

