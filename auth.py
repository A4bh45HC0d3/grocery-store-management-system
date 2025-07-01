import json

def load_users():
    with open("data/users.json", "r") as file:
        return json.load(file)

def login():
    users = load_users()
    username = input("Enter username: ")
    password = input("Enter password: ")

    for user in users:
        if user["username"] == username and user["password"] == password:
            print(f"\n✅ Login successful as {user['role']}")
            return user["role"]
    print("\n❌ Login failed. Try again.")
    return None
