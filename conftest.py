import pytest
from utils.request_handler import APIClient

@pytest.fixture(scope="session")
def api_client():
    base_url ="https://dog.ceo/api/"
    return APIClient(base_url)
