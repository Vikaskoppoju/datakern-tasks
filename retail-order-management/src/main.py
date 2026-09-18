from customer import Customer
from product import Product
from order import Order
from order_item import OrderItem

print("===============================")
print("RETAIL ORDER MANAGEMENT")
print("===============================")
print("1. Create Customer")
print("2. Create Product")
print("3. Create Order")
print("4. Add Product to Order")  
print("5. View Bill")
print("6. Exit")
print("Enter your choice:")
input_choice = input()
selected_choice = int(input_choice)

