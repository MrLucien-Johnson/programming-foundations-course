# Module 7 Quiz Answers

## Question 1: How does the Task Tracker demonstrate OOP principles?
**Answer: B** - It uses classes to model tasks and organize code

**Explanation:** The Task Tracker uses OOP by:
- Creating a `TaskItem` class to model tasks
- Creating a `TaskManager` class to manage operations
- Using objects (instances) of these classes
- Organizing data (properties) and behavior (methods) together

**Example:**
```csharp
class TaskItem  // Class definition
{
    public string Title { get; set; }  // Property
    public void MarkComplete() { ... }  // Method
}

TaskItem task = new TaskItem("Buy groceries");  // Object
```

---

## Question 2: What collection type is used to store tasks in TaskManager?
**Answer: B** - `List<TaskItem>`

**Explanation:** The TaskManager uses a `List<TaskItem>` to store multiple TaskItem objects. This allows:
- Adding tasks dynamically
- Removing tasks
- Looping through tasks
- Counting tasks

**Example:**
```csharp
class TaskManager
{
    private List<TaskItem> tasks;  // List of TaskItem objects
}
```

---

## Question 3: Why do we convert task numbers when completing a task (taskNumber - 1)?
**Answer: A** - Because arrays start at 0, but users see 1, 2, 3...

**Explanation:** 
- Users see tasks numbered: 1, 2, 3, 4...
- Lists use indexes: 0, 1, 2, 3...
- Must convert: `index = taskNumber - 1`
- This prevents "Index out of range" errors

**Example:**
```csharp
// User enters: 1 (first task)
// List index: 0 (first item)
int index = 1 - 1;  // = 0 ✅
tasks[0].MarkComplete();
```

---

## Question 4: What control flow structure is used for the main menu loop?
**Answer: B** - while loop

**Explanation:** A `while` loop is used to keep showing the menu until the user chooses to exit. This allows the program to run continuously.

**Example:**
```csharp
bool running = true;
while (running)  // Continues until running is false
{
    ShowMenu();
    // Process choice...
    if (choice == "4")
    {
        running = false;  // Exit loop
    }
}
```

---

## Question 5: What happens when you create a new TaskItem object?
**Answer: B** - The constructor sets the title and IsCompleted to false

**Explanation:** When you create a TaskItem object, the constructor runs automatically. It:
- Sets the Title to the provided value
- Sets IsCompleted to false (new tasks start incomplete)

**Example:**
```csharp
TaskItem task = new TaskItem("Buy groceries");
// Constructor runs:
// - Title = "Buy groceries"
// - IsCompleted = false
```

---

## True or False: The TaskManager class stores tasks in a private List<TaskItem>.
**Answer: True**

**Explanation:** The TaskManager uses a `private List<TaskItem>` to store tasks. The `private` keyword means it can only be accessed from within the TaskManager class, which is good encapsulation.

**Example:**
```csharp
class TaskManager
{
    private List<TaskItem> tasks;  // Private - only accessible inside TaskManager
}
```

---

## True or False: Each TaskItem object has its own Title and IsCompleted values.
**Answer: True**

**Explanation:** Each object is independent. When you create multiple TaskItem objects, each has its own copy of the properties.

**Example:**
```csharp
TaskItem task1 = new TaskItem("Buy groceries");
TaskItem task2 = new TaskItem("Finish report");

task1.Title = "Buy groceries";      // task1's Title
task2.Title = "Finish report";      // task2's Title (different!)
task1.IsCompleted = false;          // task1's IsCompleted
task2.IsCompleted = true;           // task2's IsCompleted (different!)
```

---

## True or False: The menu loop continues until the user chooses option 4 (Exit).
**Answer: True**

**Explanation:** The `while (running)` loop continues as long as `running` is `true`. When the user chooses option 4, `running` is set to `false`, which exits the loop.

**Example:**
```csharp
bool running = true;
while (running)  // Continues while true
{
    // Show menu and process choice
    if (choice == "4")
    {
        running = false;  // Set to false, loop exits
    }
}
```

---

## How Did You Do?

- **8/8 correct:** Excellent! You understand your project well. You're ready to explain it to others! 🎉
- **5-7/8 correct:** Good work! Review the questions you missed. Understanding your own code is important for interviews! 👍
- **0-4/8 correct:** No worries! Review your code and the concepts from Modules 1-6. Understanding comes with practice. 💪

---

## Key Takeaways

1. **OOP organizes code** - Classes model real things (TaskItem, TaskManager)
2. **Collections store groups** - Lists hold multiple objects
3. **Index conversion matters** - Users see 1-based, code uses 0-based
4. **Loops create interactivity** - While loops keep programs running
5. **Constructors initialize** - Set up objects when created

**Remember:** Being able to explain your code is just as important as writing it. This quiz helps you practice that skill! 🚀

