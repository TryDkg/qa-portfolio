import allure
import pytest


@allure.feature("Авторизация")
class TestLogin:

    @allure.title("Успешный вход с корректными данными")
    @pytest.mark.ui
    def test_login_standard_user(
        self, login_page, inventory_page, standard_user, standard_password
    ):
        login_page.open()
        login_page.login(standard_user, standard_password)

        assert inventory_page.get_title() == "Products"
        login_page.attach_screenshot("Успешный вход")

    @allure.title("Ошибка при входе заблокированного пользователя")
    @pytest.mark.ui
    def test_login_locked_out_user(
        self, login_page, standard_password, locked_out_user
    ):
        login_page.open()
        login_page.login(locked_out_user, standard_password)

        error_text = login_page.get_error_message()
        assert "Sorry, this user has been locked out" in error_text
        login_page.attach_screenshot("Заблокированный пользователь")

    @allure.title("Ошибка при входе с неверным паролем")
    @pytest.mark.ui
    @pytest.mark.parametrize(
        "username,password,expected_error",
        [
            ("standard_user", "wrong_password", "Username and password do not match"),
            ("", "secret_sauce", "Username is required"),
        ],
    )
    def test_login_invalid_credentials(
        self, login_page, username, password, expected_error
    ):
        login_page.open()
        login_page.login(username, password)

        assert expected_error in login_page.get_error_message()
        login_page.attach_screenshot(f"Ошибка: {expected_error}")


@allure.feature("Выход из системы")
class TestLogout:

    @allure.title("Выход из системы возвращает на страницу входа")
    @pytest.mark.ui
    def test_logout(self, logged_in_inventory, login_page):
        logged_in_inventory.logout()

        assert login_page.is_login_form_visible()
        login_page.attach_screenshot("Выход выполнен")
