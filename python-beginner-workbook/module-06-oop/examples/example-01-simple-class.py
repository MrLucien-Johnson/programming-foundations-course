# example-01-simple-class.py
# Demonstrates a simple class

class Task:
    def __init__(self, title):
        self.title = title
        self.is_completed = False
    
    def mark_complete(self):
        self.is_completed = True

# Create objects
task1 = Task("Buy groceries")
task2 = Task("Finish report")

# Use objects
print(task1.title)
task1.mark_complete()
print(task1.is_completed)

