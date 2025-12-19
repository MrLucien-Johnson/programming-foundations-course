# example-03-calculations.py
# Demonstrates calculations and f-string formatting

# Get order details from user
item_name = input("Enter item name: ")
base_price = float(input("Enter base price: £"))
quantity = int(input("Enter quantity: "))

# Calculate subtotal
subtotal = base_price * quantity

# Calculate VAT (20%)
vat_rate = 0.20
vat_amount = subtotal * vat_rate

# Calculate total
total = subtotal + vat_amount

# Display formatted order summary
print("\n=== Order Summary ===")
print(f"Item: {item_name}")
print(f"Base Price: £{base_price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: £{subtotal:.2f}")
print(f"VAT (20%): £{vat_amount:.2f}")
print(f"{'='*25}")
print(f"Total: £{total:.2f}")

