from openai import OpenAI
import os
from dotenv import load_dotenv
import pandas as pd
import time  # For potential delay between API calls
from product_meta_data import ProductMetaData

# Load API key
load_dotenv()
api_key = os.getenv('open_ai_key')
client = OpenAI(api_key=api_key)

def get_img_url(name: str, description: str) -> str:
    """
    Generate an image URL using the OpenAI API based on the product's name and description.
    """
    try:
        prompt = (
            f"You are generating product images for an e-commerce store. "
            f"Create a realistic image for the product titled '{name}', with the following description: '{description}'. "
            f"The image should be professional, visually appealing, and suitable for display on an e-commerce platform like Walmart or Amazon."
        )
        response = client.images.generate(
            model="dall-e-3",
            prompt=prompt,
            quality="standard",
            n=1,
        )
        return response.data[0].url
    except Exception as e:
        print(f"Error generating image for {name}: {e}")
        return None

def build_urls(products: list[dict]):
    """
    Generate image URLs for a list of products and save them to a CSV file.
    """
    product_ids = []
    product_img_urls = []
    
    for p in products:
        try:
            if int(p['id']) <= 228:
                continue
            product_ids.append(p['id'])
            p_name = p['name']
            p_description = p['description']
            # print(f"Generating image for: {p_name}")
            p_img_url = get_img_url(p_name, p_description)
            print(p_img_url+ ','+str(p['id'])+',')
            product_img_urls.append(p_img_url)
            time.sleep(12)  # Delay to avoid API rate limits
        except KeyError as e:
            print(f"Missing key in product data: {e}")
            product_img_urls.append(None)
    
    # Create DataFrame and save to CSV
    url_df = pd.DataFrame({
        'product_id': product_ids,
        'product_img_url': product_img_urls,
    })
    url_df.to_csv('product_image_urls.csv', index=False)
    print("Image URLs saved to 'product_image_urls.csv'")



products = ProductMetaData['food'] + ProductMetaData['pet'] + ProductMetaData['electronics']
build_urls(products)