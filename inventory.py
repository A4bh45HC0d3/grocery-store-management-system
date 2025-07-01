import json

PRODUCTS_FILE = "data/products.json"

def load_products():
    with open(PRODUCTS_FILE, "r") as file:
        return json.load(file)

def save_products(products):
    with open(PRODUCTS_FILE, "w") as file:
        json.dump(products, file, indent=4)

def view_products():
    products = load_products()
    print("\n--- Product List ---")
    if not products:
        print("No products found.")
        return
    print("{:<5} {:<15} {:<10} {:<10}".format("ID", "Name", "Price", "Qty"))
    for p in products:
        print("{:<5} {:<15} {:<10} {:<10}".format(p["id"], p["name"], p["price"], p["quantity"]))

def add_product():
    products = load_products()
    name = input("Enter product name: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter quantity: "))

    # Auto-generate ID
    product_id = 1 if not products else products[-1]["id"] + 1

    products.append({
        "id": product_id,
        "name": name,
        "price": price,
        "quantity": quantity
    })
    save_products(products)
    print("✅ Product added successfully.")

def update_product():
    products = load_products()
    product_id = int(input("Enter product ID to update: "))
    for p in products:
        if p["id"] == product_id:
            print(f"Updating {p['name']}")
            p["price"] = float(input("New price: "))
            p["quantity"] = int(input("New quantity: "))
            save_products(products)
            print("✅ Product updated.")
            return
    print("❌ Product not found.")

def delete_product():
    products = load_products()
    product_id = int(input("Enter product ID to delete: "))
    products = [p for p in products if p["id"] != product_id]
    save_products(products)
    print("✅ Product deleted (if it existed).")

def inventory_menu():
    while True:
        print("\n--- Inventory Menu ---")
        print("1. View Products")
        print("2. Add Product")
        print("3. Update Product")
        print("4. Delete Product")
        print("5. Back to Main Menu")
        choice = input("Choose: ")

        if choice == "1":
            view_products()
        elif choice == "2":
            add_product()
        elif choice == "3":
            update_product()
        elif choice == "4":
            delete_product()
        elif choice == "5":
            break
        else:
            print("❌ Invalid option.")
