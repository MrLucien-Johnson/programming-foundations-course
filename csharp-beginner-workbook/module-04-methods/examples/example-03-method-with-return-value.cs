// Example 3: Method with Return Value
// This demonstrates methods that calculate and return results

static bool IsValidAge(int age)
{
    if (age >= 0 && age <= 120)
    {
        return true;
    }
    else
    {
        return false;
    }
}

static bool IsValidPrice(double price)
{
    return price > 0;  // Returns true if price is positive
}

static int GetMax(int a, int b)
{
    if (a > b)
    {
        return a;
    }
    else
    {
        return b;
    }
}

// Main program
Console.WriteLine("=== Validation Examples ===\n");

// Age validation
Console.Write("Enter your age: ");
int age = int.Parse(Console.ReadLine());

if (IsValidAge(age))
{
    Console.WriteLine("✓ Valid age entered!");
}
else
{
    Console.WriteLine("✗ Invalid age! Must be between 0 and 120.");
}

// Price validation
Console.Write("\nEnter a price: $");
double price = double.Parse(Console.ReadLine());

if (IsValidPrice(price))
{
    Console.WriteLine("✓ Valid price!");
}
else
{
    Console.WriteLine("✗ Invalid price! Must be greater than 0.");
}

// Finding maximum
Console.WriteLine("\n=== Finding Maximum ===");
int num1 = 25;
int num2 = 42;
int maximum = GetMax(num1, num2);
Console.WriteLine($"Maximum of {num1} and {num2} is {maximum}");

