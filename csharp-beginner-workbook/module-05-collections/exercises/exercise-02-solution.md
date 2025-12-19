# Exercise 2 Solution: Customer List with Count

## Solution Code

```csharp
List<string> customers = new List<string>();

// Add customers to the list
customers.Add("Sarah Johnson");
customers.Add("Mike Chen");
customers.Add("Emma Davis");
customers.Add("David Wilson");

// Display header
Console.WriteLine("=== Customer Database ===");

// Display all customers with numbers
int customerNumber = 1;
foreach (string customer in customers)
{
    Console.WriteLine($"{customerNumber}. {customer}");
    customerNumber++;
}

// Display total count
Console.WriteLine($"\nTotal customers: {customers.Count}");
```

## Explanation

This solution demonstrates:
1. **Creating a customer list** - `List<string> customers = new List<string>();`
2. **Adding customers** - Multiple `Add()` calls
3. **Displaying with header** - Professional formatting
4. **Numbering customers** - Starting from 1 for readability
5. **Showing total** - Using `Count` property

## Key Points

- Lists are perfect for customer databases (can grow over time)
- `foreach` makes it easy to process each customer
- Numbering from 1 makes it user-friendly
- `Count` gives accurate total

## Variations

### Option 1: Using For Loop
```csharp
List<string> customers = new List<string>();
customers.Add("Sarah Johnson");
customers.Add("Mike Chen");
customers.Add("Emma Davis");
customers.Add("David Wilson");

Console.WriteLine("=== Customer Database ===");

for (int i = 0; i < customers.Count; i++)
{
    Console.WriteLine($"{i + 1}. {customers[i]}");
}

Console.WriteLine($"\nTotal customers: {customers.Count}");
```

### Option 2: With Detailed Formatting
```csharp
List<string> customers = new List<string>();
customers.Add("Sarah Johnson");
customers.Add("Mike Chen");
customers.Add("Emma Davis");
customers.Add("David Wilson");

Console.WriteLine("========================================");
Console.WriteLine("      CUSTOMER DATABASE");
Console.WriteLine("========================================\n");

int customerNumber = 1;
foreach (string customer in customers)
{
    Console.WriteLine($"Customer #{customerNumber}: {customer}");
    customerNumber++;
}

Console.WriteLine($"\n----------------------------------------");
Console.WriteLine($"Total Customers: {customers.Count}");
Console.WriteLine("========================================");
```

### Option 3: With Customer IDs
```csharp
List<string> customers = new List<string>();
customers.Add("Sarah Johnson");
customers.Add("Mike Chen");
customers.Add("Emma Davis");
customers.Add("David Wilson");

Console.WriteLine("=== Customer Database ===");

for (int i = 0; i < customers.Count; i++)
{
    string customerId = $"CUST-{(i + 1):D4}";  // CUST-0001, CUST-0002, etc.
    Console.WriteLine($"{customerId}: {customers[i]}");
}

Console.WriteLine($"\nTotal customers: {customers.Count}");
```

### Option 4: With Search Functionality
```csharp
List<string> customers = new List<string>();
customers.Add("Sarah Johnson");
customers.Add("Mike Chen");
customers.Add("Emma Davis");
customers.Add("David Wilson");

Console.WriteLine("=== Customer Database ===");

int customerNumber = 1;
foreach (string customer in customers)
{
    Console.WriteLine($"{customerNumber}. {customer}");
    customerNumber++;
}

Console.WriteLine($"\nTotal customers: {customers.Count}");

// Search for a customer
Console.Write("\nEnter customer name to search: ");
string searchName = Console.ReadLine();

if (customers.Contains(searchName))
{
    int index = customers.IndexOf(searchName);
    Console.WriteLine($"✓ Found! Customer #{index + 1}: {searchName}");
}
else
{
    Console.WriteLine($"✗ Customer '{searchName}' not found.");
}
```

## Common Mistakes to Avoid

1. **Off-by-one error in loop:**
   ```csharp
   // WRONG - Will cause out-of-range error
   for (int i = 0; i <= customers.Count; i++)  // Should be <
   {
       Console.WriteLine(customers[i]);
   }
   ```

2. **Not resetting counter:**
   ```csharp
   // WRONG - If you use the counter multiple times without resetting
   int customerNumber = 1;
   foreach (string customer in customers) { ... }
   // Later, if you loop again, customerNumber continues from where it left off
   ```

3. **Using wrong property:**
   ```csharp
   // WRONG - Arrays use Length, lists use Count
   Console.WriteLine(customers.Length);  // Error! Lists don't have Length
   ```

4. **Forgetting to increment:**
   ```csharp
   // WRONG - All customers show as #1
   int customerNumber = 1;
   foreach (string customer in customers)
   {
       Console.WriteLine($"{customerNumber}. {customer}");
       // Missing: customerNumber++;
   }
   ```

## Real-World Application

This pattern is used in:
- Customer relationship management (CRM) systems
- Contact management applications
- Client databases
- Membership systems
- Employee directories

## Try This

Modify the program to:
- Add customers from user input
- Search for specific customers
- Remove customers
- Sort customers alphabetically
- Add customer details (email, phone) - requires classes (Module 6!)

