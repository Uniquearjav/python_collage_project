"""
Features:
- Separate Admin and Customer menus
- Password-protected Admin section
- Admin can add, delete and modify products
- Admin can view customer order history
- Customers can view, search and filter products
- Shopping cart with remove and checkout options
- Payment selection: COD, UPI Demo, Card Demo

Default admin password: admin123

Note: Data is stored in Python lists and dictionaries in memory.
Products and order history reset when the program is closed.
"""

ADMIN_PASSWORD = "admin123"

products = [
    {"id": 1, "name": "Notebook", "category": "Stationery", "price": 60.0, "stock": 30},
    {"id": 2, "name": "Ball Pen", "category": "Stationery", "price": 10.0, "stock": 100},
    {"id": 3, "name": "Water Bottle", "category": "Accessories", "price": 180.0, "stock": 20},
    {"id": 4, "name": "Headphones", "category": "Electronics", "price": 799.0, "stock": 12},
    {"id": 5, "name": "USB Cable", "category": "Electronics", "price": 149.0, "stock": 25}
]

orders = []
next_product_id = 6
next_order_id = 1


def line():
    print("-" * 70)


def pause():
    input("\nPress Enter to continue...")


def read_integer(message, minimum=0):
    while True:
        try:
            number = int(input(message))
            if number < minimum:
                print("Please enter a valid number.")
            else:
                return number
        except ValueError:
            print("Please enter a whole number.")


def read_price(message):
    while True:
        try:
            price = float(input(message))
            if price < 0:
                print("Price cannot be negative.")
            else:
                return round(price, 2)
        except ValueError:
            print("Please enter a valid price.")


def find_product(product_id):
    for product in products:
        if product["id"] == product_id:
            return product
    return None


def display_products(product_list):
    if not product_list:
        print("\nNo products found.")
        return

    line()
    print(f"{'ID':<6}{'NAME':<22}{'CATEGORY':<17}{'PRICE':<13}{'STOCK':<8}")
    line()

    for product in product_list:
        print(
            f"{product['id']:<6}"
            f"{product['name']:<22}"
            f"{product['category']:<17}"
            f"Rs.{product['price']:<10.2f}"
            f"{product['stock']:<8}"
        )

    line()


# ============================ ADMIN SECTION ============================

def admin_login():
    print("\nADMIN LOGIN")
    line()
    password = input("Enter admin password: ")

    if password == ADMIN_PASSWORD:
        print("Login successful!")
        return True
    else:
        print("Incorrect password!")
        return False


def add_product():
    global next_product_id

    print("\nADD NEW PRODUCT")
    line()

    name = input("Enter product name: ").strip()
    if name == "":
        print("Product name cannot be empty.")
        return

    category = input("Enter category: ").strip()
    if category == "":
        print("Category cannot be empty.")
        return

    price = read_price("Enter price: Rs.")
    stock = read_integer("Enter available stock: ", 0)

    product = {
        "id": next_product_id,
        "name": name,
        "category": category,
        "price": price,
        "stock": stock
    }

    products.append(product)
    next_product_id += 1

    print("Product added successfully!")


def delete_product():
    print("\nDELETE PRODUCT")
    display_products(products)

    if not products:
        return

    product_id = read_integer("Enter product ID to delete: ", 1)
    product = find_product(product_id)

    if product is None:
        print("Product not found.")
    else:
        confirm = input("Are you sure you want to delete it? (y/n): ").lower()

        if confirm == "y":
            products.remove(product)
            print("Product deleted successfully.")
        else:
            print("Deletion cancelled.")


def modify_product():
    print("\nMODIFY PRODUCT")
    display_products(products)

    if not products:
        return

    product_id = read_integer("Enter product ID to modify: ", 1)
    product = find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    print("\nEnter new details. Press Enter to keep the old value.")

    name = input("New name [" + product["name"] + "]: ").strip()
    category = input("New category [" + product["category"] + "]: ").strip()
    price = input("New price [" + str(product["price"]) + "]: ").strip()
    stock = input("New stock [" + str(product["stock"]) + "]: ").strip()

    if name:
        product["name"] = name

    if category:
        product["category"] = category

    if price:
        try:
            new_price = float(price)
            if new_price >= 0:
                product["price"] = round(new_price, 2)
            else:
                print("Invalid price. Old price retained.")
        except ValueError:
            print("Invalid price. Old price retained.")

    if stock:
        try:
            new_stock = int(stock)
            if new_stock >= 0:
                product["stock"] = new_stock
            else:
                print("Invalid stock. Old stock retained.")
        except ValueError:
            print("Invalid stock. Old stock retained.")

    print("Product modified successfully!")


