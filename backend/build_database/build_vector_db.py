import lancedb
from build_database.product_meta_data import ProductMetaData
from build_database.vector_db_utils import create_vector_schema


def build():
    # connect to LanceDB
    print("Connecting to LanceDB...")
    db = lancedb.connect("./general_store_db") # we expect to run this file from root directory
    print("Connected to LanceDB.")

    # Drop pre-existing data
    print("Dropping pre-existing tables...")
    for table_name in db.table_names():
        print(f"Dropping table: {table_name}")
        db.drop_table(table_name)
    print("Pre-existing tables dropped.")

    print("Fetching product metadata...")
    food_meta_data = ProductMetaData['food']
    pet_meta_data = ProductMetaData['pet']
    electronics_meta_data = ProductMetaData['electronics']
    print("Product metadata fetched.")

    print("Creating vector schemas...")
    food_vector_schema = create_vector_schema(food_meta_data)
    pet_vector_schema = create_vector_schema(pet_meta_data)
    electronics_vector_schema = create_vector_schema(electronics_meta_data)
    print("Vector schemas created.")

    # Create tables
    print("Creating tables...")
    db.create_table("food", data=food_vector_schema)
    print("Food table created.")
    db.create_table("electronics", data=electronics_vector_schema)
    print("Electronics table created.")
    db.create_table("pet_supplies", data=pet_vector_schema)
    print("Pet supplies table created.")

    print("Database created successfully!")