// Example 2: Constructor
// This demonstrates creating a class with a constructor that initializes objects

// Define the Product class with constructor
class Product
{
    public string Name { get; set; }
    public double Price { get; set; }
    
    // Constructor - requires name and price when creating a Product
    public Product(string name, double price)
    {
        Name = name;
        Price = price;
    }
}

// Main program - create products using the constructor
Product apple = new Product("Red Apple", 0.99);
Product bread = new Product("Whole Wheat Bread", 2.50);
Product milk = new Product("Whole Milk", 3.99);

Console.WriteLine("=== Product Catalog ===");
Console.WriteLine($"{apple.Name}: ${apple.Price:F2}");
Console.WriteLine($"{bread.Name}: ${bread.Price:F2}");
Console.WriteLine($"{milk.Name}: ${milk.Price:F2}");

Console.WriteLine("\n=== Product Details ===");
Console.WriteLine($"Product 1 - Name: {apple.Name}, Price: ${apple.Price:F2}");
Console.WriteLine($"Product 2 - Name: {bread.Name}, Price: ${bread.Price:F2}");
Console.WriteLine($"Product 3 - Name: {milk.Name}, Price: ${milk.Price:F2}");

