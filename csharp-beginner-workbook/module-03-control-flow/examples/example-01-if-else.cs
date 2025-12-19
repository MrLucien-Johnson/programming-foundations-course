// Example 1: If/Else Decisions
// This demonstrates making decisions based on conditions

Console.Write("Enter your age: ");
string ageText = Console.ReadLine();
int age = int.Parse(ageText);

// Simple if statement
if (age >= 18)
{
    Console.WriteLine("You are an adult.");
}
else
{
    Console.WriteLine("You are a minor.");
}

// If/else if/else with multiple conditions
Console.Write("\nEnter purchase total: $");
string totalText = Console.ReadLine();
double total = double.Parse(totalText);

double discount = 0;
string discountMessage = "";

if (total > 1000)
{
    discount = total * 0.30;
    discountMessage = "30% discount applied!";
}
else if (total > 500)
{
    discount = total * 0.20;
    discountMessage = "20% discount applied!";
}
else if (total > 100)
{
    discount = total * 0.10;
    discountMessage = "10% discount applied!";
}
else
{
    discountMessage = "No discount available.";
}

double finalTotal = total - discount;

Console.WriteLine($"\nOriginal Price: ${total:F2}");
Console.WriteLine(discountMessage);
if (discount > 0)
{
    Console.WriteLine($"Discount Amount: ${discount:F2}");
}
Console.WriteLine($"Final Price: ${finalTotal:F2}");

