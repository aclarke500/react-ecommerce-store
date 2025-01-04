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


def test_query():
    """Test the /query endpoint."""
    payload = {"query": "Find products that are good for computers"}
    response = requests.post(f"{url}/query", json=payload)

    # Check HTTP status code
    assert response.status_code == 200, f"Expected 200, got {response.status_code}"

    # Check if response is a list
    data = response.json()
    assert isinstance(data, list), "Response should be a list"

    # Validate structure of the first item if available
    if data:
        first_item = data[0]
        expected_keys = {"price", "id", "name", "description", "quantity", "availability"}
        assert expected_keys.issubset(first_item.keys()), "Missing keys in response item"
