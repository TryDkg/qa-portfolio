import pytest

@pytest.fixture(scope="function")
def browser_context_args(browser_context_args):
    """Настройки контекста браузера для всех UI-тестов."""
    return {
        **browser_context_args,
        "viewport": {"width": 1920, "height": 1080},
        "locale": "en-US",
    }

@pytest.fixture(scope="function")
def ui_base_url():
    return "https://www.saucedemo.com"

@pytest.fixture(scope="function")
def api_base_url():
    return "https://jsonplaceholder.typicode.com"
