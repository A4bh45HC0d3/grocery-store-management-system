from auth import login
from inventory import inventory_menu
from billing import billing_menu
from reports import generate_report

def main():
    print("=== Welcome to Grocery Store Management System ===\n")
    role = login()

    if role == "admin":
        while True:
            print("\nAdmin Menu:")
            print("1. Inventory Management")
            print("2. View Sales Reports")
            print("3. Exit")
            choice = input("Choose: ")

            if choice == "1":
                inventory_menu()
            elif choice == "2":
                generate_report()
            elif choice == "3":
                break
            else:
                print("Invalid choice.")

    elif role == "cashier":
        while True:
            print("\nCashier Menu:")
            print("1. Billing")
            print("2. Exit")
            choice = input("Choose: ")

            if choice == "1":
                billing_menu()
            elif choice == "2":
                break
            else:
                print("Invalid choice.")

if __name__ == "__main__":
    main()
