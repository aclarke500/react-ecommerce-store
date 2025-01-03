import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

# Load the data
df = pd.read_csv('data/product_embeddings_text-embedding-3-large.csv')
print(df.head())
print(df['id'])

# Function to retrieve embeddings as numpy arrays
def get_embedding_by_id(df, id):
    embedding_str = df.loc[df['id'] == id, 'embedding'].values[0]
    embedding_array = np.fromstring(embedding_str.strip('[]'), sep=',')
    return embedding_array

# Get embeddings by ID
v1 = get_embedding_by_id(df, 8)
v2 = get_embedding_by_id(df, 9)
v3 = get_embedding_by_id(df, 7)

# Stack the vectors into a matrix
vectors = np.vstack([v1, v2, v3])

# Compute the cosine similarity matrix
cosine_sim_matrix = cosine_similarity(vectors)

print("Cosine similarity matrix:")
print(cosine_sim_matrix)
