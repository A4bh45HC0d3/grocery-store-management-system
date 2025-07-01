import json
from datetime import datetime

PRODUCTS_FILE = "data/products.json"
SALES_FILE = "data/sales.json"

def load_products():
    with open(PRODUCTS_FILE, "r") as file:
        return json.load(file)

def save_products(products):
    with open(PRODUCTS_FILE, "w") as file:
        json.dump(products, file, indent=4)

def save_sale(sale):
    with open(SALES_FILE, "r") as file:
        sales = json.load(file)
    sales.append(sale)
    with open(SALES_FILE, "w") as file:
        json.dump(sales, file, indent=4)

def view_products():
    products = load_products()
    print("\n--- Available Products ---")
    print("{:<5} {:<15} {:<10} {:<10}".format("ID", "Name", "Price", "Qty"))
    for p in products:
        print("{:<5} {:<15} {:<10} {:<10}".format(p["id"], p["name"], p["price"], p["quantity"]))

def billing_menu():
    cart = []
    products = load_products()

    while True:
        view_products()
        try:
            product_id = int(input("Enter product ID to add to cart (0 to checkout): "))
        except ValueError:
            print("❌ Please enter a valid number.")
            continue

        if product_id == 0:
            break

        matching = next((p for p in products if p["id"] == product_id), None)
        if not matching:
            print("❌ Product not found.")
            continue

        try:
            qty = int(input(f"Enter quantity for {matching['name']}: "))
        except ValueError:
            print("❌ Enter a valid number.")
            continue

        if qty > matching["quantity"]:
            print(f"⚠️ Only {matching['quantity']} in stock.")
            continue

        cart.append({
            "id": matching["id"],
            "name": matching["name"],
            "price": matching["price"],
            "quantity": qty,
            "total": matching["price"] * qty
        })

        matching["quantity"] -= qty  # reduce stock

    if not cart:
        print("🛒 Cart is empty. Cancelled.")
        return

    # Checkout
    save_products(products)
    total_amount = sum(item["total"] for item in cart)
    print("\n--- Bill ---")
    for item in cart:
        print(f"{item['name']} x {item['quantity']} = Rs.{item['total']}")
    print(f"Total Amount: Rs.{total_amount}")

    # Save to sales.json
    sale = {
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "items": cart,
        "total": total_amount
    }
    save_sale(sale)
    print("✅ Sale saved. Thank you!")

    # Optional: Save receipt to text file
    receipt_file = f"receipt_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
    with open(f"receipts/{receipt_file}", "w") as file:
        file.write("GROCERY STORE BILL\n")
        file.write(f"Date: {sale['date']}\n\n")
        for item in cart:
            file.write(f"{item['name']} x {item['quantity']} = Rs.{item['total']}\n")
        file.write(f"\nTOTAL: Rs.{total_amount}\n")
    print(f"🧾 Receipt saved as: receipts/{receipt_file}")
