import requests
from dotenv import load_dotenv
import os



load_dotenv()
is_dev = os.getenv("TEST_DEV", "True").lower() in ("true", "1", "t")
print(os.getenv("TEST_DEV", "True").lower())
url = "http://localhost:5001" if is_dev else "https://react-rag-store.onrender.com"



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
