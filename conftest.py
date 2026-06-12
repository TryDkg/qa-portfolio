import pytest

from config.settings import (
    API_BASE_URL,
    LOCKED_OUT_USER,
    REQRES_API_KEY,
    STANDARD_PASSWORD,
    STANDARD_USER,
    UI_BASE_URL,
)
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


@pytest.fixture(scope="function")
def browser_context_args(browser_context_args):
    """Настройки контекста браузера для всех UI-тестов."""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "locale": "en-US",
    }


@pytest.fixture(scope="function")
def ui_base_url() -> str:
    return UI_BASE_URL


@pytest.fixture(scope="function")
def api_base_url() -> str:
    return API_BASE_URL


@pytest.fixture(scope="function")
def reqres_api_key() -> str:
    return REQRES_API_KEY


@pytest.fixture(scope="function")
def standard_user() -> str:
    return STANDARD_USER


@pytest.fixture(scope="function")
def standard_password() -> str:
    return STANDARD_PASSWORD


@pytest.fixture(scope="function")
def locked_out_user() -> str:
    return LOCKED_OUT_USER


@pytest.fixture(scope="function")
def login_page(page, ui_base_url) -> LoginPage:
    return LoginPage(page, ui_base_url)


@pytest.fixture(scope="function")
def inventory_page(page, ui_base_url) -> InventoryPage:
    return InventoryPage(page, ui_base_url)


@pytest.fixture(scope="function")
def logged_in_inventory(login_page, standard_user, standard_password) -> InventoryPage:
    """Авторизованный пользователь на странице каталога."""
    login_page.open()
    login_page.login(standard_user, standard_password)
    return InventoryPage(login_page.page, login_page.base_url)
