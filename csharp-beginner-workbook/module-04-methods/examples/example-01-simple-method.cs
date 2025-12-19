// Example 1: Simple Method
// This demonstrates a basic method with no parameters that displays a formatted header

static void DisplayHeader()
{
    Console.WriteLine("========================================");
    Console.WriteLine("    COMPANY REPORT SYSTEM");
    Console.WriteLine("========================================");
    Console.WriteLine();
}

static void DisplayFooter()
{
    Console.WriteLine();
    Console.WriteLine("========================================");
    Console.WriteLine("    End of Report");
    Console.WriteLine("========================================");
}

// Main program
DisplayHeader();

Console.WriteLine("Report Content:");
Console.WriteLine("- Sales: $50,000");
Console.WriteLine("- Expenses: $30,000");
Console.WriteLine("- Profit: $20,000");

DisplayFooter();

// Can call the same method multiple times
DisplayHeader();
Console.WriteLine("Another report section...");
DisplayFooter();

