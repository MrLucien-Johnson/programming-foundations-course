# example-02-user-input.py
# Demonstrates getting input from users

# Get user's name (always returns a string)
name = input("Enter your name: ")

# Get user's age (convert string to integer)
age = int(input("Enter your age: "))

# Get a price (convert string to float)
price = float(input("Enter a price: £"))

# Display the collected information
print("\n=== Information Summary ===")
print(f"Name: {name}")
print(f"Age: {age}")
print(f"Price: £{price:.2f}")

# Calculate something with the input
years_until_100 = 100 - age
print(f"\nYou'll be 100 years old in {years_until_100} years!")

