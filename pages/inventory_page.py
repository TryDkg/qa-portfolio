import allure

from pages.base_page import BasePage


class InventoryPage(BasePage):
    PRODUCTS_TITLE = ".title"
    BURGER_MENU = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"
    CART_BADGE = ".shopping_cart_badge"
    ADD_TO_CART_BACKPACK = "[data-test='add-to-cart-sauce-labs-backpack']"

    @allure.step("Получение заголовка страницы")
    def get_title(self) -> str:
        return self.page.locator(self.PRODUCTS_TITLE).inner_text()

    @allure.step("Получение количества товаров в корзине")
    def get_cart_badge_count(self) -> str:
        return self.page.locator(self.CART_BADGE).inner_text()

    @allure.step("Выход из системы через бургер-меню")
    def logout(self) -> None:
        self.page.locator(self.BURGER_MENU).click()
        self.page.locator(self.LOGOUT_LINK).click()

    @allure.step("Добавление рюкзака в корзину")
    def add_backpack_to_cart(self) -> None:
        self.page.locator(self.ADD_TO_CART_BACKPACK).click()
