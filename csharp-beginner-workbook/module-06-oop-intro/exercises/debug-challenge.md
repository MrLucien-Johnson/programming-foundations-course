# Debug Challenge: Find the Errors

## 🎯 Your Task

Look at this broken code and find **all the errors**. Fix them so the program runs correctly!

## 🐛 The Broken Code

```csharp
class Book
{
    public string Title
    public double Price
    
    public Book(title, price)
    {
        Title = title;
        Price = price;
    }
    
    public void DisplayInfo()
    {
        Console.WriteLine("Title: " + Title "Price: $" + Price);
    }
}

Book myBook = Book("C# Guide", 29.99);
myBook.DisplayInfo();
```

## 📝 Steps

1. **Create a new project:**
   ```bash
   dotnet new console -o DebugChallenge
   cd DebugChallenge
   ```

2. **Try to type this code into `Program.cs`**

3. **Look for errors** - Cursor or VS Code might show red squiggly lines!

4. **Find all the mistakes:**
   - Error 1: _______________
   - Error 2: _______________
   - Error 3: _______________
   - Error 4: _______________
   - Error 5: _______________

5. **Fix the errors** and run the program: `dotnet run`

6. **Verify it works** - The program should create a Book object and display its information

## 💡 Hints

- Check property syntax
- Check constructor syntax
- Check method calls
- Check string concatenation
- Look at each line carefully

## 🎓 Learning Goals

By completing this challenge, you'll practice:
- Reading error messages
- Finding class definition errors
- Understanding constructor syntax
- Understanding property syntax
- Debugging OOP code

## ✅ Success Criteria

Your program is fixed when:
- ✅ It compiles without errors
- ✅ It runs successfully
- ✅ It creates a Book object correctly
- ✅ It displays the book information
- ✅ You can explain what each error was

## 🔍 Check Your Work

After you've found and fixed the errors, check `debug-challenge-solution.md` to see:
- What each error was
- Why it was wrong
- How to fix it
- Tips for avoiding these mistakes

## 🎉 Bonus Challenge

After fixing the code, try:
- Adding more properties to the Book class
- Creating multiple Book objects
- Adding more methods (e.g., `GetFormattedPrice()`)
- Using a constructor with different parameters

**Remember:** Finding and fixing errors is a superpower! Every programmer does this constantly. You're learning a valuable skill! 💪

