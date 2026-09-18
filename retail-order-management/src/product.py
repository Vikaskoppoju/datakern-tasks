class Product:
    def __init__(self, product_id, name, price, stock):
        if price < 0:
            raise ValueError("Price cannot be negative")

        if stock < 0:
            raise ValueError("Stock cannot be negative")

        self.product_id = product_id
        self.name = name
        self.price = price
        self.stock = stock

    def display_info(self):
        print(f"Product ID: {self.product_id}")
        print(f"Name: {self.name}")
        print(f"Price: ₹{self.price}")
        print(f"Stock: {self.stock}")

    def reduce_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0")

        if quantity > self.stock:
            raise ValueError("Insufficient stock")

        self.stock -= quantity