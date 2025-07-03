from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

products = [
    {"id": 1, "name": "Milk", "quantity": 10, "price": 2.5},
    {"id": 2, "name": "Bread", "quantity": 20, "price": 1.5},
]

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Get product by id
@app.route('/products/<int:id>', methods=['GET'])
def get_product(id):
    product = next((item for item in products if item["id"] == id), None)
    if product:
        return jsonify(product)
    return jsonify({"error": "Product not found"}), 404

# Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    new_product = {
        "id": products[-1]["id"] + 1 if products else 1,
        "name": data["name"],
        "quantity": data["quantity"],
        "price": data["price"]
    }
    products.append(new_product)
    return jsonify(new_product), 201

# Update a product
@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    data = request.json
    product = next((item for item in products if item["id"] == id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404
    product.update({
        "name": data.get("name", product["name"]),
        "quantity": data.get("quantity", product["quantity"]),
        "price": data.get("price", product["price"])
    })
    return jsonify(product)

# Delete a product
@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    global products
    products = [item for item in products if item["id"] != id]
    return jsonify({"message": "Product deleted"}), 200

@app.route('/')
def home():
    return jsonify({"message": "Welcome to the Grocery Backend API!"})

if __name__ == '__main__':
    app.run(debug=True)
