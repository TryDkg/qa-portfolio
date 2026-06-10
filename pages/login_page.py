import allure
from pages.base_page import BasePage

class LoginPage(BasePage):
    # Локаторы
    USERNAME_INPUT = "[data-test='username']"
    PASSWORD_INPUT = "[data-test='password']"
    LOGIN_BUTTON = "[data-test='login-button']"
    ERROR_MESSAGE = "[data-test='error']"

    @allure.step("Авторизация с логином {username} и паролем {password}")
    def login(self, username: str, password: str):
        self.page.locator(self.USERNAME_INPUT).fill(username)
        self.page.locator(self.PASSWORD_INPUT).fill(password)
        self.page.locator(self.LOGIN_BUTTON).click()

    @allure.step("Получение текста ошибки")
    def get_error_message(self) -> str:
        return self.page.locator(self.ERROR_MESSAGE).inner_text()
