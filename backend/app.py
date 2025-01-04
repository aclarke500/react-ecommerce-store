from flask import Flask, request, jsonify, send_file
import lancedb
from utils.query_utils import query_db, query_LLM
from utils.intro import display_ascii_art
import pandas as pd
from flask_cors import CORS
import random
import os
from build_database.build_vector_db import build # just this line will build the lance db

# Initialize Flask app
app = Flask(__name__)

# Connect to LanceDB



CORS(app, resources={r"/*": {"origins": "*"}})

# Display ASCII art at startup
display_ascii_art()
@app.route('/query', methods=['POST'])
def query():
    # db = lancedb.connect("./general_store_db")
    try:
        # Get the JSON input from the request
        user_input = request.json.get('query', '')
        if not user_input:
            return jsonify({"error": "Query is required"}), 400

        # Call the LLM and query the database
        response = query_LLM(user_input)
        results = query_db(response, db)  # This might return a DataFrame or ndarray
        ret_val = []
        for index, row in results.head(15).iterrows():
            obj = {
                "price": row['price'],
                "id":row['id'],
                "name":row['name'],
                "description":row['description'],
                "quantity":row['quantity'],
                "availability":row['availability']
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
    print('opening db')
    # db = lancedb.connect("./general_store_db")
    try:
        # Get all table names in the database
        print('entered')
        table_names = db.table_names()
        print('table_names',table_names)
        for name in table_names:
            product = get_item_from_table(name, product_id, db)
            if product:
                return jsonify(product), 200
        raise ValueError(f'Item with id {product_id} not found in these tables: {table_names}')

    except Exception as e:
        print('error',e)
        return jsonify({"error": str(e)}), 500



IMAGE_DIR = "photos"
# Valid range for product images

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


@app.route('/products', methods=['GET'])
def get_all_products():
    try:
        all_products = []
        # Get all table names in the database
        table_names = db.table_names()
        for name in table_names:
            table = db.open_table(name)
            df = table.to_pandas()
            for _, row in df.iterrows():
                product = row_to_product(row, name)
                all_products.append(product)
        return jsonify(all_products), 200

    except Exception as e:
        return jsonify({"error": str(e)}), 500
# Run the Flask app
if __name__ == "__main__":
    print("Building LanceDB...")
    build()
    # Run the Flask app
    print("Starting Flask app...")
    port = int(os.environ.get("PORT", 10000)) # Use the PORT environment variable if it exists
    print(f"Starting server on 0.0.0.0:{port}...")
    debug_mode = os.environ.get("DEV", "false").lower() == "true"
    if debug_mode:
        print("Running in debug mode")
        port = 5001
    app.run(host="0.0.0.0", port=port, debug=debug_mode)
