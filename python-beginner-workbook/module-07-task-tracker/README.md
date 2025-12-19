# Module 7: Task Tracker Application - Your Portfolio Project

## 🎯 What You're Building

You're going to build a **complete, working Task Tracker application** - a console program that lets you add, view, and manage tasks. This is your **portfolio project** - something you can show to employers!

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

Task trackers are used everywhere in professional work. By building this, you're creating a tool you can use and a portfolio piece for job applications.

## 💪 Welcome & Motivation

**Congratulations!** You've made it to the final module! 🎉

You've learned:
- Variables and data types
- Control flow (if/else, loops)
- Functions
- Collections (Lists, Dictionaries)
- Object-Oriented Programming (Classes)

Now you're going to **combine everything** to build a real application!

## 📋 Project Structure

Your project will have this structure:

```
TaskTracker/
├── main.py          (Main program with menu)
├── task_item.py    (Task class definition)
└── task_manager.py (Manages the list of tasks)
```

## 🏗️ Step-by-Step Build Instructions

### Step 1: Create the Project Folder

1. Create a folder called `TaskTracker`
2. Open it in Cursor or VS Code

### Step 2: Create task_item.py

Create `task_item.py`:

```python
class TaskItem:
    def __init__(self, title):
        self.title = title
        self.is_completed = False
    
    def mark_complete(self):
        self.is_completed = True
    
    def display_info(self, index):
        status = "✓ Complete" if self.is_completed else "○ Incomplete"
        print(f"{index}. {self.title} - {status}")
```

### Step 3: Create task_manager.py

Create `task_manager.py`:

```python
from task_item import TaskItem

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title):
        new_task = TaskItem(title)
        self.tasks.append(new_task)
        print(f"✓ Task '{title}' added successfully!")
    
    def list_tasks(self):
        if len(self.tasks) == 0:
            print("No tasks yet. Add some tasks to get started!")
            return
        
        print("\n=== Your Tasks ===")
        for i, task in enumerate(self.tasks, start=1):
            task.display_info(i)
        print(f"\nTotal: {len(self.tasks)} task(s)")
    
    def complete_task(self, task_number):
        index = task_number - 1
        
        if 0 <= index < len(self.tasks):
            if self.tasks[index].is_completed:
                print("This task is already completed!")
            else:
                self.tasks[index].mark_complete()
                print(f"✓ Task '{self.tasks[index].title}' marked as complete!")
        else:
            print("Invalid task number. Please try again.")
    
    def get_task_count(self):
        return len(self.tasks)
```

### Step 4: Create main.py

Create `main.py`:

```python
from task_manager import TaskManager

def show_menu():
    print("\n=== Task Tracker Menu ===")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Complete Task")
    print("4. Exit")
    print()

def add_task(task_manager):
    title = input("Enter task title: ")
    if title.strip():
        task_manager.add_task(title)
    else:
        print("Task title cannot be empty. Please try again.")

def complete_task(task_manager):
    if task_manager.get_task_count() == 0:
        print("No tasks to complete. Add some tasks first!")
        return
    
    task_manager.list_tasks()
    try:
        task_number = int(input("\nEnter task number to mark complete: "))
        task_manager.complete_task(task_number)
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    task_manager = TaskManager()
    running = True
    
    print("=== Welcome to Task Tracker ===")
    print("Manage your tasks efficiently!\n")
    
    while running:
        show_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            add_task(task_manager)
        elif choice == "2":
            task_manager.list_tasks()
        elif choice == "3":
            complete_task(task_manager)
        elif choice == "4":
            running = False
            print("\nThank you for using Task Tracker. Goodbye!")
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")
        
        if running:
            input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()
```

### Step 5: Run Your Application

```bash
python main.py
```

## 💻 Complete Code Files

The complete, working code is available in the `project/` folder. You can study it, use it as reference, or run it directly.

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

Press Enter to continue...

=== Task Tracker Menu ===
1. Add Task
2. View All Tasks
3. Complete Task
4. Exit

Enter your choice: 2

=== Your Tasks ===
1. Buy groceries - ○ Incomplete

Total: 1 task(s)

Press Enter to continue...
```

## 🚀 Optional Enhancements

Once you have the basic version working, try these enhancements! Each has its own file in the `exercises/` folder.

### Enhancement 1: Add Due Dates
Add a `due_date` property to tasks and show tasks due soon.

**See:** `exercises/enhancement-01.md`

### Enhancement 2: Add Task Categories
Add categories (Work, Personal, Shopping) and filter by category.

**See:** `exercises/enhancement-02.md`

### Enhancement 3: Delete Tasks
Add ability to delete tasks from the list.

**See:** `exercises/enhancement-03.md`

### Enhancement 4: Colored Output
Use ANSI colors to highlight completed vs incomplete tasks.

**See:** `exercises/enhancement-04.md`

### Enhancement 5: Save/Load to JSON
Save tasks to a JSON file and load them when program starts.

**See:** `exercises/enhancement-05.md`

## 🐛 Debug Challenge

Find the errors in a broken TaskManager method! See `exercises/debug-challenge.md`

## 🧪 Quiz: Test Your Understanding

Answer questions about your project! See `exercises/quiz.md`

## 💼 Portfolio Tips

### How to Present This Project

**1. Screenshot Your Running Application**
- Take screenshots showing the menu and task list
- Show it working (adding tasks, completing tasks)

**2. Upload to GitHub**
- Create a GitHub account (free)
- Create a new repository called "TaskTracker"
- Upload your code files
- Add a README explaining what it does

**3. Write a Portfolio Description**

Example:
```
Task Tracker Application (Python)

A console-based task management application built with Python.

Features:
- Add, view, and manage tasks
- Mark tasks as complete
- Clean, user-friendly interface
- Object-oriented design using classes

Technologies: Python, Object-Oriented Programming

This project demonstrates:
- Class design and object creation
- Working with collections (Lists)
- Control flow (loops, conditionals)
- Function organization
- Input validation
```

**4. Mention in Your CV/Resume**

Example:
```
Projects:
Task Tracker Application (Python)
- Built a console application for task management
- Implemented object-oriented design with classes
- Used collections and control flow for task operations
- Created reusable, maintainable code structure
```

## ✅ Project Checklist

Before considering your project complete, make sure:

- [ ] Can add new tasks
- [ ] Can view all tasks
- [ ] Can mark tasks as complete
- [ ] Menu system works correctly
- [ ] Exit option works
- [ ] Input validation works
- [ ] Code is organized into classes
- [ ] Methods are clear and focused
- [ ] Code has comments where helpful

## 🎉 Congratulations!

When you complete this project, you've:
- ✅ **Learned fundamental Python programming**
- ✅ **Built a complete application**
- ✅ **Created a portfolio piece**
- ✅ **Gained confidence in your abilities**
- ✅ **Taken a major step toward a skilled tech career**

**You've come a long way from "Hello, World!"**

---

**Need help?** Review Modules 1-6 if you get stuck. The concepts you need are all there!
