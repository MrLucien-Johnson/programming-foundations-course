# main.py
# Main program for the Task Tracker application

from task_manager import TaskManager

def show_menu():
    """Display the main menu."""
    print("\n=== Task Tracker Menu ===")
    print("1. Add Task")
    print("2. View All Tasks")
    print("3. Complete Task")
    print("4. Exit")
    print()

def add_task(task_manager):
    """Get task title from user and add it."""
    title = input("Enter task title: ")
    if title.strip():
        task_manager.add_task(title)
    else:
        print("Task title cannot be empty. Please try again.")

def complete_task(task_manager):
    """Get task number from user and mark it complete."""
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
    """Main program loop."""
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

