# ## Customer

# Customer represents a customer who can place orders in the retail system.

# ### Attributes
# - customer_id
# - name
# - email
# - customer_type

# ### Behaviours
# - Store customer information
# - Display customer information

# ### Customer Types
# - Regular
# - Premium
# - Corporate

# ### Initial assumptions
# - Customer ID uniquely identifies a customer.
# - Customer type determines the customer's pricing/discount behaviour.
# - Discount rules will be implemented later.
class Customer:
    def __init__(self, customer_id,name, email, customer_type):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.customer_type = customer_type
    def display_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")
        print(f"Customer Type: {self.customer_type}")

Cus=Customer(1,"John Doe","john.doe@example.com","Premium")
Cus.display_info()
 
