from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample data for products and orders (you'll replace this with your database)
products = [
    {"id": 1, "name": "Product 1", "description": "Description 1", "price": 10.0, "category": "Category 1", "stock": 100},
    {"id": 2, "name": "Product 2", "description": "Description 2", "price": 20.0, "category": "Category 2", "stock": 50}
]

orders = []




# Routes for managing products
@app.route('/products', methods=['GET']) #WORKING
def get_products():
    return jsonify(products)

@app.route('/products/<int:product_id>', methods=['GET'])#WORKING
def get_product(product_id):
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404

@app.route('/products', methods=['POST'])
def add_product():
    data = request.json
    products.append(data)
    return jsonify(data), 201

@app.route('/products/<int:product_id>', methods=['PUT']) #WORKING
def update_product(product_id):
    data = request.json
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        product.update(data)
        return jsonify(product)
    else:
        return jsonify({"error": "Product not found"}), 404

@app.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    global products
    products = [p for p in products if p['id'] != product_id]
    return jsonify({"message": "Product deleted"}), 200

# Routes for managing orders
@app.route('/orders', methods=['POST'])
def create_order():
    data = request.json
    orders.append(data)
    return jsonify(data), 201

@app.route('/orders/<int:user_id>', methods=['GET'])
def get_user_orders(user_id):
    user_orders = [order for order in orders if order.get('user_id') == user_id]
    return jsonify(user_orders)

# Routes for managing the shopping cart
@app.route('/cart/<int:user_id>', methods=['POST'])
def add_to_cart(user_id):
    data = request.json
    # Implement logic to add product to user's shopping cart
    return jsonify(data), 200

@app.route('/cart/<int:user_id>', methods=['GET'])
def get_cart(user_id):
    # Implement logic to retrieve user's shopping cart
    return jsonify({"message": "Get user's shopping cart"}), 200

@app.route('/cart/<int:user_id>/item/<int:product_id>', methods=['DELETE'])
def remove_from_cart(user_id, product_id):
    # Implement logic to remove product from user's shopping cart
    return jsonify({"message": "Remove item from user's shopping cart"}), 200

if __name__ == '__main__':
    app.run(debug=True)
