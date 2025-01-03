

from dotenv import load_dotenv
import pandas as pd
# Load environment variables from .env file
load_dotenv()
from openai import OpenAI
client = OpenAI()
from build_database.product_meta_data import ProductMetaData

open_ai_model = "text-embedding-3-large"

# products = [ {"id": 5, "name": "Cheddar Cheese", "category": "Dairy", "price": 4.99, "availability": True, "shelf_life": "2 Weeks", "description": "A block of sharp cheddar cheese.", "quantity": 40},
#     {"id": 6, "name": "Eggs", "category": "Dairy", "price": 3.49, "availability": True, "shelf_life": "2 Weeks", "description": "A dozen large, free-range eggs.", "quantity": 90},
#     {"id": 7, "name": "Ground Beef", "category": "Meat", "price": 7.99, "availability": True, "shelf_life": "3 Days", "description": "Lean ground beef for versatile cooking.", "quantity": 70},
#     {"id": 8, "name": "Carrots", "category": "Vegetable", "price": 1.99, "availability": True, "shelf_life": "2 Weeks", "description": "Crunchy, organic carrots.", "quantity": 100},
#     {"id": 9, "name": "Orange", "category": "Fruit", "price": 0.8, "availability": True, "shelf_life": "1 Week", "description": "A sweet, juicy orange packed with Vitamin C.", "quantity": 180},
#     # electronics
#     {"id":(80*2)+ 59, "name": "Portable Fan Heater", "category": "Home Appliances", "price": 49.99, "availability": True, "warranty_period": "1 Year", "description": "Compact fan heater with safety features.", "quantity": 60},
#     {"id":(80*2)+ 60, "name": "Graphic Tablet", "category": "Computers", "price": 299.99, "availability": True, "warranty_period": "1 Year", "description": "Graphic tablet with a pressure-sensitive stylus.", "quantity": 25},
#     {"id":(80*2)+ 61, "name": "High-Performance Laptop Cooler", "category": "Accessories", "price": 34.99, "availability": True, "warranty_period": "6 Months", "description": "Laptop cooling pad with silent fans.", "quantity": 80},
#     {"id":(80*2)+ 62, "name": "Wi-Fi Range Extender", "category": "Accessories", "price": 49.99, "availability": True, "warranty_period": "1 Year", "description": "Device to extend your Wi-Fi range seamlessly.", "quantity": 60},
#     {"id":(80*2)+ 63, "name": "Noise-Isolating Earbuds", "category": "Accessories", "price": 29.99, "availability": True, "warranty_period": "6 Months", "description": "Compact earbuds with noise-isolating technology.", "quantity": 100},
#     ]



# ProductMetaData = {
#     "food": food_meta_data,
#     "pet": pet_meta_data,
#     "electronics": electronics_meta_data
# }

products = []
for category in ProductMetaData.values():
    products.extend(category)



def get_embedding(text, model="text-embedding-3-small"):
    text = text.replace("\n", " ")
    return client.embeddings.create(input = [text], model=model).data[0].embedding

embedding_data = {
    "id": [],
    "embedding": []
}

for product in products:
    print(product)
    # embedding_data["id"].append(product["id"])
    # embedding_data["embedding"].append(get_embedding(product["description"], model=open_ai_model))


df = pd.DataFrame(embedding_data)
df.to_csv(f'data/product_embeddings_{open_ai_model}.csv', index=False)
