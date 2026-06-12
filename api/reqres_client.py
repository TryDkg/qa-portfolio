import allure
import requests
from requests import Response


class ReqresClient:
    def __init__(self, base_url: str, api_key: str = ""):
        self.base_url = base_url.rstrip("/")
        self.session = requests.Session()
        if api_key:
            self.session.headers["x-api-key"] = api_key

    @allure.step("GET /users?page={page}")
    def get_users(self, page: int = 1) -> Response:
        return self.session.get(f"{self.base_url}/users", params={"page": page})

    @allure.step("POST /users")
    def create_user(self, name: str, job: str) -> Response:
        return self.session.post(
            f"{self.base_url}/users",
            json={"name": name, "job": job},
        )

    @allure.step("GET /users/{user_id}")
    def get_single_user(self, user_id: int) -> Response:
        return self.session.get(f"{self.base_url}/users/{user_id}")
