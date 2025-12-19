# Exercise 2: Create a Product Class with Constructor

## 🎯 Your Task

Build a `Product` class with `Price` and `Description` properties, and a constructor that requires these values.

## 📝 Learning Goals

By completing this exercise, you'll practice:
- Defining a class with properties
- Creating a constructor
- Using constructors to initialize objects
- Ensuring objects are created with required information

## 🚀 Steps

1. **Create a new project:**
   ```bash
   dotnet new console -o ProductClass
   cd ProductClass
   ```

2. **Open `Program.cs` in Cursor or VS Code**

3. **Write a program that:**
   - Defines a `Product` class with:
     - `Price` property (double)
     - `Description` property (string)
     - A constructor that takes `price` and `description` as parameters
   - Creates at least 3 Product objects using the constructor
   - Displays all products with their prices and descriptions

## 💡 Hints

- Define the class: `class Product { ... }`
- Add properties: `public double Price { get; set; }`
- Create constructor: `public Product(double price, string description) { ... }`
- In constructor, set properties: `Price = price;`
- Create objects: `Product item = new Product(29.99, "Widget");`

## 📋 Example Output

```
=== Product Catalog ===
Product 1:
  Description: Wireless Mouse
  Price: $29.99

Product 2:
  Description: USB Keyboard
  Price: $45.00

Product 3:
  Description: Monitor Stand
  Price: $35.50
```

## ✅ Tips

- Make sure constructor parameters match property types
- Set properties inside the constructor
- Use the constructor when creating objects (pass values)
- Format prices with currency formatting (`F2`)

## 🎓 Real-World Connection

This is exactly how inventory systems work! Products must have a price and description when created. Constructors ensure this requirement is met. Used in:
- E-commerce systems
- Inventory management
- Product catalogs
- Point-of-sale systems

## 🔍 Bonus Challenge

After completing the basic version, try:
- Adding a `Name` property
- Adding validation in the constructor (e.g., price must be positive)
- Creating a method to display product info
- Calculating total value of all products

## 🔍 Check Your Work

Once you've written your program:
1. Verify the constructor requires both price and description
2. Check that you can't create a Product without providing values
3. Make sure properties are set correctly in the constructor
4. Test creating multiple products with different values
5. Check the solution in `exercise-02-solution.md` to see one possible approach

**Remember:** If your class has a constructor and you create objects using it, you've succeeded! 🎉

