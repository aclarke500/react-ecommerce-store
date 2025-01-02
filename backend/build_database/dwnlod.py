import pandas as pd
import requests
from PIL import Image
from io import BytesIO
import os

df = pd.read_csv('build_database/temp.csv')

if not os.path.exists('photos'):
    os.makedirs('photos')

for index, row in df.iterrows():
    img_url = row['product_img_url']
    product_id = row['product_id']
    try:
        response = requests.get(img_url)
        if response.status_code == 200:
            img = Image.open(BytesIO(response.content))
            img.save(f'photos/product_{product_id}.png')
            print(f'Saved image for product {product_id}')
        else:
            print(f'Failed to download image for product {product_id}')
    except Exception as e:
        print(f'Error downloading image for product {product_id}: {e}')