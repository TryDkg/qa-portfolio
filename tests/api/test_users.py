import allure
import pytest
from jsonschema import validate
from api.schemas.user import SINGLE_USER_SCHEMA, CREATE_USER_SCHEMA

@allure.feature("Пользователи")
class TestUsers:

    @allure.title("Получение одного пользователя и валидация схемы")
    @pytest.mark.api
    def test_get_single_user(self, reqres_client):
        response = reqres_client.get_single_user(2)
        assert response.status_code == 200
        body = response.json()
        validate(instance=body, schema=SINGLE_USER_SCHEMA)
        assert body["data"]["id"] == 2
        assert body["data"]["first_name"] is not None

    @allure.title("Создание пользователя и проверка ответа")
    @pytest.mark.api
    def test_create_user(self, reqres_client):
        response = reqres_client.create_user("morpheus", "leader")
        assert response.status_code == 201
        body = response.json()
        validate(instance=body, schema=CREATE_USER_SCHEMA)
        assert body["name"] == "morpheus"
        assert body["job"] == "leader"
