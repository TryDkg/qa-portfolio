import allure
import pytest
from jsonschema import validate

from api.schemas.user import (
    CREATE_USER_SCHEMA,
    NOT_FOUND_SCHEMA,
    SINGLE_USER_SCHEMA,
    USERS_LIST_SCHEMA,
)


@allure.feature("Пользователи")
class TestUsers:

    @allure.title("Получение списка пользователей и валидация схемы")
    @pytest.mark.api
    def test_get_users_list(self, reqres_client):
        response = reqres_client.get_users(page=1)

        assert response.status_code == 200
        body = response.json()
        validate(instance=body, schema=USERS_LIST_SCHEMA)
        assert body["page"] == 1
        assert len(body["data"]) > 0

    @allure.title("Получение одного пользователя и валидация схемы")
    @pytest.mark.api
    def test_get_single_user(self, reqres_client):
        response = reqres_client.get_single_user(2)

        assert response.status_code == 200
        body = response.json()
        validate(instance=body, schema=SINGLE_USER_SCHEMA)
        assert body["data"]["id"] == 2
        assert body["data"]["first_name"]

    @allure.title("Создание пользователя и проверка ответа")
    @pytest.mark.api
    def test_create_user(self, reqres_client):
        response = reqres_client.create_user("morpheus", "leader")

        assert response.status_code == 201
        body = response.json()
        validate(instance=body, schema=CREATE_USER_SCHEMA)
        assert body["name"] == "morpheus"
        assert body["job"] == "leader"

    @allure.title("Запрос несуществующего пользователя возвращает 404")
    @pytest.mark.api
    def test_get_user_not_found(self, reqres_client):
        response = reqres_client.get_single_user(9999)

        assert response.status_code == 404
        validate(instance=response.json(), schema=NOT_FOUND_SCHEMA)

    @allure.title("Пагинация: вторая страница списка пользователей")
    @pytest.mark.api
    @pytest.mark.parametrize("page", [1, 2])
    def test_get_users_pagination(self, reqres_client, page):
        response = reqres_client.get_users(page=page)

        assert response.status_code == 200
        body = response.json()
        validate(instance=body, schema=USERS_LIST_SCHEMA)
        assert body["page"] == page
