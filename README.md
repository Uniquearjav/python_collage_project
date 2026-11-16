# Python Shopping Management System

**Academic Project**

## Submitted To

**Lachoo Memorial College, Jodhpur, Rajasthan**

## Project Developed By

| S. No. | Student Name |
|---|---|
| 1 | Arjav Choudhary |
| 2 | Arhaan Saadiq |
| 3 | Bhanu Pratap Singh |

**Class:** BCA J1  
**Semester:** 3rd Semester

---

## Project Introduction

The Python Shopping Management System is a menu-driven application developed using Python. It provides separate Admin and Customer sections to manage products, shopping carts, customer information, and orders.

The project demonstrates fundamental Python programming concepts through a practical shopping management application.

## Features

### Admin
- Password-protected admin login
- View all products
- Add new products
- Delete products
- Modify product details
- View customer order history
- View customer mobile numbers and delivery addresses

### Customer
- Enter customer name
- View all available products
- Search products by name or category
- Filter products by category
- Filter products by maximum price
- Filter products by minimum stock
- Add products to shopping cart
- View shopping cart
- Remove products from cart
- Checkout with mobile number and delivery address
- Select payment method

### Payment Methods
- Cash on Delivery (COD)
- UPI (Demo)
- Debit/Credit Card (Demo)

## Requirements

- Python 3.x
- No external libraries required
- No internet connection required

## Installation and Execution

1. Download or clone the project.
2. Open the project folder in terminal.
3. Run the following command:

```bash
python shopping_management_system.py
```

Alternatively:

```bash
python3 shopping_management_system.py
```

## Admin Login

Default Admin Password:

```text
admin123
```

You can change the password by modifying the `ADMIN_PASSWORD` variable in the Python source code.

## Sample Products

| ID | Product | Category | Price | Stock |
|---|---|---|---:|---:|
| 1 | Notebook | Stationery | ₹60 | 30 |
| 2 | Ball Pen | Stationery | ₹10 | 100 |
| 3 | Water Bottle | Accessories | ₹180 | 20 |
| 4 | Headphones | Electronics | ₹799 | 12 |
| 5 | USB Cable | Electronics | ₹149 | 25 |

## Checkout Process

During checkout, customers must provide:

1. Customer name
2. 10-digit Indian mobile number
3. Complete delivery address
4. Payment method
5. Order confirmation

The admin can view these details in the Customer Order History section.

## Project Structure

```text
Shopping-Management-System/
│
├── shopping_management_system.py
└── README.md
```

## Technologies and Concepts Used

- Python
- Lists
- Dictionaries
- Functions
- Conditional Statements
- Loops
- Exception Handling

## Important Notes

- The application uses Python lists and dictionaries for data storage.
- Product and order data are stored temporarily in memory.
- All data resets when the program is closed.
- UPI and Card payments are demo options only.
- No real payment transactions are processed.
- Mobile number validation checks the format but does not verify ownership.

---

## Acknowledgement

This project has been developed as part of the academic learning activities of **BCA J1, 3rd Semester, Lachoo Memorial College, Jodhpur**.

**Project Contributors:**
- Arjav Choudhary
- Arhaan Saadiq
- Bhanu Pratap Singh

**Institution:** Lachoo Memorial College, Jodhpur, Rajasthan.
