class OrderItem:
    def __init__(self, product, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        if quantity > product.stock:
            raise ValueError("Quantity exceeds available stock")

        self.product = product
        self.quantity = quantity

    def calculate_subtotal(self):
        return self.product.price * self.quantity

    def display_info(self):
        print(f"Product: {self.product.name}")
        print(f"Quantity: {self.quantity}")
        print(f"Price: ₹{self.product.price}")
        print(f"Subtotal: ₹{self.calculate_subtotal()}")