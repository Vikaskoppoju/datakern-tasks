
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
 
