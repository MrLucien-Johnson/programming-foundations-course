# Exercise 2 Solution: VAT Calculator

## Solution Code

```csharp
Console.Write("Enter the base price: $");
string priceText = Console.ReadLine();
double price = double.Parse(priceText);

Console.Write("Enter the tax rate (e.g., 0.20 for 20%): ");
string taxText = Console.ReadLine();
double taxRate = double.Parse(taxText);

double tax = price * taxRate;
double total = price + tax;

Console.WriteLine($"Base Price: ${price:F2}");
Console.WriteLine($"Tax: ${tax:F2}");
Console.WriteLine($"Total: ${total:F2}");
```

## Explanation

This solution demonstrates:
1. **Getting decimal input** - Uses `double.Parse()` for prices and tax rates
2. **Calculations** - Multiplies price by tax rate to get tax amount
3. **Adding** - Adds tax to base price to get total
4. **Formatting** - Uses `F2` to format all currency values with 2 decimal places

## Key Points

- Tax calculation: `tax = price × taxRate`
- Total calculation: `total = price + tax`
- Currency formatting (`F2`) ensures consistent display
- Clear prompts help users understand the format

## Example Run

```
Enter the base price: $100.00
Enter the tax rate (e.g., 0.20 for 20%): 0.20
Base Price: $100.00
Tax: $20.00
Total: $120.00
```

## Variations

### Option 1: More Detailed Output
```csharp
Console.Write("Enter the base price: $");
double price = double.Parse(Console.ReadLine());

Console.Write("Enter the tax rate (e.g., 0.20 for 20%): ");
double taxRate = double.Parse(Console.ReadLine());

double tax = price * taxRate;
double total = price + tax;

Console.WriteLine("\n=== Price Breakdown ===");
Console.WriteLine($"Base Price:    ${price:F2}");
Console.WriteLine($"Tax Rate:       {taxRate:P0}");  // P0 formats as percentage
Console.WriteLine($"Tax Amount:     ${tax:F2}");
Console.WriteLine($"Total Price:   ${total:F2}");
```

### Option 2: Fixed Tax Rate
```csharp
const double TAX_RATE = 0.20;  // 20% tax

Console.Write("Enter the base price: $");
double price = double.Parse(Console.ReadLine());

double tax = price * TAX_RATE;
double total = price + tax;

Console.WriteLine($"Base Price: ${price:F2}");
Console.WriteLine($"Tax (20%): ${tax:F2}");
Console.WriteLine($"Total: ${total:F2}");
```

## Common Mistakes to Avoid

1. **Wrong calculation order:**
   ```csharp
   // WRONG - This calculates total incorrectly!
   double total = price * (1 + taxRate);  // This works, but less clear
   double tax = total - price;  // This is backwards!
   ```

2. **Forgetting to format currency:**
   ```csharp
   // Less professional output
   Console.WriteLine($"Total: ${total}");  // Might show $120.0 instead of $120.00
   ```

3. **Not explaining tax rate format:**
   ```csharp
   // Confusing for users
   Console.Write("Enter tax rate: ");  // User might enter 20 instead of 0.20
   ```

## Real-World Application

This is exactly how e-commerce sites calculate prices:
- Base price from product catalog
- Tax rate from location/jurisdiction
- Display breakdown to customer
- Store total for payment processing

## Try This

Modify the program to:
- Accept tax rate as a percentage (e.g., user enters 20 instead of 0.20)
- Calculate discount before tax
- Show savings amount
- Format everything as a receipt

