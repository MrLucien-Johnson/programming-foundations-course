# example-02-list-manager.py
# Demonstrates adding and removing from lists

shopping_list = []

# Add items
shopping_list.append("Milk")
shopping_list.append("Bread")
shopping_list.append("Eggs")

print(f"Shopping list ({len(shopping_list)} items):")
for item in shopping_list:
    print(f"- {item}")

# Remove an item
shopping_list.remove("Bread")
print(f"\nAfter removing Bread ({len(shopping_list)} items):")
for item in shopping_list:
    print(f"- {item}")

