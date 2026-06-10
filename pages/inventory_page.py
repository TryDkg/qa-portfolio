import allure
from pages.base_page import BasePage

class InventoryPage(BasePage):
    PRODUCTS_TITLE = ".title"
    BURGER_MENU = "#react-burger-menu-btn"
    LOGOUT_LINK = "#logout_sidebar_link"
    CART_ICON = ".shopping_cart_link"
    ADD_TO_CART_BACKPACK = "[data-test='add-to-cart-sauce-labs-backpack']"

    @allure.step("Проверка, что заголовок страницы = 'Products'")
    def check_title_is_products(self):
        assert self.page.locator(self.PRODUCTS_TITLE).inner_text() == "Products"

    @allure.step("Выход из системы через бургер-меню")
    def logout(self):
        self.page.locator(self.BURGER_MENU).click()
        self.page.locator(self.LOGOUT_LINK).click()

    @allure.step("Добавление рюкзака в корзину")
    def add_backpack_to_cart(self):
        self.page.locator(self.ADD_TO_CART_BACKPACK).click()
