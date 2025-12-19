# Exercise 1 Solution

```python
shopping_list = []
shopping_list.append("Milk")
shopping_list.append("Bread")
shopping_list.append("Eggs")

print("=== Shopping List ===")
for i, item in enumerate(shopping_list, start=1):
    print(f"{i}. {item}")

print(f"\nTotal items: {len(shopping_list)}")
```

