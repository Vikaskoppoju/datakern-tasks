class Order:
    def __init__(self, order_id, customer, status="Pending"):
        self.order_id = order_id
        self.customer = customer
        self.status = status
        self.items = []

    def add_item(self, item):
        self.items.append(item)

    def calculate_total(self):
        return sum(item.calculate_subtotal() for item in self.items)

    def display_info(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.customer.name}")
        print(f"Status: {self.status}")
        print(f"Total: ₹{self.calculate_total()}")