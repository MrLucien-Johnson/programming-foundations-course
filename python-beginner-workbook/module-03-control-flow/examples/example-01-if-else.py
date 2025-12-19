# example-01-if-else.py
# Demonstrates if/elif/else statements

# Get user's age
age = int(input("Enter your age: "))

# Check age and display appropriate message
if age >= 18:
    print("You are an adult.")
    print("You can vote and drive!")
elif age >= 13:
    print("You are a teenager.")
else:
    print("You are a child.")
    print("Enjoy being young!")

# Another example: Check if user can get discount
order_total = float(input("\nEnter order total: £"))

if order_total >= 100:
    print("🎉 You qualify for a discount!")
    discount = order_total * 0.10
    final_total = order_total - discount
    print(f"Discount: £{discount:.2f}")
    print(f"Final total: £{final_total:.2f}")
else:
    print(f"No discount. Total: £{order_total:.2f}")

