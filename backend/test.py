import json
from typing import List
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import random

# Path to the JSON file
# file_path = './data.json'

# # Read the JSON file
# with open(file_path, 'r') as file:
#     data = json.load(file)

def get_random_products(data: dict, n: int = 25) -> List[dict]:
    """
    Get n random products from the data.
    :param data: The data to search.
    :param n: The number of random products to return.
    :return: A list of n random products.
    """
    return random.sample(data, n)


def get_product_from_id(id: int, data: dict) -> dict:
    """
    Get the product from the ID.
    :param id: The ID of the product.
    :param data: The data to search.
    :return: The product if found, otherwise None.
    """
    for product in data:
        if product['id'] == id:
            return product
    return None

def get_top_n_products(embedding: List[float], data: dict, n: int) -> List[int]:
    """
    Get the top n product IDs based on cosine similarity to the given embedding.
    :param embedding: The vector embedding to compare.
    :param data: The data to search.
    :param n: The number of top products to return.
    :return: A list of top n product IDs.
    """
    similarities = []
    for product in data:
        product_embedding = product['embedding']
        similarity = cosine_similarity([embedding], [product_embedding])[0][0]
        similarities.append((product['id'], similarity))
    
    # Sort by similarity in descending order and get the top n product IDs
    similarities.sort(key=lambda x: x[1], reverse=True)
    top_n_products = [product_id for product_id, _ in similarities[:n]]
    
    return top_n_products
# Print the data to verify
# print(data)