from flask import Flask, request, jsonify, send_file
from utils.query_utils import query_db, query_LLM, get_random_products, get_product_from_id
from utils.intro import display_ascii_art
from flask_cors import CORS
import os
import json

# data is stored in a JSON file
# file_path = './data.json'
# with open(file_path, 'r') as file:
#     data = json.load(file)

categories = {
    'food':'./data/food_products.json',
    'electronics':'./data/electronics_products.json',
    'pet_supplies':'./data/pet_products.json'
}

app = Flask(__name__)

   

CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/query', methods=['POST'])
def query():
    try:

        user_input = request.json.get('query', '')
        if not user_input:
            return jsonify({"error": "Query is required"}), 400

        # Call the LLM and query the database
        response = query_LLM(user_input)
        results = query_db(response)  # array of dicts
        ret_val = []
        for row in results:
            obj = {
                "price": row['price'],
                "id":row['id'],
                "name":row['name'],
                "description":row['description'],
                "quantity":row['quantity'],
                "availability":row['availability'],
            }
            ret_val.append(obj)
        return jsonify(ret_val), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


def row_to_product(row, table_name) -> dict:
    obj = {
                "price": row['price'],
                "id":row['id'],
                "name":row['name'],
                "description":row['description'],
                "quantity":row['quantity'],
                "availability":row['availability'],
                "category":table_name,
            }
    return obj

@app.route('/', methods=['GET'])
def health_check():
    """
    Health check endpoint.
    """
    return jsonify({"message": "API is running"}), 200


def get_item_from_table(table_name, id, db) -> dict | None:
    table = db.open_table(table_name)
    df = table.to_pandas()

    for _, row in df.iterrows():
        if str(row['id']) == str(id):
            return row_to_product(row, table_name)
    
    return None


@app.route('/product/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    product_id = int(product_id)
    try:
        product = get_product_from_id(product_id)
        if product is None:
            return jsonify({"error": f"Product with id {product_id} not found"}), 404
        return jsonify(product), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
  



IMAGE_DIR = "photos"
@app.route('/product_image/<int:product_id>', methods=['GET'])
def serve_product_image(product_id):
    try:
        
        # Construct the file path
        file_path = os.path.join(IMAGE_DIR, f"product_{product_id}.png")
        
        # Check if the file exists
        if not os.path.isfile(file_path):
            return jsonify({"error": f"Image for product_id {product_id} not found"}), 404
        
        # Serve the file
        return send_file(file_path, mimetype='image/png')
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/test', methods=['GET'])
def test():
    return jsonify({"message": "Test endpoint is working"}), 200



def load_data(file_path):
    """Load JSON data from a file."""
    with open(file_path, 'r') as file:
        return json.load(file)

@app.route('/products', defaults={'category': None}, methods=['GET'])
@app.route('/products/<category>', methods=['GET'])
def get_all_products(category):
    try:
        if category:
            if category not in categories:
                return jsonify({"error": f"Category '{category}' not found"}), 404
            
            # Lazy load the category-specific JSON file
            data_table = load_data(categories[category])
            products = get_random_products(data_table, 25)
            return jsonify(products), 200

        # No category specified: Load and mix products from all categories
        pet_products = get_random_products(load_data(categories['pet_supplies']), 8)
        food_products = get_random_products(load_data(categories['food']), 8)
        electronics_products = get_random_products(load_data(categories['electronics']), 9)

        mixed_products = pet_products + food_products + electronics_products
        return jsonify(mixed_products), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Run the Flask app
if __name__ == "__main__":
    # Display ASCII art at startup
    display_ascii_art()

    print("Starting Flask app...")
    port = int(os.environ.get("PORT", 10000)) # Use the PORT environment variable if it exists
    print(f"Starting server on 0.0.0.0:{port}...")

    debug_mode = os.environ.get("DEV", "false").lower() == "true" # debug mode for dev
    if debug_mode:
        print("Running in debug mode")
        port = 5001
    app.run(host="0.0.0.0", port=port, debug=True)

