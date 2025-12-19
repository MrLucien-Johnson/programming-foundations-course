// Program.cs
// Main program for the Task Tracker application

using System;

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

