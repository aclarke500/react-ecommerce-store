import requests
from dotenv import load_dotenv
import os

load_dotenv()
is_dev = os.getenv("TEST_DEV", "True").lower() in ("true", "1", "t")
print(os.getenv("TEST_DEV", "True").lower())
url = "http://localhost:5001" if is_dev else "https://react-rag-store.onrender.com"


def test_get_posts():
    """Test retrieving all posts."""
    response = requests.get(f"{url}/products")
    assert response.status_code == 200  # check HTTP status code
    assert isinstance(response.json(), list)  # check if response is a list

def test_get_post_by_id():
    """Test retrieving a post by ID."""
    response = requests.get(f"{url}/product/161")
    assert response.status_code == 200  # check HTTP status code
    assert isinstance(response.json(), dict)  # check if response is a dict

def test_get_post_by_id_invalid():
    """Test retrieving a post by an invalid ID."""
    response = requests.get(f"{url}/product/999999")
    assert response.status_code == 404  # check HTTP status code
    assert "error" in response.json()  # check if response contains an error message

def test_get_post_image():
    """Test retrieving a post image."""
    response = requests.get(f"{url}/product_image/161")
    assert response.status_code == 200  # check HTTP status code
    assert response.headers["Content-Type"] == "image/png"  # check if response is an image


def test_helth():
    """Test the health endpoint."""
    response = requests.get(f"{url}/test")
    assert response.status_code == 200  # check HTTP status code
    assert response.json()["message"] == "Test endpoint is working"  # check if response message is correct