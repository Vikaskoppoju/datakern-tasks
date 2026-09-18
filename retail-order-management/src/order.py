class Order:
    def __init__(self, order_id, customer, status="Pending"):
        self.order_id = order_id
        self.customer = customer
        self.status = status
        self.items = []

    def add_item(self, item):
        item.product.reduce_stock(item.quantity)
        self.items.append(item)

    def calculate_subtotal(self):
        return sum(item.calculate_subtotal() for item in self.items)

    def calculate_discount(self):
        subtotal = self.calculate_subtotal()
        discount_percentage = self.customer.get_discount()

        return subtotal * discount_percentage / 100

    def calculate_total(self):
        subtotal = self.calculate_subtotal()
        discount = self.calculate_discount()

        return subtotal - discount

    def display_info(self):
        print(f"Order ID: {self.order_id}")
        print(f"Customer: {self.customer.name}")
        print(f"Customer Type: {self.customer.__class__.__name__}")
        print(f"Status: {self.status}")

        print("----------------------------------------")

        for item in self.items:
            item.display_info()

        print("----------------------------------------")
        print(f"Subtotal: ₹{self.calculate_subtotal():.2f}")
        print(f"Discount: ₹{self.calculate_discount():.2f}")
        print(f"Final Total: ₹{self.calculate_total():.2f}")