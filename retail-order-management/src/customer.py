class Customer:
    def __init__(self, customer_id, name, email):
        self.customer_id = customer_id
        self.name = name
        self.email = email

    def display_info(self):
        print(f"Customer ID: {self.customer_id}")
        print(f"Name: {self.name}")
        print(f"Email: {self.email}")

    def get_discount(self):
        return 0


class RegularCustomer(Customer):
    def get_discount(self):
        return 0


class PremiumCustomer(Customer):
    def get_discount(self):
        return 10


class CorporateCustomer(Customer):
    def get_discount(self):
        return 15