def view_order_history():
    print("\nCUSTOMER ORDER HISTORY")
    line()

    if not orders:
        print("No orders have been placed yet.")
        return

    for order in orders:
        print("\nOrder ID:", order["order_id"])
        print("Customer:", order["customer"])
        print("Mobile Number:", order["mobile"])
        print("Delivery Address:", order["address"])
        print("Payment Mode:", order["payment"])
        print("Total Amount: Rs.", format(order["total"], ".2f"))
        print("Order Status:", order["status"])
        print("Items:")

        for item in order["items"]:
            print(
                "  ", item["name"],
                " x ", item["quantity"],
                " = Rs.", format(item["subtotal"], ".2f")
            )

        line()


def admin_menu():
    if not admin_login():
        return

    while True:
        print("\n========== ADMIN MENU ==========")
        print("1. View Products")
        print("2. Add Product")
        print("3. Delete Product")
        print("4. Modify Product")
        print("5. View Customer Order History")
        print("6. Logout")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_products(products)
            pause()
        elif choice == "2":
            add_product()
            pause()
        elif choice == "3":
            delete_product()
            pause()
        elif choice == "4":
            modify_product()
            pause()
        elif choice == "5":
            view_order_history()
            pause()
        elif choice == "6":
            print("Admin logged out.")
            break
        else:
            print("Invalid choice. Please select 1-6.")


# ========================== CUSTOMER SECTION ===========================

def search_products():
    keyword = input("Enter product name or category to search: ").lower()

    result = []
    for product in products:
        if (keyword in product["name"].lower()
                or keyword in product["category"].lower()):
            result.append(product)

    print("\nSEARCH RESULTS")
    display_products(result)


def filter_products():
    print("\nFILTER PRODUCTS")
    print("1. Filter by Category")
    print("2. Filter by Maximum Price")
    print("3. Filter by Minimum Stock")

    choice = input("Choose filter: ")
    result = []

    if choice == "1":
        category = input("Enter category: ").lower()

        for product in products:
            if product["category"].lower() == category:
                result.append(product)

    elif choice == "2":
        maximum_price = read_price("Enter maximum price: Rs.")

        for product in products:
            if product["price"] <= maximum_price:
                result.append(product)

    elif choice == "3":
        minimum_stock = read_integer("Enter minimum stock: ", 0)

        for product in products:
            if product["stock"] >= minimum_stock:
                result.append(product)

    else:
        print("Invalid filter choice.")
        return

    print("\nFILTERED PRODUCTS")
    display_products(result)


def add_to_cart(cart):
    display_products(products)

    if not products:
        return

    product_id = read_integer("Enter product ID: ", 1)
    product = find_product(product_id)

    if product is None:
        print("Product not found.")
        return

    if product["stock"] == 0:
        print("Product is out of stock.")
        return

    quantity = read_integer("Enter quantity: ", 1)
    current_quantity = cart.get(product_id, 0)

    if current_quantity + quantity > product["stock"]:
        print("Not enough stock available.")
        return

    cart[product_id] = current_quantity + quantity
    print("Product added to cart successfully!")


def view_cart(cart):
    print("\nYOUR SHOPPING CART")
    line()

    if not cart:
        print("Your cart is empty.")
        return 0

    total = 0

    print(f"{'PRODUCT':<22}{'QUANTITY':<12}{'PRICE':<13}{'SUBTOTAL':<13}")
    line()

    for product_id in cart:
        product = find_product(product_id)

        if product is not None:
            quantity = cart[product_id]
            subtotal = product["price"] * quantity
            total += subtotal

            print(
                f"{product['name']:<22}"
                f"{quantity:<12}"
                f"{product['price']:<13.2f}"
                f"{subtotal:<13.2f}"
            )

    line()
    print("TOTAL AMOUNT: Rs.", format(total, ".2f"))
    return total


def remove_from_cart(cart):
    if not cart:
        print("Your cart is empty.")
        return

    view_cart(cart)

    product_id = read_integer("Enter product ID to remove: ", 1)

    if product_id in cart:
        del cart[product_id]
        print("Product removed from cart.")
    else:
        print("Product not found in cart.")


