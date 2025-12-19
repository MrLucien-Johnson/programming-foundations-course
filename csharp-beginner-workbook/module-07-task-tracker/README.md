# Module 7: Task Tracker Application - Your Portfolio Project

## 🎯 What You're Building

You're going to build a **complete, working Task Tracker application** - a console program that lets you add, view, and manage tasks. This is your **portfolio project** - something you can show to employers to demonstrate your C# programming skills!

**What the application does:**
- Add new tasks
- View all tasks
- Mark tasks as completed
- Exit the application

**Why this matters:**
- Employers love seeing completed projects
- Shows you can build real applications
- Demonstrates all the skills you've learned
- Something you can actually use!

## 🌍 Real-World Connection

Task trackers are used everywhere in professional work:
- Project managers track team tasks
- Developers track bugs and features
- Teams coordinate work
- Individuals organize daily work

By building this, you're creating:
- A tool you can actually use
- A demonstration of your skills
- A portfolio piece for job applications
- Proof you can build complete applications

**CV/Portfolio mention:** "Built a C# console Task Tracker application with features for adding, viewing, and managing tasks. Used object-oriented programming principles and collections to create a reusable, maintainable solution."

## 💪 Welcome & Motivation

**Congratulations!** You've made it to the final module! 🎉

You've learned:
- Variables and data types
- Control flow (if/else, loops)
- Methods
- Collections (Lists)
- Object-Oriented Programming (Classes)

Now you're going to **combine everything** to build a real application. This is where it all comes together!

**Think of this like:**
- You've learned individual tools (hammer, saw, drill)
- Now you're building a complete piece of furniture
- This project shows you can use all the tools together

**This project will:**
- Use classes to model tasks
- Use lists to store multiple tasks
- Use methods to organize code
- Use loops and if/else for the menu
- Create a complete, working program

## 📋 Project Overview

### What You'll Build

A console-based Task Tracker where users can:
1. **Add Tasks** - Create new tasks with a title
2. **View Tasks** - See all tasks with their completion status
3. **Complete Tasks** - Mark tasks as done
4. **Exit** - Close the application

### Project Structure

Your project will have this structure:

```
TaskTracker/
├── Program.cs          (Main program with menu)
├── TaskItem.cs         (Task class definition)
└── TaskManager.cs      (Manages the list of tasks)
```

**Why this structure?**
- **TaskItem.cs** - Defines what a task is (class)
- **TaskManager.cs** - Handles operations on tasks (add, list, complete)
- **Program.cs** - The main program with the menu

This organization makes your code:
- Easy to understand
- Easy to modify
- Professional-looking
- Ready to show employers

## 🏗️ Step-by-Step Build Instructions

### Step 1: Create the Project

1. **Open Cursor or VS Code**

