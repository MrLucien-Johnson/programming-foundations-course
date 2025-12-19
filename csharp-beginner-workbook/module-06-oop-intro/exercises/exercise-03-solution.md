# Exercise 3 Solution: Create a Customer Class with Method

## Solution Code

```csharp
// Define the Customer class with method
class Customer
{
    public string Name { get; set; }
    public string Email { get; set; }
    public string Phone { get; set; }
    
    // Method that displays customer profile
    public void DisplayProfile()
    {
        Console.WriteLine("=== Customer Profile ===");
        Console.WriteLine($"Name: {Name}");
        Console.WriteLine($"Email: {Email}");
        Console.WriteLine($"Phone: {Phone}");
        Console.WriteLine();
    }
}

// Create customer objects
Customer customer1 = new Customer();
customer1.Name = "Sarah Johnson";
customer1.Email = "sarah@example.com";
customer1.Phone = "555-0123";

Customer customer2 = new Customer();
customer2.Name = "Mike Chen";
customer2.Email = "mike@example.com";
customer2.Phone = "555-0456";

// Display customer profiles using the method
Console.WriteLine("=== Customer Database ===\n");
customer1.DisplayProfile();
customer2.DisplayProfile();
```

## Explanation

This solution demonstrates:
1. **Class with properties** - `Name`, `Email`, `Phone` store customer data
2. **Method in class** - `DisplayProfile()` belongs to the Customer class
3. **Method uses properties** - Inside method, can access `Name`, `Email`, `Phone`
4. **Calling methods** - `customer1.DisplayProfile()` calls the method on that object
5. **Each object has its own method** - Each customer can display their own profile

## Key Points

- Methods belong to the class and can use the class's properties
- Each object can call the method independently
- Method uses `this` object's properties (implicitly)
- Methods organize behavior with data

## Variations

### Option 1: With Multiple Methods
```csharp
class Customer
{
    public string Name { get; set; }
    public string Email { get; set; }
    public string Phone { get; set; }
    
    public void DisplayProfile()
    {
        Console.WriteLine($"Name: {Name}");
        Console.WriteLine($"Email: {Email}");
        Console.WriteLine($"Phone: {Phone}");
    }
    
    public void UpdatePhone(string newPhone)
    {
        Phone = newPhone;
        Console.WriteLine($"Phone number updated to {newPhone}");
    }
    
    public void SendWelcomeEmail()
    {
        Console.WriteLine($"Sending welcome email to {Email}...");
        Console.WriteLine($"Hello {Name}, welcome to our service!");
    }
}

Customer customer = new Customer();
customer.Name = "Sarah Johnson";
customer.Email = "sarah@example.com";
customer.Phone = "555-0123";

customer.DisplayProfile();
customer.SendWelcomeEmail();
customer.UpdatePhone("555-9999");
customer.DisplayProfile();
```

### Option 2: With Formatted Output
```csharp
class Customer
{
    public string Name { get; set; }
    public string Email { get; set; }
    public string Phone { get; set; }
    
    public void DisplayProfile()
    {
        Console.WriteLine("========================================");
        Console.WriteLine("         CUSTOMER PROFILE");
        Console.WriteLine("========================================");
        Console.WriteLine($"Name:    {Name}");
        Console.WriteLine($"Email:   {Email}");
        Console.WriteLine($"Phone:   {Phone}");
        Console.WriteLine("========================================");
        Console.WriteLine();
    }
}
```

### Option 3: Method That Returns String
```csharp
class Customer
{
    public string Name { get; set; }
    public string Email { get; set; }
    public string Phone { get; set; }
    
    public string GetProfileInfo()
    {
        return $"Customer: {Name}\nEmail: {Email}\nPhone: {Phone}";
    }
    
    public void DisplayProfile()
    {
        Console.WriteLine(GetProfileInfo());
    }
}

Customer customer = new Customer();
customer.Name = "Sarah Johnson";
customer.Email = "sarah@example.com";
customer.Phone = "555-0123";

string info = customer.GetProfileInfo();
Console.WriteLine(info);
```

### Option 4: With Constructor
```csharp
class Customer
{
    public string Name { get; set; }
    public string Email { get; set; }
    public string Phone { get; set; }
    
    public Customer(string name, string email, string phone)
    {
        Name = name;
        Email = email;
        Phone = phone;
    }
    
    public void DisplayProfile()
    {
        Console.WriteLine("=== Customer Profile ===");
        Console.WriteLine($"Name: {Name}");
        Console.WriteLine($"Email: {Email}");
        Console.WriteLine($"Phone: {Phone}");
        Console.WriteLine();
    }
}

Customer customer1 = new Customer("Sarah Johnson", "sarah@example.com", "555-0123");
Customer customer2 = new Customer("Mike Chen", "mike@example.com", "555-0456");

customer1.DisplayProfile();
customer2.DisplayProfile();
```

## Common Mistakes to Avoid

1. **Method outside class:**
   ```csharp
   // WRONG - Method is outside the class
   class Customer
   {
       public string Name { get; set; }
   }
   
   public void DisplayProfile()  // Error! Method must be inside class
   {
       Console.WriteLine(Name);
   }
   ```

2. **Forgetting to call method:**
   ```csharp
   // WRONG - Method defined but never called
   Customer customer = new Customer();
   customer.Name = "Sarah";
   // Missing: customer.DisplayProfile();
   ```

3. **Using class name instead of object:**
   ```csharp
   // WRONG - Can't call method on class
   Customer.DisplayProfile();  // Error! Need an object
   
   // CORRECT
   Customer customer = new Customer();
   customer.DisplayProfile();  // ✅
   ```

4. **Method can't access properties:**
   ```csharp
   // WRONG - Properties not accessible (if not public)
   class Customer
   {
       private string Name { get; set; }  // private means can't access from outside
       
       public void DisplayProfile()
       {
           Console.WriteLine(Name);  // This works inside class
       }
   }
   
   Customer customer = new Customer();
   customer.Name = "Sarah";  // Error! Name is private
   ```

## Real-World Application

This pattern is used in:
- Customer relationship management (CRM) systems
- Contact management applications
- Client databases
- Membership systems
- User account systems

## Try This

Modify the program to:
- Add more methods (`UpdateEmail()`, `SendEmail()`)
- Add a constructor to initialize customer data
- Add validation in methods
- Create methods that return values
- Store customers in a list and process them

