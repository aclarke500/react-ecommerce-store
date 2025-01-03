import lancedb
from build_database.product_meta_data import ProductMetaData
from build_database.vector_db_utils import create_vector_schema
import os
from dotenv import load_dotenv
# from sentence_transformers import SentenceTransformer



import psutil

def print_memory_usage(label=""):
    process = psutil.Process()
    mem_info = process.memory_info().rss / (1024 * 1024)  # in MB
    print(f"Memory usage {label}: {mem_info:.2f} MB")

# Example usage
print_memory_usage("before importing sentence-transformers")
from sentence_transformers import SentenceTransformer
model = SentenceTransformer('paraphrase-MiniLM-L3-v2')
print_memory_usage("after importing sentence-transformers")


# adding import here to fail fast


def build_db():
    # connect to LanceDB
    db = lancedb.connect("./general_store_db") # we expect to run this file from root directory

    # # Drop pre-existing data
    # load_dotenv()

    # is_dev = os.getenv('ENV') == 'DEV'
    # if is_dev:
    #     print("Running in development mode")
    #     for table_name in db.table_names():
    #         db.drop_table(table_name)

    food_meta_data = ProductMetaData['food']
    pet_meta_data = ProductMetaData['pet']
    electronics_meta_data = ProductMetaData['electronics']

    food_vector_schema = create_vector_schema(food_meta_data)
    pet_vector_schema = create_vector_schema(pet_meta_data)
    electronics_vector_schema = create_vector_schema(electronics_meta_data)

    # # # Create tables
    # db.create_table("food", data=food_vector_schema)
    # db.create_table("electronics", data=electronics_vector_schema)
    # db.create_table("pet_supplies", data=pet_vector_schema)

    # print("Database created successfully!")