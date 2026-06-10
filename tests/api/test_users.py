import allure
import pytest
from jsonschema import validate
from api.schemas.user import SINGLE_USER_SCHEMA, CREATE_USER_SCHEMA

@allure.feature("Пользователи")
class TestUsers:

    @allure.title("Получение одного пользователя и валидация схемы")
    @pytest.mark.api
    def test_get_single_user(self, api_client):
        response = api_client.get_single_user(1)
        assert response.status_code == 200
        body = response.json()
        validate(instance=body, schema=SINGLE_USER_SCHEMA)

    @allure.title("Создание пользователя и проверка ответа")
    @pytest.mark.api
    def test_create_user(self, api_client):
        response = api_client.create_user("John", "john@example.com")
        assert response.status_code == 201
        body = response.json()
        validate(instance=body, schema=CREATE_USER_SCHEMA)
        assert body["name"] == "John"
