import allure
from playwright.sync_api import Page

class BasePage:
    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url

    def open(self, path: str = ""):
        full_url = f"{self.base_url}/{path.lstrip('/')}"
        with allure.step(f"Открываю страницу {full_url}"):
            self.page.goto(full_url)

    def wait_for_element(self, selector: str, timeout: int = 10000):
        return self.page.locator(selector).wait_for(timeout=timeout)

    def attach_screenshot(self, name: str = "screenshot"):
        allure.attach(
            self.page.screenshot(),
            name=name,
            attachment_type=allure.attachment_type.PNG
        )
