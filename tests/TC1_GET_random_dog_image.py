import requests
from utils.request_handler import APIClient
import pytest

def test_get_random_dog_image(api_client):
    response = api_client.get("breeds/image/random")
    assert response.status_code == 200
    # Content-Type validation
    assert "application/json" in response.headers["Content-Type"]

    # Parse and print JSON
    data = response.json()
    print(f"\nResponse JSON: {data}")

    # Validate fields
    assert "status" in data
    assert data["status"] == "success"
    assert "message" in data
    assert data["message"].startswith("https://")
    assert data["message"].endswith(".jpg") or data["message"].endswith(".png")

