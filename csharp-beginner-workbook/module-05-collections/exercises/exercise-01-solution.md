# Exercise 1 Solution: Shopping List

## Solution Code

```csharp
List<string> shoppingList = new List<string>();

// Add items to the shopping list
shoppingList.Add("Milk");
shoppingList.Add("Bread");
shoppingList.Add("Eggs");
shoppingList.Add("Butter");
shoppingList.Add("Cheese");

// Display the shopping list
Console.WriteLine("=== Shopping List ===");

int itemNumber = 1;
foreach (string item in shoppingList)
{
    Console.WriteLine($"{itemNumber}. {item}");
    itemNumber++;
}

Console.WriteLine($"\nTotal items: {shoppingList.Count}");
```

## Explanation

This solution demonstrates:
1. **Creating a list** - `List<string> shoppingList = new List<string>();`
2. **Adding items** - Using `Add()` method multiple times
3. **Displaying items** - Using `foreach` loop to go through each item
4. **Numbering items** - Starting from 1 (not 0) for user-friendly display
5. **Showing count** - Using `Count` property to display total

## Key Points

- `List<string>` creates a list that holds strings
- `Add()` method adds items to the end of the list
- `foreach` loop is perfect for displaying all items
- `Count` gives you the number of items
- Numbering starts at 1 for display (even though indexes start at 0)

## Variations

### Option 1: Using For Loop Instead
```csharp
List<string> shoppingList = new List<string>();
shoppingList.Add("Milk");
shoppingList.Add("Bread");
shoppingList.Add("Eggs");
shoppingList.Add("Butter");
shoppingList.Add("Cheese");

Console.WriteLine("=== Shopping List ===");

for (int i = 0; i < shoppingList.Count; i++)
{
    Console.WriteLine($"{i + 1}. {shoppingList[i]}");
}

Console.WriteLine($"\nTotal items: {shoppingList.Count}");
```

### Option 2: With User Input
```csharp
List<string> shoppingList = new List<string>();

Console.WriteLine("Add items to your shopping list (type 'done' when finished):");

string input = "";
while (input != "done")
{
    Console.Write("Enter item: ");
    input = Console.ReadLine();
    
    if (input != "done" && !string.IsNullOrEmpty(input))
    {
        shoppingList.Add(input);
    }
}

Console.WriteLine("\n=== Shopping List ===");
int itemNumber = 1;
foreach (string item in shoppingList)
{
    Console.WriteLine($"{itemNumber}. {item}");
    itemNumber++;
}

Console.WriteLine($"\nTotal items: {shoppingList.Count}");
```

### Option 3: With Removal
```csharp
List<string> shoppingList = new List<string>();
shoppingList.Add("Milk");
shoppingList.Add("Bread");
shoppingList.Add("Eggs");
shoppingList.Add("Butter");
shoppingList.Add("Cheese");

Console.WriteLine("=== Shopping List ===");
int itemNumber = 1;
foreach (string item in shoppingList)
{
    Console.WriteLine($"{itemNumber}. {item}");
    itemNumber++;
}

// Remove an item
Console.WriteLine("\nRemoving 'Bread'...");
shoppingList.Remove("Bread");

Console.WriteLine("\n=== Updated Shopping List ===");
itemNumber = 1;
foreach (string item in shoppingList)
{
    Console.WriteLine($"{itemNumber}. {item}");
    itemNumber++;
}

Console.WriteLine($"\nTotal items: {shoppingList.Count}");
```

## Common Mistakes to Avoid

1. **Forgetting to create the list:**
   ```csharp
   // WRONG - List doesn't exist
   shoppingList.Add("Milk");  // Error! shoppingList not defined
   ```

2. **Wrong loop condition:**
   ```csharp
   // WRONG - Will cause out-of-range error
   for (int i = 0; i <= shoppingList.Count; i++)  // Should be < not <=
   {
       Console.WriteLine(shoppingList[i]);
   }
   ```

3. **Using array syntax:**
   ```csharp
   // WRONG - Arrays use {}, lists use Add()
   List<string> shoppingList = { "Milk", "Bread" };  // Error!
   ```

4. **Not incrementing item number:**
   ```csharp
   // WRONG - All items will show as "1."
   int itemNumber = 1;
   foreach (string item in shoppingList)
   {
       Console.WriteLine($"{itemNumber}. {item}");  // Missing: itemNumber++;
   }
   ```

## Real-World Application

This pattern is used in:
- Shopping list applications
- Grocery apps
- To-do list managers
- Inventory tracking systems
- Checklist applications

## Try This

Modify the program to:
- Check if an item already exists before adding
- Remove items by index
- Sort items alphabetically
- Group items by category
- Save/load from a file (advanced)

