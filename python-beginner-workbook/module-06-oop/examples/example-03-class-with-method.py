# example-03-class-with-method.py
# Demonstrates class with methods

class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    
    def display(self):
        print(f"Customer: {self.name}")
        print(f"Email: {self.email}")
    
    def update_email(self, new_email):
        self.email = new_email

# Create customer
customer = Customer("Sarah", "sarah@example.com")
customer.display()

customer.update_email("sarah.new@example.com")
customer.display()

