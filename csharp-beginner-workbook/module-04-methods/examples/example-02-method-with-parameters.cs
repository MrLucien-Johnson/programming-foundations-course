// Example 2: Method with Parameters
// This demonstrates passing information to a method and using it in calculations

static double CalculateTotalWithTax(double price, double taxRate)
{
    double tax = price * taxRate;
    double total = price + tax;
    return total;
}

static void DisplayPriceBreakdown(double price, double taxRate)
{
    double tax = price * taxRate;
    double total = price + tax;
    
    Console.WriteLine($"Base Price:    ${price:F2}");
    Console.WriteLine($"Tax Rate:      {taxRate:P0}");
    Console.WriteLine($"Tax Amount:    ${tax:F2}");
    Console.WriteLine($"Total Price:   ${total:F2}");
}

// Main program
Console.WriteLine("=== Order Calculator ===\n");

Console.Write("Enter item price: $");
double price = double.Parse(Console.ReadLine());

Console.Write("Enter tax rate (e.g., 0.20 for 20%): ");
double taxRate = double.Parse(Console.ReadLine());

Console.WriteLine("\n--- Price Breakdown ---");
DisplayPriceBreakdown(price, taxRate);

Console.WriteLine("\n--- Using Calculation Method ---");
double finalPrice = CalculateTotalWithTax(price, taxRate);
Console.WriteLine($"Final Price (from method): ${finalPrice:F2}");

// Use the method with different values
Console.WriteLine("\n--- Another Order ---");
double anotherPrice = 75.50;
double anotherTaxRate = 0.15;
DisplayPriceBreakdown(anotherPrice, anotherTaxRate);

