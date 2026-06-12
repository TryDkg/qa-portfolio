import allure
import pytest


@allure.feature("Корзина")
class TestInventory:

    @allure.title("Добавление товара в корзину")
    @pytest.mark.ui
    def test_add_item_to_cart(self, logged_in_inventory):
        logged_in_inventory.add_backpack_to_cart()

        assert logged_in_inventory.get_cart_badge_count() == "1"
        logged_in_inventory.attach_screenshot("Товар добавлен в корзину")
