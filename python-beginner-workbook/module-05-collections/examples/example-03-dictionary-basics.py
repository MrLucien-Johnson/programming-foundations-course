# example-03-dictionary-basics.py
# Demonstrates dictionary operations

customer = {
    "name": "Sarah",
    "email": "sarah@example.com",
    "age": 32
}

# Access values
print(f"Name: {customer['name']}")
print(f"Email: {customer['email']}")

# Add new key
customer["phone"] = "123-456-7890"

# Safe access
address = customer.get("address", "Not provided")
print(f"Address: {address}")

# Display all info
print("\n=== Customer Info ===")
for key, value in customer.items():
    print(f"{key}: {value}")

