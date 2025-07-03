
from flask import Blueprint, jsonify, request

api_blueprint = Blueprint('api', __name__)

# Sample route
@api_blueprint.route('/items', methods=['GET'])
def get_items():
    # Sample data – Replace with real DB later
    items = [
        {"id": 1, "name": "Rice", "price": 100},
        {"id": 2, "name": "Milk", "price": 50},
    ]
    return jsonify(items)

# Route to add new item
@api_blueprint.route('/items', methods=['POST'])
def add_item():
    data = request.get_json()
    print("Received:", data)
    # Save to DB (not implemented yet)
    return jsonify({"message": "Item received", "data": data}), 201

