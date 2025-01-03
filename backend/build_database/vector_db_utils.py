import numpy as np
import pandas as pd

embedding_df = pd.read_csv('data/product_embeddings_text-embedding-3-large.csv')


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
        id = item['id']
        vector = get_embedding_by_id(id)
        item['vector'] = vector
        vector_schema.append(item)
    return vector_schema 

def get_embedding_by_id(product_id):
    embedding_str = embedding_df.loc[embedding_df['id'] == product_id, 'embedding'].values[0]
    embedding_list = embedding_str.strip('[]').split(',')
    embedding_array = np.array([float(x) for x in embedding_list])
    normalized_embedding_array = embedding_array / np.linalg.norm(embedding_array)
    print(np.linalg.norm(normalized_embedding_array))
    return normalized_embedding_array
