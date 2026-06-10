import allure
import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

@allure.feature("Корзина")
class TestInventory:

    @allure.title("Добавление товара в корзину")
    @pytest.mark.ui
    def test_add_item_to_cart(self, page, ui_base_url):
        # Предусловие: авторизоваться
        login_page = LoginPage(page, ui_base_url)
        login_page.open()
        login_page.login("standard_user", "secret_sauce")

        inventory = InventoryPage(page, ui_base_url)
        inventory.add_backpack_to_cart()
        # Проверим, что иконка корзины показывает количество
        cart_badge = page.locator(".shopping_cart_badge")
        assert cart_badge.inner_text() == "1"
        inventory.attach_screenshot("Товар добавлен в корзину")
