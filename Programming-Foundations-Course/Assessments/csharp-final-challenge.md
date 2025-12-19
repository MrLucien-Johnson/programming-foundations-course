# C# Final Challenge: Enhance Your Task Tracker

## 🎯 Your Mission

Congratulations on completing the C# Beginner Workbook! Now it's time to demonstrate your skills by enhancing your Task Tracker application.

## 📋 The Challenge

**Extend your Task Tracker** by adding **at least ONE** meaningful feature from the list below. This challenge tests your ability to:
- Understand existing code
- Add new functionality
- Combine multiple concepts
- Solve real problems

## 🚀 Feature Options

Choose **at least one** feature to add (feel free to add more!):

### Option 1: Task Categories
Add the ability to assign categories to tasks (e.g., "Work", "Personal", "Shopping") and filter tasks by category.

**Requirements:**
- Add `Category` property to TaskItem class
- Update TaskManager to handle categories
- Add menu option to filter by category
- Display category when listing tasks

**Skills demonstrated:** Classes, properties, filtering, user input

### Option 2: Due Dates
Add due dates to tasks and show which tasks are due soon or overdue.

**Requirements:**
- Add `DueDate` property to TaskItem (use `DateTime?` for nullable)
- Update TaskManager to handle dates
- Add menu option to show tasks due today/soon
- Display due dates when listing tasks

**Skills demonstrated:** Classes, DateTime, nullable types, date comparisons

### Option 3: Delete Tasks
Add the ability to delete tasks from the list.

**Requirements:**
- Add `DeleteTask()` method to TaskManager
- Add menu option to delete tasks
- Show confirmation before deleting
- Update task numbering after deletion

**Skills demonstrated:** List manipulation, user confirmation, error handling

### Option 4: Save/Load to File
Save tasks to a JSON file and load them when the program starts.

**Requirements:**
- Use `System.Text.Json` (add NuGet package if needed)
- Save tasks when program exits
- Load tasks when program starts
- Handle file not found (first run)

**Skills demonstrated:** File I/O, JSON serialization, error handling

### Option 5: Task Priority
Add priority levels (Low, Medium, High) and sort/filter by priority.

**Requirements:**
- Add `Priority` property to TaskItem (use enum or string)
- Update display to show priority
- Add menu option to sort by priority
- Use Console colors or symbols to indicate priority

**Skills demonstrated:** Enums, sorting, display formatting

## ✅ Pass Criteria

Your enhanced Task Tracker passes if:

- [ ] **Code compiles and runs** - No compilation or runtime errors
- [ ] **Feature works correctly** - The new feature functions as intended
- [ ] **Code is organized** - Clean, readable, well-structured
- [ ] **Integrates smoothly** - New feature works with existing code
- [ ] **User-friendly** - Clear prompts and error messages
- [ ] **You can explain it** - You understand what you built

## 💡 Tips for Success

### Before You Start

1. **Review your existing code** - Understand how it works
2. **Plan your changes** - Think about what needs to be modified
3. **Start small** - Get one feature working, then add more
4. **Test frequently** - Run your code often as you build

### While Coding

1. **Read error messages** - They tell you what's wrong
2. **Test edge cases** - Empty lists, invalid input, null values
3. **Keep it simple** - Don't overcomplicate
4. **Comment your code** - Explain what you're doing

### Common Challenges

- **"Where do I start?"** - Start with the TaskItem class, add the property
- **"How do I integrate it?"** - Update TaskManager methods that use TaskItem
- **"It won't compile!"** - Check syntax, missing semicolons, type mismatches
- **"Is this right?"** - If it compiles, runs, and works, it's probably right!

## 🎓 What This Demonstrates

Completing this challenge shows you can:

- ✅ Read and understand existing C# code
- ✅ Extend functionality without breaking existing features
- ✅ Apply multiple programming concepts together
- ✅ Solve problems independently
- ✅ Write working, organized C# code

## 📝 Submission Guidelines

### What to Submit

1. **Your enhanced code** - All C# files (.cs) and project files
2. **Brief description** - What feature(s) you added and how
3. **Screenshots** - Show it running (optional but helpful)

### How to Submit

- **Upload to GitHub** - Create a repository with your enhanced project
- **Or share files** - If submitting to instructor/platform
- **Include README** - Explain what you added

### Example Description

> "I enhanced my Task Tracker by adding task categories. Users can now assign categories like 'Work' or 'Personal' to tasks and filter the task list by category. I added a `Category` property to the TaskItem class, updated the TaskManager to handle category filtering, and added a new menu option. This taught me how to extend existing code while maintaining functionality."

## 🌟 Going Beyond

Want to impress? Try adding:

- **Multiple features** - Combine 2-3 features
- **Better UI** - Colored output, better formatting
- **Data validation** - Ensure valid dates, categories, etc.
- **Statistics** - Show counts by category, completion rates
- **Search** - Find tasks by keyword

## 💪 Remember

- **This is achievable** - You have all the skills needed
- **Mistakes are learning** - Errors teach you more than success
- **There's no one right way** - Your solution is valid if it works
- **You've got this** - You've learned everything needed to complete this

## 🎉 Success!

When you complete this challenge, you've:

- ✅ Demonstrated real C# programming skills
- ✅ Built something you can show employers
- ✅ Proved you can extend existing code
- ✅ Created a portfolio piece
- ✅ Gained confidence in your abilities

**You're not just learning to code - you're becoming a C# developer!** 🚀

---

**Ready to start?** Review your Task Tracker code, choose a feature, and begin enhancing!