def checkout(cart, customer_name):
    global next_order_id

    total = view_cart(cart)

    if not cart:
        return

    # Check stock again before placing the order.
    for product_id in cart:
        product = find_product(product_id)

        if product is None or cart[product_id] > product["stock"]:
            print("Insufficient stock. Please update your cart.")
            return

    # Collect and validate the customer's mobile number.
    while True:
        mobile = input("\nEnter your 10-digit mobile number: ").strip()

        if len(mobile) == 10 and mobile.isdigit() and mobile[0] in "6789":
            break
        else:
            print("Invalid mobile number. Enter a valid 10-digit Indian mobile number.")

    # Collect the delivery address.
    while True:
        address = input("Enter your complete delivery address: ").strip()

        if address:
            break
        else:
            print("Delivery address cannot be empty.")

    print("\nSELECT MODE OF PAYMENT")
    print("1. Cash on Delivery")
    print("2. UPI (Demo)")
    print("3. Debit/Credit Card (Demo)")

    choice = input("Select payment mode: ")

    if choice == "1":
        payment = "Cash on Delivery"
    elif choice == "2":
        payment = "UPI (Demo)"
        print("Demo payment selected. No real transaction will occur.")
    elif choice == "3":
        payment = "Debit/Credit Card (Demo)"
        print("Demo payment selected. No real transaction will occur.")
    else:
        print("Invalid payment option.")
        return

    # Show all details before final confirmation.
    print("\n========== ORDER DETAILS ==========")
    print("Customer:", customer_name)
    print("Mobile Number:", mobile)
    print("Delivery Address:", address)
    print("Payment Mode:", payment)
    print("Total Amount: Rs.", format(total, ".2f"))

    confirm = input("\nConfirm your order? (y/n): ").lower()

    if confirm != "y":
        print("Order cancelled. Your cart is unchanged.")
        return

    order_items = []

    for product_id in cart:
        product = find_product(product_id)
        quantity = cart[product_id]
        subtotal = product["price"] * quantity

        order_items.append({
            "name": product["name"],
            "quantity": quantity,
            "subtotal": subtotal
        })

        product["stock"] -= quantity

    order = {
        "order_id": next_order_id,
        "customer": customer_name,
        "mobile": mobile,
        "address": address,
        "items": order_items,
        "total": total,
        "payment": payment,
        "status": "Placed"
    }

    orders.append(order)
    next_order_id += 1
    cart.clear()

    print("\nORDER PLACED SUCCESSFULLY!")
    print("Order ID:", order["order_id"])
    print("Customer:", customer_name)
    print("Mobile Number:", mobile)
    print("Payment Mode:", payment)
    print("Total Amount: Rs.", format(total, ".2f"))


def customer_menu():
    customer_name = input("\nEnter your name: ").strip()

    if customer_name == "":
        print("Name cannot be empty.")
        return

    cart = {}

    while True:
        print("\n========== CUSTOMER MENU ==========")
        print("1. View All Products")
        print("2. Search Products")
        print("3. Filter Products")
        print("4. Add Product to Cart")
        print("5. View Cart")
        print("6. Remove Product from Cart")
        print("7. Order Now / Checkout")
        print("8. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            display_products(products)
            pause()
        elif choice == "2":
            search_products()
            pause()
        elif choice == "3":
            filter_products()
            pause()
        elif choice == "4":
            add_to_cart(cart)
            pause()
        elif choice == "5":
            view_cart(cart)
            pause()
        elif choice == "6":
            remove_from_cart(cart)
            pause()
        elif choice == "7":
            checkout(cart, customer_name)
            pause()
        elif choice == "8":
            print("Thank you for visiting!")
            break
        else:
            print("Invalid choice. Please select 1-8.")


# =============================== MAIN ===================================

def main():
    while True:
        print("\n" + "=" * 70)
        print("             PYTHON SHOPPING MANAGEMENT SYSTEM")
        print("=" * 70)
        print("1. Admin")
        print("2. Customer")
        print("3. Exit")

        choice = input("Select your option: ")

        if choice == "1":
            admin_menu()
        elif choice == "2":
            customer_menu()
        elif choice == "3":
            print("Thank you for using the Shopping Management System.")
            break
        else:
            print("Invalid choice. Please select 1, 2 or 3.")

main()
