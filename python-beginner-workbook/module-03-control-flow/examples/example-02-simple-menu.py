# example-02-simple-menu.py
# Demonstrates a while loop for an interactive menu

running = True

while running:
    print("\n=== Task Manager Menu ===")
    print("1. Add task")
    print("2. View tasks")
    print("3. Complete task")
    print("4. Exit")
    
    choice = input("\nEnter your choice (1-4): ")
    
    if choice == "1":
        task_name = input("Enter task name: ")
        print(f"✓ Added task: {task_name}")
    elif choice == "2":
        print("Your tasks will appear here...")
    elif choice == "3":
        print("Marking task as complete...")
    elif choice == "4":
        running = False
        print("Goodbye! Thanks for using Task Manager.")
    else:
        print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")

print("\nProgram ended.")

