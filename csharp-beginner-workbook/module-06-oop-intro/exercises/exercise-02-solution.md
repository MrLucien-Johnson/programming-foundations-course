# Exercise 2 Solution: Create a Product Class with Constructor

## Solution Code

```csharp
// Define the Product class with constructor
class Product
{
    public double Price { get; set; }
    public string Description { get; set; }
    
    // Constructor - requires price and description
    public Product(double price, string description)
    {
        Price = price;
        Description = description;
    }
}

// Create products using the constructor
Product product1 = new Product(29.99, "Wireless Mouse");
Product product2 = new Product(45.00, "USB Keyboard");
Product product3 = new Product(35.50, "Monitor Stand");

// Display products
Console.WriteLine("=== Product Catalog ===");
Console.WriteLine($"Product 1:");
Console.WriteLine($"  Description: {product1.Description}");
Console.WriteLine($"  Price: ${product1.Price:F2}");
Console.WriteLine();

Console.WriteLine($"Product 2:");
Console.WriteLine($"  Description: {product2.Description}");
Console.WriteLine($"  Price: ${product2.Price:F2}");
Console.WriteLine();

Console.WriteLine($"Product 3:");
Console.WriteLine($"  Description: {product3.Description}");
Console.WriteLine($"  Price: ${product3.Price:F2}");
```

## Explanation

This solution demonstrates:
1. **Class with properties** - `Price` and `Description` define product characteristics
2. **Constructor** - Requires price and description when creating a Product
3. **Object creation with constructor** - `new Product(29.99, "Wireless Mouse")` passes values
4. **Initialization** - Constructor sets properties automatically
5. **Using objects** - Display information from each product object

## Key Points

- Constructor has same name as class
- Constructor parameters match property types
- Properties are set inside constructor
- Objects are created with required values
- Can't create Product without providing price and description

## Variations

### Option 1: With Name Property
```csharp
class Product
{
    public string Name { get; set; }
    public double Price { get; set; }
    public string Description { get; set; }
    
    public Product(string name, double price, string description)
    {
        Name = name;
        Price = price;
        Description = description;
    }
}

Product apple = new Product("Red Apple", 0.99, "Fresh red apples");
```

### Option 2: With Validation
```csharp
class Product
{
    public double Price { get; set; }
    public string Description { get; set; }
    
    public Product(double price, string description)
    {
        // Validate price is positive
        if (price < 0)
        {
            Price = 0;
            Console.WriteLine("Warning: Price cannot be negative!");
        }
        else
        {
            Price = price;
        }
        
        Description = description;
    }
}
```

### Option 3: With Display Method
```csharp
class Product
{
    public double Price { get; set; }
    public string Description { get; set; }
    
    public Product(double price, string description)
    {
        Price = price;
        Description = description;
    }
    
    public void DisplayInfo()
    {
        Console.WriteLine($"Product: {Description}");
        Console.WriteLine($"Price: ${Price:F2}");
    }
}

Product product1 = new Product(29.99, "Wireless Mouse");
product1.DisplayInfo();
```

### Option 4: Simplified Display
```csharp
class Product
{
    public double Price { get; set; }
    public string Description { get; set; }
    
    public Product(double price, string description)
    {
        Price = price;
        Description = description;
    }
}

Product product1 = new Product(29.99, "Wireless Mouse");
Product product2 = new Product(45.00, "USB Keyboard");
Product product3 = new Product(35.50, "Monitor Stand");

Console.WriteLine("=== Product Catalog ===");
Console.WriteLine($"{product1.Description}: ${product1.Price:F2}");
Console.WriteLine($"{product2.Description}: ${product2.Price:F2}");
Console.WriteLine($"{product3.Description}: ${product3.Price:F2}");
```

## Common Mistakes to Avoid

1. **Missing parameter types in constructor:**
   ```csharp
   // WRONG - Missing types
   public Product(price, description)  // Error!
   {
       Price = price;
       Description = description;
   }
   
   // CORRECT
   public Product(double price, string description)  // ✅
   {
       Price = price;
       Description = description;
   }
   ```

2. **Constructor name doesn't match class:**
   ```csharp
   // WRONG - Constructor name must match class name
   class Product
   {
       public Product(double price, string description) { }
       public CreateProduct(double price, string description) { }  // This is not a constructor!
   }
   ```

3. **Not using `new` when creating object:**
   ```csharp
   // WRONG - Missing new
   Product product1 = Product(29.99, "Mouse");  // Error!
   
   // CORRECT
   Product product1 = new Product(29.99, "Mouse");  // ✅
   ```

4. **Wrong parameter order:**
   ```csharp
   // WRONG - Parameters in wrong order
   Product product1 = new Product("Mouse", 29.99);  // Error if constructor expects (price, description)
   
   // CORRECT - Match constructor parameter order
   Product product1 = new Product(29.99, "Mouse");  // ✅
   ```

## Real-World Application

This pattern is used in:
- E-commerce systems
- Inventory management
- Product catalogs
- Point-of-sale systems
- Pricing systems

## Try This

Modify the program to:
- Add a `Name` property
- Add validation (price must be positive)
- Create a method to calculate price with tax
- Create a method to display product info
- Store products in a list

