from flask import Flask, request, jsonify
import lancedb
from utils.query_utils import query_db, query_LLM
from utils.intro import display_ascii_art
import pandas as pd
from flask_cors import CORS

# Initialize Flask app
app = Flask(__name__)

# Connect to LanceDB
db = lancedb.connect("./general_store_db")


CORS(app)
# Display ASCII art at startup
display_ascii_art()
@app.route('/query', methods=['POST'])
def query():
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
        # # Convert DataFrame or ndarray to JSON serializable format
        # if isinstance(results, pd.DataFrame):
        #     json_results = results.to_dict(orient='records')  # Convert DataFrame to list of dicts
        # elif isinstance(results, np.ndarray):
        #     json_results = results.tolist()  # Convert ndarray to list
        # else:
        #     json_results = results  # Assume it's already serializable

        # return jsonify(json_results), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


def row_to_product(row) -> dict:
    obj = {
                "price": row['price'],
                "id":row['id'],
                "name":row['name'],
                "description":row['description'],
                "quantity":row['quantity'],
                "availability":row['availability']
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
        print(f"Processing ID: {row['id']}")
        if str(row['id']) == str(id):
            return row_to_product(row)
    
    return None


@app.route('/product/<product_id>', methods=['GET'])
def get_product_by_id(product_id):
    try:
        # Get all table names in the database
        table_names = db.table_names()
        for name in table_names:
            product = get_item_from_table(name, product_id, db)
            if product:
                return jsonify(product), 200
        raise ValueError(f'Item with id {product_id} not found in these tables: {table_names}')

        # # Iterate through each table and search for the product by ID
        # for table_name in table_names:
        #     table = db.table(table_name)
        #     result = table.query(f"SELECT * FROM {table_name} WHERE id = '{product_id}'")
        #     if not result.empty:
        #         product = result.iloc[0].to_dict()
        #         break

        # if product:
        #     return jsonify(product), 200
        # else:
        #     return jsonify({"error": "Product not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500
# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
