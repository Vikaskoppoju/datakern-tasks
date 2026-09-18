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
### Attributes and behaviours for each class.
### Encapsulation decisions and validation rules.
### Inheritance decisions and why they make sense.
### Polymorphism decisions and what behaviour changes.
### Business assumptions you made.
### Design changes you make while developing.
### Problems you encounter and how you solve them.
