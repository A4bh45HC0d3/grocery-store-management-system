import json
from collections import defaultdict

SALES_FILE = "data/sales.json"

def load_sales():
    with open(SALES_FILE, "r") as file:
        return json.load(file)

def generate_report():
    sales = load_sales()
    if not sales:
        print("\n📭 No sales data available.\n")
        return

    total_revenue = 0
    product_counter = defaultdict(int)

    print("\n--- All Sales ---")
    for sale in sales:
        print(f"🕒 {sale['date']}")
        for item in sale['items']:
            print(f"   {item['name']} x {item['quantity']} = Rs.{item['total']}")
            product_counter[item['name']] += item['quantity']
        print(f"   🧾 Total: Rs.{sale['total']}\n")
        total_revenue += sale["total"]

    print("\n📊 Summary Report")
    print(f"🧮 Total Sales: {len(sales)}")
    print(f"💰 Total Revenue: Rs.{total_revenue}")

    # Top 3 selling products
    print("\n🏆 Top Selling Products:")
    sorted_products = sorted(product_counter.items(), key=lambda x: x[1], reverse=True)
    for i, (name, qty) in enumerate(sorted_products[:3], start=1):
        print(f"{i}. {name} — {qty} sold")
