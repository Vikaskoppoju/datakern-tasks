class Product:
    def __init__(self, product_id, name, price, stock):
        self.product_id = product_id
        self.name = name

        if price < 0:
            raise ValueError("Price cannot be negative")

        if stock < 0:
            raise ValueError("Stock cannot be negative")

        self._price = price
        self._stock = stock

    @property
    def price(self):
        return self._price

    @property
    def stock(self):
        return self._stock

    def increase_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        self._stock += quantity

    def decrease_stock(self, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")

        if quantity > self._stock:
            raise ValueError("Insufficient stock")

        self._stock -= quantity