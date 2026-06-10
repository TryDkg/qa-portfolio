import pytest
from api.reqres_client import ReqresClient

@pytest.fixture
def reqres_client(api_base_url) -> ReqresClient:
    return ReqresClient(api_base_url)
