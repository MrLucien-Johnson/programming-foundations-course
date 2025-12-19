// TaskItem.cs
// This class represents a single task in the Task Tracker application

using System;

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

