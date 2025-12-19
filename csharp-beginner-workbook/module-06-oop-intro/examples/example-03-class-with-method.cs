// Example 3: Class with Method
// This demonstrates adding methods to classes so objects can perform actions

// Define the Customer class with methods
class Customer
{
    public string Name { get; set; }
    public string Email { get; set; }
    public bool IsVip { get; set; }
    
    // Method that displays customer information
    public void DisplayInfo()
    {
        string vipStatus = IsVip ? "VIP Member" : "Regular Customer";
        Console.WriteLine("=== Customer Profile ===");
        Console.WriteLine($"Name: {Name}");
        Console.WriteLine($"Email: {Email}");
        Console.WriteLine($"Status: {vipStatus}");
        Console.WriteLine();
    }
    
    // Method that upgrades customer to VIP
    public void UpgradeToVip()
    {
        IsVip = true;
        Console.WriteLine($"{Name} has been upgraded to VIP status!");
    }
}

// Main program
Customer customer1 = new Customer();
customer1.Name = "Sarah Johnson";
customer1.Email = "sarah@example.com";
customer1.IsVip = false;

Customer customer2 = new Customer();
customer2.Name = "Mike Chen";
customer2.Email = "mike@example.com";
customer2.IsVip = true;

// Use the methods
Console.WriteLine("=== Customer Database ===\n");
customer1.DisplayInfo();
customer2.DisplayInfo();

// Upgrade customer1
Console.WriteLine("=== Upgrading Customer ===");
customer1.UpgradeToVip();
customer1.DisplayInfo();

