# Exercise 2: Customer List with Count

## 🎯 Your Task

Build a program that stores customer names in a list, displays them, and shows the total count.

## 📝 Learning Goals

By completing this exercise, you'll practice:
- Creating a `List<string>` for customer names
- Adding multiple customers to the list
- Using `foreach` to loop through the list
- Displaying formatted customer information
- Using `Count` to show totals

## 🚀 Steps

1. **Create a new project:**
   ```bash
   dotnet new console -o CustomerList
   cd CustomerList
   ```

2. **Open `Program.cs` in Cursor or VS Code**

3. **Write a program that:**
   - Creates a `List<string>` called `customers`
   - Adds at least 4 customer names (e.g., "Sarah Johnson", "Mike Chen", etc.)
   - Displays a header (e.g., "=== Customer Database ===")
   - Uses a `foreach` loop to display each customer with a number
   - Shows the total number of customers at the end

## 💡 Hints

- Create the list: `List<string> customers = new List<string>();`
- Add customers: `customers.Add("Name");`
- Use `foreach (string customer in customers)` to loop
- Keep track of the customer number as you loop
- Use `customers.Count` for the total

## 📋 Example Output

```
=== Customer Database ===
1. Sarah Johnson
2. Mike Chen
3. Emma Davis
4. David Wilson

Total customers: 4
```

## ✅ Tips

- Use realistic customer names
- Format the output nicely with headers
- Number customers starting from 1
- Make the total count clear and visible

## 🎓 Real-World Connection

This is exactly how customer databases work! CRM systems:
- Store customer names in lists/collections
- Display customer information
- Track total number of customers
- Process each customer individually

Used in:
- Customer relationship management (CRM) systems
- Contact management applications
- Client databases
- Membership systems

## 🔍 Bonus Challenge

After completing the basic version, try:
- Adding customers from user input
- Searching for a specific customer
- Removing a customer
- Displaying customers in alphabetical order
- Creating a menu system to manage customers

## 🔍 Check Your Work

Once you've written your program:
1. Verify all customers are displayed
2. Check that the numbering is correct (1, 2, 3, 4...)
3. Verify the total count matches the number of customers
4. Test with different numbers of customers
5. Check the solution in `exercise-02-solution.md` to see one possible approach

**Remember:** If your program stores customers, displays them with numbers, and shows the total count, you've succeeded! 🎉

