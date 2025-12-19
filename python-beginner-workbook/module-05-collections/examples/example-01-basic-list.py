# example-01-basic-list.py
# Demonstrates basic list operations

tasks = ["Buy groceries", "Finish report", "Call client"]

# Access items
print(f"First task: {tasks[0]}")
print(f"Number of tasks: {len(tasks)}")

# Loop through list
print("\n=== All Tasks ===")
for task in tasks:
    print(f"- {task}")

