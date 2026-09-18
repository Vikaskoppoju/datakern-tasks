from customer import (
    RegularCustomer,
    PremiumCustomer,
    CorporateCustomer
)

from product import Product
from order import Order
from order_item import OrderItem


def main():

    print("===============================")
    print("   RETAIL ORDER MANAGEMENT")
    print("===============================")

    # -------------------------
    # CREATE CUSTOMER
    # -------------------------

    print("\n--- Create Customer ---")

    customer_id = int(input("Enter Customer ID: "))
    name = input("Enter Customer Name: ")
    email = input("Enter Customer Email: ")

    print("\nCustomer Types")
    print("1. Regular")
    print("2. Premium")
    print("3. Corporate")

    customer_choice = input("Choose customer type: ")

    if customer_choice == "1":
        customer = RegularCustomer(
            customer_id,
            name,
            email
        )

    elif customer_choice == "2":
        customer = PremiumCustomer(
            customer_id,
            name,
            email
        )

    elif customer_choice == "3":
        customer = CorporateCustomer(
            customer_id,
            name,
            email
        )

    else:
        print("Invalid customer type.")
        return

    print("\nCustomer created successfully!")

    # -------------------------
    # CREATE PRODUCTS
    # -------------------------

    products = {
        101: Product(101, "Laptop", 50000, 10),
        102: Product(102, "Mouse", 1000, 20),
        103: Product(103, "Keyboard", 2000, 15)
    }

    # -------------------------
    # CREATE ORDER
    # -------------------------

    print("\n--- Create Order ---")

    order_id = int(input("Enter Order ID: "))

    order = Order(order_id, customer)

    print("Order created successfully!")

    # -------------------------
    # ADD PRODUCTS
    # -------------------------

    while True:

        print("\n--- Available Products ---")

        for product in products.values():
            product.display_info()
            print("-------------------")

        product_id = int(
            input("Enter Product ID (0 to finish): ")
        )

        if product_id == 0:
            break

        if product_id not in products:
            print("Product not found.")
            continue

        product = products[product_id]

        try:
            quantity = int(
                input("Enter Quantity: ")
            )

            item = OrderItem(product, quantity)

            order.add_item(item)

            print("Product added successfully!")

        except ValueError as error:
            print(f"Error: {error}")

    # -------------------------
    # DISPLAY BILL
    # -------------------------

    print("\n========================================")
    print("              RETAIL BILL")
    print("========================================")

    order.display_info()

    print("========================================")
    print("       Thank you for shopping!")
    print("========================================")


if __name__ == "__main__":
    main()