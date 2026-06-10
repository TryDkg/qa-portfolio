# QA Portfolio — автотесты UI и API

[![Tests](https://github.com/TryDkg/qa-portfolio/actions/workflows/tests.yml/badge.svg)](https://github.com/TryDkg/qa-portfolio/actions)
[![Allure Report](https://img.shields.io/badge/Allure%20Report-Live-green)](https://trydkg.github.io/qa-portfolio)

Проект демонстрирует навыки автоматизации тестирования веб-приложений и REST API.

**Стек:** Python, Playwright, Pytest, Requests, Allure, GitHub Actions.

**Объекты тестирования:**
- UI: https://www.saucedemo.com
- API: https://reqres.in

Features

• UI testing with Playwright
• API testing with Requests
• Page Object Model
• JSON Schema validation
• Allure reporting
• GitHub Actions CI

**Структура:**
- `pages/` — Page Object Model для UI
- `api/` — клиент и JSON-схемы для API
- `tests/ui` — UI-тесты
- `tests/api` — API-тесты

**Локальный запуск:**
```bash
pip install -r requirements.txt
playwright install chromium
pytest
