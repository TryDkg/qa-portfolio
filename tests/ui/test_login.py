import allure
import pytest
from pages.login_page import LoginPage

@allure.feature("Авторизация")
class TestLogin:

    @allure.title("Успешный вход с корректными данными")
    @pytest.mark.ui
    def test_login_standard_user(self, page, ui_base_url):
        login_page = LoginPage(page, ui_base_url)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        from pages.inventory_page import InventoryPage
        inventory = InventoryPage(page, ui_base_url)
        inventory.check_title_is_products()
        login_page.attach_screenshot("Успешный вход")

    @allure.title("Ошибка при входе заблокированного пользователя")
    @pytest.mark.ui
    def test_login_locked_out_user(self, page, ui_base_url):
        login_page = LoginPage(page, ui_base_url)
        login_page.open()
        login_page.login("locked_out_user", "secret_sauce")

        error_text = login_page.get_error_message()
        assert "Sorry, this user has been locked out" in error_text
        login_page.attach_screenshot("Заблокированный пользователь")
