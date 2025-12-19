# example-03-looping-through-list.py
# Demonstrates looping through a list

# List of tasks
tasks = [
    "Buy groceries",
    "Finish report",
    "Call client",
    "Review documents"
]

# Loop through tasks and display them
print("=== Your Tasks ===")
for i, task in enumerate(tasks, start=1):
    print(f"{i}. {task}")

# Another example: Process each customer
print("\n=== Processing Customers ===")
customers = ["Alice", "Bob", "Charlie"]

for customer in customers:
    print(f"Processing order for {customer}...")
    print(f"✓ Order processed for {customer}")

print("\nAll customers processed!")