2. **Open the integrated terminal** (`` Ctrl + ` ``)

3. **Create the project:**
   ```bash
   dotnet new console -o TaskTracker
   cd TaskTracker
   ```

4. **Verify it was created:**
   - You should see `Program.cs` in the file explorer
   - Run `dotnet run` to make sure it works (should print "Hello, World!")

### Step 2: Create the TaskItem Class

Create a new file called `TaskItem.cs`:

1. **In Cursor/VS Code:** Right-click in the file explorer → New File → `TaskItem.cs`

2. **Add this code:**
   ```csharp
   class TaskItem
   {
       public string Title { get; set; }
       public bool IsCompleted { get; set; }
       
       // Constructor - requires a title when creating a task
       public TaskItem(string title)
       {
           Title = title;
           IsCompleted = false;  // New tasks start as incomplete
       }
       
       // Method to mark task as complete
       public void MarkComplete()
       {
           IsCompleted = true;
       }
       
       // Method to display task information
       public void DisplayInfo(int index)
       {
           string status = IsCompleted ? "✓ Complete" : "○ Incomplete";
           Console.WriteLine($"{index}. {Title} - {status}");
       }
   }
   ```

**What this does:**
- Defines a `TaskItem` class with `Title` and `IsCompleted` properties
- Constructor requires a title (can't create a task without one)
- `MarkComplete()` method sets `IsCompleted` to true
- `DisplayInfo()` method shows the task nicely formatted

### Step 3: Create the TaskManager Class

Create a new file called `TaskManager.cs`:

1. **Create `TaskManager.cs`**

2. **Add this code:**
   ```csharp
   class TaskManager
   {
       private List<TaskItem> tasks;
       
       // Constructor - initializes the task list
       public TaskManager()
       {
           tasks = new List<TaskItem>();
       }
       
       // Add a new task
       public void AddTask(string title)
       {
           TaskItem newTask = new TaskItem(title);
           tasks.Add(newTask);
           Console.WriteLine($"✓ Task '{title}' added successfully!");
       }
       
       // Display all tasks
       public void ListTasks()
       {
           if (tasks.Count == 0)
           {
               Console.WriteLine("No tasks yet. Add some tasks to get started!");
               return;
           }
           
           Console.WriteLine("\n=== Your Tasks ===");
           for (int i = 0; i < tasks.Count; i++)
           {
               tasks[i].DisplayInfo(i + 1);  // Display with number starting from 1
           }
           Console.WriteLine($"\nTotal: {tasks.Count} task(s)");
       }
       
       // Mark a task as complete
       public void CompleteTask(int taskNumber)
       {
           // Convert to index (user sees 1, 2, 3... but list uses 0, 1, 2...)
           int index = taskNumber - 1;
           
           if (index >= 0 && index < tasks.Count)
           {
               if (tasks[index].IsCompleted)
               {
                   Console.WriteLine("This task is already completed!");
               }
               else
               {
                   tasks[index].MarkComplete();
                   Console.WriteLine($"✓ Task '{tasks[index].Title}' marked as complete!");
               }
           }
           else
           {
               Console.WriteLine("Invalid task number. Please try again.");
           }
       }
       
       // Get the number of tasks
       public int GetTaskCount()
       {
           return tasks.Count;
       }
   }
   ```

**What this does:**
- Stores a list of `TaskItem` objects
- `AddTask()` - Creates and adds a new task
- `ListTasks()` - Shows all tasks with numbers
- `CompleteTask()` - Marks a task complete by number
- Handles edge cases (empty list, invalid numbers)

### Step 4: Create the Main Program

Replace the contents of `Program.cs` with:

```csharp
class Program
{
    static void Main(string[] args)
    {
        TaskManager taskManager = new TaskManager();
        bool running = true;
        
        Console.WriteLine("=== Welcome to Task Tracker ===");
        Console.WriteLine("Manage your tasks efficiently!\n");
        
        while (running)
        {
            ShowMenu();
            string choice = Console.ReadLine();
            
            switch (choice)
            {
                case "1":
                    AddTask(taskManager);
                    break;
                case "2":
                    taskManager.ListTasks();
                    break;
                case "3":
                    CompleteTask(taskManager);
                    break;
                case "4":
                    running = false;
                    Console.WriteLine("\nThank you for using Task Tracker. Goodbye!");
                    break;
                default:
                    Console.WriteLine("Invalid choice. Please enter 1, 2, 3, or 4.");
                    break;
            }
            
            if (running)
            {
                Console.WriteLine("\nPress any key to continue...");
                Console.ReadKey();
                Console.Clear();
            }
        }
    }
    
    static void ShowMenu()
    {
        Console.WriteLine("=== Task Tracker Menu ===");
        Console.WriteLine("1. Add Task");
        Console.WriteLine("2. View All Tasks");
        Console.WriteLine("3. Complete Task");
        Console.WriteLine("4. Exit");
        Console.Write("Enter your choice: ");
    }
    
    static void AddTask(TaskManager taskManager)
    {
        Console.Write("Enter task title: ");
        string title = Console.ReadLine();
        
        if (string.IsNullOrWhiteSpace(title))
        {
            Console.WriteLine("Task title cannot be empty. Please try again.");
        }
        else
        {
            taskManager.AddTask(title);
        }
    }
    
    static void CompleteTask(TaskManager taskManager)
    {
        if (taskManager.GetTaskCount() == 0)
        {
            Console.WriteLine("No tasks to complete. Add some tasks first!");
            return;
        }
        
        taskManager.ListTasks();
        Console.Write("\nEnter task number to mark complete: ");
        
        string input = Console.ReadLine();
        if (int.TryParse(input, out int taskNumber))
        {
            taskManager.CompleteTask(taskNumber);
        }
        else
        {
            Console.WriteLine("Invalid input. Please enter a number.");
        }
    }
}
```

**What this does:**
- Creates a `TaskManager` object
- Shows a menu in a loop
- Handles user choices with switch statement
- Calls appropriate methods based on choice
- Validates input
- Clears screen between actions for better UX

### Step 5: Run Your Application

1. **Save all files** (`Ctrl + S` or `Cmd + S`)

2. **Run the application:**
   ```bash
   dotnet run
   ```

3. **Try it out:**
   - Add a task (choose option 1)
   - View tasks (choose option 2)
   - Complete a task (choose option 3)
   - Exit (choose option 4)

## 💻 Complete Code Files

The complete, working code is available in the `project/` folder. You can:
- Study it to understand the structure
- Use it as a reference
- Run it to see how it works

**Files in `project/` folder:**
- `TaskItem.cs` - Complete TaskItem class
- `TaskManager.cs` - Complete TaskManager class
- `Program.cs` - Complete main program

## 🎮 Running the Application

### Sample Session

```
=== Welcome to Task Tracker ===
Manage your tasks efficiently!

=== Task Tracker Menu ===
1. Add Task
2. View All Tasks
3. Complete Task
4. Exit
Enter your choice: 1
Enter task title: Buy groceries
✓ Task 'Buy groceries' added successfully!

Press any key to continue...

=== Task Tracker Menu ===
1. Add Task
2. View All Tasks
3. Complete Task
4. Exit
Enter your choice: 1
Enter task title: Finish report
✓ Task 'Finish report' added successfully!

Press any key to continue...

=== Task Tracker Menu ===
1. Add Task
2. View All Tasks
3. Complete Task
4. Exit
Enter your choice: 2

=== Your Tasks ===
1. Buy groceries - ○ Incomplete
2. Finish report - ○ Incomplete

Total: 2 task(s)

Press any key to continue...

=== Task Tracker Menu ===
1. Add Task
2. View All Tasks
3. Complete Task
4. Exit
Enter your choice: 3

=== Your Tasks ===
1. Buy groceries - ○ Incomplete
2. Finish report - ○ Incomplete

Total: 2 task(s)

Enter task number to mark complete: 1
✓ Task 'Buy groceries' marked as complete!

Press any key to continue...

=== Task Tracker Menu ===
1. Add Task
2. View All Tasks
3. Complete Task
4. Exit
Enter your choice: 2

=== Your Tasks ===
1. Buy groceries - ✓ Complete
2. Finish report - ○ Incomplete

Total: 2 task(s)

Press any key to continue...

=== Task Tracker Menu ===
1. Add Task
2. View All Tasks
3. Complete Task
4. Exit
Enter your choice: 4

Thank you for using Task Tracker. Goodbye!
```

## 🎓 How It All Works Together

### The Flow

1. **Program starts** → Creates a `TaskManager` object
2. **Menu loop** → Shows menu, gets user choice
3. **User chooses** → Switch statement routes to correct method
4. **TaskManager methods** → Handle the actual work
5. **TaskItem objects** → Store individual task data
6. **Repeat** → Until user chooses Exit

### Key Concepts Used

- **Classes** - `TaskItem` and `TaskManager` classes
- **Objects** - Creating `TaskItem` objects and a `TaskManager` object
- **Lists** - `List<TaskItem>` stores multiple tasks
- **Methods** - Each operation is a method
- **Loops** - `while` loop keeps menu running
- **If/Else** - Validates input and checks conditions
- **Switch** - Routes menu choices

**Real-world connection:** This is exactly how professional applications are structured - organized into classes, using collections, with clear separation of concerns.

## 🚀 Optional Enhancements

Once you have the basic version working, try these enhancements! Each has its own file in the `exercises/` folder.

### Enhancement 1: Add Due Dates
Add a `DueDate` property to tasks and show tasks due soon.

**See:** `exercises/enhancement-01.md`

### Enhancement 2: Add Task Categories
Add categories (Work, Personal, Shopping) and filter by category.

**See:** `exercises/enhancement-02.md`

### Enhancement 3: Delete Tasks
Add ability to delete tasks from the list.

**See:** `exercises/enhancement-03.md`

### Enhancement 4: Colored Output
Use colors to highlight completed vs incomplete tasks.

**See:** `exercises/enhancement-04.md`

### Enhancement 5: Save/Load to File
Save tasks to a JSON file and load them when program starts.

**See:** `exercises/enhancement-05.md`

**Try these enhancements to make your project even more impressive!**

## 🐛 Debug Challenge

Find the errors in a broken TaskManager method! See `exercises/debug-challenge.md` for the challenge.

## 🧪 Quiz: Test Your Understanding

Answer questions about your project! See `exercises/quiz.md` for the quiz.

## 💼 Portfolio Tips

### How to Present This Project

**1. Screenshot Your Running Application**
- Take screenshots showing the menu and task list
- Show it working (adding tasks, completing tasks)
- Include these in your portfolio

**2. Upload to GitHub**
- Create a GitHub account (free)
- Create a new repository called "TaskTracker"
- Upload your code files
- Add a README explaining what it does

**3. Write a Portfolio Description**

Example:
```
Task Tracker Application (C#)

A console-based task management application built with C# and .NET.

Features:
- Add, view, and manage tasks
- Mark tasks as complete
- Clean, user-friendly interface
- Object-oriented design using classes

Technologies: C#, .NET, Object-Oriented Programming

This project demonstrates:
- Class design and object creation
- Working with collections (Lists)
- Control flow (loops, conditionals)
- Method organization
- Input validation
```

**4. Mention in Your CV/Resume**

Example:
```
Projects:
Task Tracker Application (C#)
- Built a console application for task management
- Implemented object-oriented design with classes
- Used collections and control flow for task operations
- Created reusable, maintainable code structure
```

**5. Be Ready to Explain**
- How the classes work together
- Why you organized code this way
- What you'd add next
- What you learned building it

## ✅ Project Checklist

Before considering your project complete, make sure:

### Functionality
- [ ] Can add new tasks
- [ ] Can view all tasks
- [ ] Can mark tasks as complete
- [ ] Menu system works correctly
- [ ] Exit option works
- [ ] Input validation works

### Code Quality
- [ ] Code is organized into classes
- [ ] Methods are clear and focused
- [ ] Variable names are descriptive
- [ ] Code has comments where helpful
- [ ] No obvious bugs

### Testing
- [ ] Tested adding multiple tasks
- [ ] Tested viewing tasks
- [ ] Tested completing tasks
- [ ] Tested invalid input
- [ ] Tested empty task list

## 🎉 Congratulations!

When you complete this project, you've:

- ✅ **Learned fundamental C# programming**
- ✅ **Built a complete application**
- ✅ **Created a portfolio piece**
- ✅ **Gained confidence in your abilities**
- ✅ **Taken a major step toward a skilled tech career**

**You've come a long way from "Hello, World!"**

This project demonstrates:
- You can write C# code
- You understand OOP
- You can build complete applications
- You're ready for entry-level programming work

## 🚀 Next Steps

After completing this project:

1. **Try the enhancements** - Make it even better!
2. **Add it to your portfolio** - GitHub, CV, LinkedIn
3. **Build more projects** - Practice makes perfect
4. **Keep learning** - There's always more to discover
5. **Be proud** - You built something real!

**Remember:** Every expert was once a beginner. You've built a complete application. That's a huge achievement! 🎊

---

**Need help?** Review Modules 1-6 if you get stuck. The concepts you need are all there!

---

## 🔗 Navigation

- **[Previous: Module 6 - Intro to OOP →](../module-06-oop-intro/README.md)**
- **[Back to C# Workbook →](../README.md)**
- **[Back to Course Home →](../../README.md)**
- **[Course Links →](../../COURSE-LINKS.md)**
- **[Portfolio Guide →](../../../Programming-Foundations-Course/PORTFOLIO-GUIDE.md)**
- **[Final Assessments →](../../../Programming-Foundations-Course/Assessments/)**
- **[Examples →](project/)** | **[Exercises →](exercises/)**