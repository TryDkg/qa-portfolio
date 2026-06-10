import requests
import allure

class JsonPlaceholderClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.session = requests.Session()

    @allure.step("GET /users")
    def get_users(self):
        return self.session.get(f"{self.base_url}/users")

    @allure.step("POST /users")
    def create_user(self, name: str, email: str):
        return self.session.post(
            f"{self.base_url}/users",
            json={"name": name, "email": email}
        )

    @allure.step("GET /users/{user_id}")
    def get_single_user(self, user_id: int):
        return self.session.get(f"{self.base_url}/users/{user_id}")
