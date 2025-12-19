# example-03-function-with-return.py
# Demonstrates functions that return values

def is_valid_age(age):
    """Check if age is between 18 and 100."""
    if age >= 18 and age <= 100:
        return True
    else:
        return False

# Use the function
user_age = int(input("Enter your age: "))
if is_valid_age(user_age):
    print("✓ Age is valid!")
else:
    print("❌ Age must be between 18 and 100.")

