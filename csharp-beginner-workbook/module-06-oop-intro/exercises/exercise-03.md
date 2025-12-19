# Exercise 3: Create a Customer Class with Method

## 🎯 Your Task

Create a `Customer` class with a method that prints a formatted customer profile.

## 📝 Learning Goals

By completing this exercise, you'll practice:
- Defining a class with properties
- Adding methods to a class
- Using methods to perform actions with objects
- Organizing data and behavior together

## 🚀 Steps

1. **Create a new project:**
   ```bash
   dotnet new console -o CustomerClass
   cd CustomerClass
   ```

2. **Open `Program.cs` in Cursor or VS Code**

3. **Write a program that:**
   - Defines a `Customer` class with:
     - `Name` property (string)
     - `Email` property (string)
     - `Phone` property (string)
     - A method called `DisplayProfile()` that prints formatted customer information
   - Creates at least 2 Customer objects
   - Sets their properties
   - Calls the `DisplayProfile()` method for each customer

## 💡 Hints

- Define the class with properties
- Add a method: `public void DisplayProfile() { ... }`
- Inside the method, use the properties: `Console.WriteLine($"Name: {Name}");`
- Create objects and set properties
- Call the method: `customer1.DisplayProfile();`

## 📋 Example Output

```
=== Customer Profiles ===

Customer Profile:
  Name: Sarah Johnson
  Email: sarah@example.com
  Phone: 555-0123

Customer Profile:
  Name: Mike Chen
  Email: mike@example.com
  Phone: 555-0456
```

## ✅ Tips

- Make the method format the output nicely
- Use the object's properties inside the method
- Call the method on each customer object
- Add headers and separators for better formatting

## 🎓 Real-World Connection

This is exactly how CRM systems work! Customer objects have properties (name, email) and methods (display profile, send email, update info). Used in:
- Customer relationship management (CRM) systems
- Contact management applications
- Client databases
- Membership systems

## 🔍 Bonus Challenge

After completing the basic version, try:
- Adding more methods (e.g., `SendWelcomeEmail()`, `UpdatePhone()`)
- Adding a constructor to initialize customer data
- Adding validation in methods
- Creating a method that returns formatted information as a string

## 🔍 Check Your Work

Once you've written your program:
1. Verify the method is inside the class
2. Check that the method uses the object's properties
3. Make sure you can call the method on each customer
4. Test that each customer displays their own information
5. Check the solution in `exercise-03-solution.md` to see one possible approach

**Remember:** If your class has a method and you can call it on objects, you've succeeded! 🎉

