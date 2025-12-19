# Exercise 1: Shopping List

## 🎯 Your Task

Create a program that manages a shopping list using `List<string>`. Add items, display the list, and show the count.

## 📝 Learning Goals

By completing this exercise, you'll practice:
- Creating a `List<string>`
- Adding items to a list
- Displaying all items in a list
- Counting items in a list
- Building a practical list management tool

## 🚀 Steps

1. **Create a new project:**
   ```bash
   dotnet new console -o ShoppingList
   cd ShoppingList
   ```

2. **Open `Program.cs` in Cursor or VS Code**

3. **Write a program that:**
   - Creates a `List<string>` called `shoppingList`
   - Adds at least 5 items to the list (e.g., "Milk", "Bread", "Eggs", etc.)
   - Displays all items in the list with numbers (1, 2, 3, etc.)
   - Shows the total count of items

## 💡 Hints

- Use `List<string> shoppingList = new List<string>();` to create the list
- Use `shoppingList.Add("item")` to add items
- Use a `foreach` loop to display all items
- Use `shoppingList.Count` to get the total number of items
- Number the items starting from 1 (not 0) for display

## 📋 Example Output

```
=== Shopping List ===
1. Milk
2. Bread
3. Eggs
4. Butter
5. Cheese

Total items: 5
```

## ✅ Tips

- Choose realistic shopping items
- Make the output clear and formatted
- Use `foreach` for displaying items (it's easier!)
- Show the count clearly

## 🎓 Real-World Connection

This is exactly how shopping list apps work! They:
- Store items in a list
- Allow adding new items
- Display all items
- Show how many items you need to buy

Used in:
- Shopping list applications
- Grocery apps
- To-do list apps
- Inventory tracking systems

## 🔍 Bonus Challenge

After completing the basic version, try:
- Removing an item from the list
- Checking if an item is already on the list before adding
- Adding items from user input
- Creating a menu to add/remove/view items

## 🔍 Check Your Work

Once you've written your program:
1. Verify all items are displayed correctly
2. Check that the count is correct
3. Test adding more items
4. Make sure the formatting looks good
5. Check the solution in `exercise-01-solution.md` to see one possible approach

**Remember:** If your program creates a list, adds items, displays them, and shows the count, you've succeeded! 🎉

