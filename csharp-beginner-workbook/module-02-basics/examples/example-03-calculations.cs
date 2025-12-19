// Example 3: Calculations and String Interpolation
// This demonstrates how to perform calculations and format output

Console.Write("Enter the price: $");
string priceText = Console.ReadLine();
double price = double.Parse(priceText);

Console.Write("Enter the quantity: ");
string quantityText = Console.ReadLine();
int quantity = int.Parse(quantityText);

double subtotal = price * quantity;
double tax = subtotal * 0.20;  // 20% tax
double total = subtotal + tax;

Console.WriteLine("\n=== Order Summary ===");
Console.WriteLine($"Price: ${price:F2}");
Console.WriteLine($"Quantity: {quantity}");
Console.WriteLine($"Subtotal: ${subtotal:F2}");
Console.WriteLine($"Tax (20%): ${tax:F2}");
Console.WriteLine($"Total: ${total:F2}");

