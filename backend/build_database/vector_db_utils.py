from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd

# Load the SentenceTransformer model
model = SentenceTransformer('all-MPNet-base-v2')
temp_img_df = pd.read_csv('build_database/temp.csv')
def get_img_url(id):
    print("ahhh",temp_img_df.columns)
    url = temp_img_df.loc[temp_img_df[' product_id'] == id, 'product_img_url'].values
    if len(url) == 0: # If the image URL is not found, return a default image
        return "https://oaidalleapiprodscus.blob.core.windows.net/private/org-GMnbtRP4ficn3DyHiO8HT2Ou/user-uBxP2K66QnLbLi7g9cnyXmw2/img-TLEVdVMIcKMwa5xCaRAp0WCs.png?st=2025-01-02T01%3A52%3A04Z&se=2025-01-02T03%3A52%3A04Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-01-02T01%3A28%3A35Z&ske=2025-01-03T01%3A28%3A35Z&sks=b&skv=2024-08-04&sig=CIyBbjhvuKd1OcWdZ5AcTJDHFx3tWbsa%2BoWAI8of8ro%3D"
    return url[0]

def embed_item(item: dict) -> np.ndarray:
    """
    Embeds the description in the item using the SentenceTransformer model.

    Args:
        item (dict): The item data.

    Returns:  
        np.ndarray: The normalized embedding of the description.
    """
    description = item['description']   
    # Embed the description, convert it to vector of 768 in np array
    if not description:
        raise ValueError("Item must contain a 'description' field.")
    embedding = model.encode(description) 
    normalized_embedding = embedding / np.linalg.norm(embedding) # normalize the vector for more efficient comparison
    return normalized_embedding

def create_vector_schema(meta_data: list[dict]) -> list[dict]:
    """
    Embeds the description in the query using the SentenceTransformer model.

    Args:
        meta_data (list[dict]): The meta data for the database items.

    Returns:
        list[dict]: The vectorized schema of the database.
    """
    vector_schema = [] # list of dictionaries with meta data and vectorized description
    for item in meta_data:
        vector = embed_item(item)
        item['vector'] = vector
        img_url = get_img_url(item['id'])
        item['img_url'] = img_url
        vector_schema.append(item)
    return vector_schema 

