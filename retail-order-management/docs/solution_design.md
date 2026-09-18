# Solution Design

## Problem
Build a Retail Order Management System for a retail company.

## Users
Store employees who manage customers, products and orders.

## Business Entities
- Customer
- Product
- Order
- OrderItem

## Customer Types
- Regular
- Premium
- Corporate

## Business Rules
- Customer places orders
- Product stock decreases after purchase
- Different customer types receive different discounts
- Invalid quantity should be rejected

### What problem you are solving and who will use the application?
The retail company is currently managing customer orders manually. This can make it difficult to keep track of customers, products, stock and order amounts.

I am building a simple command-line application to make this process easier. The application will allow users to manage customers and products, create orders and calculate the final order amount based on the type of customer.

The application will mainly be used by retail staff or someone responsible for managing customer orders and products.
### What the user needs to do.
The user should be able to:
- Create and manage customers.
- Create and maintain products.
- View available products and their stock.
- Add stock to a product.
- Create an order for a customer.
- Add one or more products to an order.

### Important business entities and actions.
The main business entities I identified are:

#### Customer

A customer places orders and has a particular customer type.

#### Product

A product is something that the company sells. It has a price and available stock.

#### Order

An order belongs to a customer and contains the products purchased by that customer.

#### Order Item

An order item represents a particular product and the quantity purchased.

#### Important Actions

Some important actions in the application are:

- Create customer
- Create product
- Add stock
- Check product availability
- Create order
- Add product to order
- Calculate subtotal
- Calculate discount
- Calculate final total
- Update stock
### Candidate classes and why they deserve to be classes.

I identified four main business classes:

#### Customer

Customer is a separate class because each customer has their own identity and information such as customer ID, name, email and customer type.

#### Product

Product is a separate class because each product has its own identity, price and stock. It also needs behaviour such as checking and updating stock.

#### Order

Order is a separate class because an order has its own order ID, customer, status and list of items. It is responsible for managing the items in an order and calculating the order amount.

#### OrderItem

OrderItem is a separate class because an order can contain multiple products and different quantities. It connects a product with the quantity purchased.

### Attributes and behaviours for each class.

#### Customer

Attributes:
- customer_id
- name
- email

Behaviours:
- Display customer information
- Provide customer-specific discount behaviour

#### RegularCustomer

Attributes:
- Inherits common customer attributes

Behaviours:
- Provides the regular customer discount

#### PremiumCustomer

Attributes:
- Inherits common customer attributes

Behaviours:
- Provides the premium customer discount

#### CorporateCustomer

Attributes:
- Inherits common customer attributes

Behaviours:
- Provides the corporate customer discount

#### Product

Attributes:
- product_id
- name
- price
- stock

Behaviours:
- Display product information
- Reduce stock
- Validate price and stock

#### OrderItem

Attributes:
- product
- quantity

Behaviours:
- Calculate item subtotal
- Display item information
- Validate quantity

#### Order

Attributes:
- order_id
- customer
- status
- items

Behaviours:
- Add items to an order
- Calculate subtotal
- Calculate discount
- Calculate final total
- Display order information

### Encapsulation decisions and validation rules.
I will use validation to prevent invalid data from entering the objects.

The Product class will validate:
- Price should not be negative.
- Stock should not be negative.
- Stock should be reduced only when enough stock is available.

The OrderItem class will validate:
- Quantity should be greater than zero.
- Quantity should not be greater than the available product stock.

The customer type should be one of:
- Regular
- Premium
- Corporate

These validations help prevent the objects from entering an invalid state.

### Inheritance decisions and why they make sense.
I decided to use Customer as the parent class because all customer types have common information such as customer ID, name and email.

The customer hierarchy will be:

Customer
├── RegularCustomer
├── PremiumCustomer
└── CorporateCustomer

RegularCustomer, PremiumCustomer and CorporateCustomer are specialized types of Customer.

Common customer information will be kept in the Customer class, while customer-specific behaviour will be implemented in the child classes.

This avoids repeating the same customer information and makes the design easier to extend.

### Polymorphism decisions and what behaviour changes.
Polymorphism will be used for calculating the customer discount.

The Customer class will define a common discount behaviour, and each customer type will provide its own implementation.

For example:

- RegularCustomer → 0% discount
- PremiumCustomer → 10% discount
- CorporateCustomer → 15% discount

The Order does not need to know the detailed discount rule for each customer type. It can ask the customer for the discount, and the appropriate customer class will provide the result.

This allows the same method to behave differently depending on the customer object.

### Business assumptions you made.
The following assumptions are made for this project:

- Each customer has a unique customer ID.
- Each product has a unique product ID.
- Product price cannot be negative.
- Product stock cannot be negative.
- Order quantity must be greater than zero.
- A customer cannot purchase more products than the available stock.
- Regular customers receive a 0% discount.
- Premium customers receive a 10% discount.
- Corporate customers receive a 15% discount.
- Stock is reduced when a product is successfully added to an order.
- An order can contain multiple order items.
- The application is command-line based.
- No external Python packages are required.

### Design changes you make while developing.

Initially, I considered storing the customer name directly inside the Order class. I changed this to store the Customer object instead so that the Order can access customer information and customer-specific behaviour.

Initially, I considered storing order items as dictionaries containing price and quantity. I changed this to use an OrderItem class because an order item is a separate business entity and should have its own data and behaviour.

Initially, discount logic was considered inside the Customer class using customer type conditions. This was changed to use separate customer types so that inheritance and polymorphism can be demonstrated.

### Problems you encounter and how you solve them.

#### Problem 1: Connecting Customer with Order

Initially, I stored only the customer name in the Order class. I changed the design to store the Customer object so that the Order can access the customer's information.

#### Problem 2: Representing products inside an order

Initially, I considered storing product information directly inside Order. I separated this responsibility into the OrderItem class, which stores the Product object and quantity.

#### Problem 3: Invalid quantity

A customer could enter zero or a negative quantity. I added validation to the OrderItem class so that invalid quantities are rejected.

#### Problem 4: Insufficient stock

A customer could request more products than are available. I added stock validation before reducing the product stock.
