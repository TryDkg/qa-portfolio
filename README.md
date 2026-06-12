# QA Portfolio — автотесты UI и API

[![Tests](https://github.com/TryDkg/qa-portfolio/actions/workflows/tests.yml/badge.svg)](https://github.com/TryDkg/qa-portfolio/actions)
[![Allure Report](https://img.shields.io/badge/Allure%20Report-Live-green)](https://trydkg.github.io/qa-portfolio)

Проект демонстрирует навыки автоматизации тестирования веб-приложений и REST API.

**Стек:** Python, Playwright, Pytest, Requests, JSON Schema, Allure, GitHub Actions.

**Features:**
- UI testing with Playwright
- API testing with Requests
- Page Object Model
- JSON Schema validation
- Allure reporting
- GitHub Actions CI

**Объекты тестирования:**

| Тип | URL |
|-----|-----|
| UI | https://www.saucedemo.com |
| API | https://reqres.in |

## Структура

```
config/          — настройки окружения (.env)
pages/           — Page Object Model для UI
api/             — HTTP-клиент и JSON-схемы
tests/ui/        — UI-тесты
tests/api/       — API-тесты
```

## Быстрый старт

```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements.txt
playwright install chromium
cp .env.example .env        # и указать REQRES_API_KEY
pytest
```

## Запуск тестов

```bash
pytest                  # все тесты
pytest -m ui            # только UI
pytest -m api           # только API
pytest tests/ui/        # конкретная папка
```

## Allure-отчёт локально

```bash
pytest
allure serve allure-results
```

Для Allure CLI: [официальная установка](https://allurereport.org/docs/install/) или `npx allure-commandline serve allure-results`.

## Конфигурация

Переменные окружения (файл `.env` или CI):

| Переменная | Описание | По умолчанию |
|------------|----------|--------------|
| `UI_BASE_URL` | URL UI-приложения | `https://www.saucedemo.com` |
| `API_BASE_URL` | Базовый URL API | `https://reqres.in/api` |
| `REQRES_API_KEY` | API-ключ reqres.in | — (обязателен для API-тестов) |
| `STANDARD_USER` | Логин тестового пользователя | `standard_user` |
| `STANDARD_PASSWORD` | Пароль | `secret_sauce` |

Ключ reqres.in: [app.reqres.in](https://app.reqres.in).

## Покрытие

### UI (Sauce Demo)

| Сценарий | Файл |
|----------|------|
| Успешный вход | `test_login.py` |
| Заблокированный пользователь | `test_login.py` |
| Неверные credentials (parametrize) | `test_login.py` |
| Выход из системы | `test_login.py` |
| Добавление товара в корзину | `test_inventory.py` |

### API (Reqres)

| Сценарий | Файл |
|----------|------|
| Список пользователей + JSON Schema | `test_users.py` |
| Один пользователь + JSON Schema | `test_users.py` |
| Создание пользователя | `test_users.py` |
| 404 для несуществующего ID | `test_users.py` |
| Пагинация (page 1, 2) | `test_users.py` |

## CI/CD

GitHub Actions при push/PR в `main`:

1. Запускает pytest (workflow падает, если тесты красные)
2. Собирает Allure-отчёт с историей
3. Публикует на [GitHub Pages](https://trydkg.github.io/qa-portfolio)

## Линтер

```bash
pip install ruff
ruff check .
```
