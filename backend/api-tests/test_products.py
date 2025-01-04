import requests
from dotenv import load_dotenv
import os
import logging

load_dotenv()
is_dev = os.getenv("TEST_DEV", "True").lower() in ("true", "1", "t")
print(os.getenv("TEST_DEV", "True").lower())
url = "http://localhost:5001" if is_dev else "https://react-rag-store.onrender.com"

# Configure logging
logging.basicConfig(level=logging.ERROR, format='%(asctime)s - %(levelname)s - %(message)s')
logging.info(f"Running tests in {'development' if is_dev else 'production'} environment")


def log_error(response):
    """Log server response errors."""
    logging.error(f"Request to {response.url} failed with status code {response.status_code}")
    logging.error(f"Response content: {response.text}")

def test_get_posts():
    """Test retrieving all posts."""
    response = requests.get(f"{url}/products")

    if response.status_code != 200:
        log_error(response)
    assert response.status_code == 200  # check HTTP status code
    assert isinstance(response.json(), list)  # check if response is a list

def test_get_post_by_id():
    """Test retrieving a post by ID."""
    response = requests.get(f"{url}/product/161")

    if response.status_code != 200:
        log_error(response)
    assert response.status_code == 200  # check HTTP status code
    assert isinstance(response.json(), dict)  # check if response is a dict

def test_get_post_by_id_invalid():
    """Test retrieving a post by an invalid ID."""
    response = requests.get(f"{url}/product/999999")

    if response.status_code != 200:
        log_error(response)
    assert response.status_code == 404  # check HTTP status code
    assert "error" in response.json()  # check if response contains an error message

def test_get_post_image():
    """Test retrieving a post image."""
    response = requests.get(f"{url}/product_image/161")

    if response.status_code != 200:
        log_error(response)
    assert response.status_code == 200  # check HTTP status code
    assert response.headers["Content-Type"] == "image/png"  # check if response is an image


def test_helth():
    """Test the health endpoint."""
    response = requests.get(f"{url}/test")

    if response.status_code != 200:
        log_error(response)
    assert response.status_code == 200  # check HTTP status code
    assert response.json()["message"] == "Test endpoint is working"  # check if response message is correct

def test_get_products_by_valid_category():
    """Test retrieving products by a valid category (food)."""
    response = requests.get(f"{url}/products/electronics")

    if response.status_code != 200:
        log_error(response)
    
    # Check HTTP status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Check if response is a list
    data = response.json()
    assert isinstance(data, list), "Response should be a list"


def test_get_products_no_category():
    """Test retrieving products when no category is specified."""
    response = requests.get(f"{url}/products")

    if response.status_code != 200:
        log_error(response)
    
    # Check HTTP status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"
    
    # Check if response is a list
    data = response.json()
    assert isinstance(data, list), "Response should be a list"

