// TaskManager.cs
// This class manages the collection of tasks

using System;
using System.Collections.Generic;

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

