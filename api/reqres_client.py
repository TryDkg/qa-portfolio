import requests
import allure

class ReqresClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    @allure.step("GET /users?page={page}")
    def get_users(self, page: int = 1):
        return self.session.get(f"{self.base_url}/users", params={"page": page})

    @allure.step("POST /users")
    def create_user(self, name: str, job: str):
        return self.session.post(
            f"{self.base_url}/users",
            json={"name": name, "job": job}
        )

    @allure.step("GET /users/{user_id}")
    def get_single_user(self, user_id: int):
        return self.session.get(f"{self.base_url}/users/{user_id}")
