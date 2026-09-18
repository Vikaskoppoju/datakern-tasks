class OrderItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self):
        return self.product.price * self.quantity

    def display_info(self):
        print(f"Product: {self.product.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Subtotal: ₹{self.calculate_subtotal()}")