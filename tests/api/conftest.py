import pytest
from api.reqres_client import JsonPlaceholderClient

@pytest.fixture
def api_client(api_base_url) -> JsonPlaceholderClient:
    return JsonPlaceholderClient(api_base_url)
