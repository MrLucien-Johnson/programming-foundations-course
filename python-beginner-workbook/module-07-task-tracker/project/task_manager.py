# task_manager.py
# This class manages the collection of tasks

from task_item import TaskItem

class TaskManager:
    def __init__(self):
        self.tasks = []
    
    def add_task(self, title):
        """Add a new task to the list."""
        new_task = TaskItem(title)
        self.tasks.append(new_task)
        print(f"✓ Task '{title}' added successfully!")
    
    def list_tasks(self):
        """Display all tasks with their status."""
        if len(self.tasks) == 0:
            print("No tasks yet. Add some tasks to get started!")
            return
        
        print("\n=== Your Tasks ===")
        for i, task in enumerate(self.tasks, start=1):
            task.display_info(i)  # Display with number starting from 1
        print(f"\nTotal: {len(self.tasks)} task(s)")
    
    def complete_task(self, task_number):
        """Mark a task as complete by its number."""
        # Convert to index (user sees 1, 2, 3... but list uses 0, 1, 2...)
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
        """Return the number of tasks."""
        return len(self.tasks)

