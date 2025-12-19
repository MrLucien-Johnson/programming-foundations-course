# task_item.py
# This class represents a single task in the Task Tracker application

class TaskItem:
    def __init__(self, title):
        self.title = title
        self.is_completed = False  # New tasks start as incomplete
    
    def mark_complete(self):
        """Mark this task as completed."""
        self.is_completed = True
    
    def display_info(self, index):
        """Display task information with index number."""
        status = "✓ Complete" if self.is_completed else "○ Incomplete"
        print(f"{index}. {self.title} - {status}")

