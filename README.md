# QA Automation Portfolio

A practical QA automation project demonstrating UI and API testing using **Python**, **Playwright**, **Pytest**, **Requests**, **Allure Reports**, and **GitHub Actions**.

The project showcases modern QA automation practices commonly used in real-world software testing projects.

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Playwright](https://img.shields.io/badge/Playwright-2EAD33)
![Pytest](https://img.shields.io/badge/Pytest-0A9EDC)
![GitHub Actions](https://img.shields.io/badge/CI-GitHub_Actions-success)
![Allure](https://img.shields.io/badge/Reports-Allure-red)

---

## Technologies

* Python
* Playwright
* Pytest
* Requests
* JSON Schema
* Allure Report
* GitHub Actions
* Git
* REST API

---

## Skills Demonstrated

* UI Test Automation
* API Testing
* REST API Validation
* Functional Testing
* JSON Schema Validation
* Page Object Model (POM)
* Parameterized Tests
* Test Reporting
* Environment Configuration
* Continuous Integration (CI)

---

## Project Features

* UI automation using Playwright
* API automation using Requests
* Page Object Model architecture
* JSON Schema validation
* Parameterized test scenarios
* Allure reporting
* GitHub Actions CI pipeline
* Environment-based configuration
* Reusable API client

---

## Test Targets

| Type | Target                    |
| ---- | ------------------------- |
| UI   | https://www.saucedemo.com |
| API  | https://reqres.in         |

---

## Project Structure

```text
qa-portfolio/
├── api/
├── config/
├── pages/
├── tests/
│   ├── api/
│   └── ui/
├── .github/workflows/
├── conftest.py
├── pytest.ini
├── requirements.txt
└── README.md
```

---

## UI Test Coverage

* Successful login
* Locked user login
* Invalid credentials
* Logout
* Add product to cart

---

## API Test Coverage

* Get users
* Get single user
* Create user
* Pagination
* JSON Schema validation
* 404 response validation

---

## Installation

```bash
git clone https://github.com/TryDkg/qa-portfolio.git

cd qa-portfolio

python -m venv .venv

source .venv/bin/activate      # Linux/macOS
# .venv\Scripts\activate       # Windows

pip install -r requirements.txt

playwright install chromium

cp .env.example .env
```

Configure the required environment variables inside `.env`.

---

## Run Tests

Run the complete test suite:

```bash
pytest
```

Run only UI tests:

```bash
pytest -m ui
```

Run only API tests:

```bash
pytest -m api
```

---

## Generate Allure Report

```bash
pytest

allure serve allure-results
```

---

## Continuous Integration

Every push and pull request automatically:

* installs dependencies
* executes UI and API tests
* generates Allure results
* validates the test suite

---

## Environment Variables

| Variable          | Description        |
| ----------------- | ------------------ |
| UI_BASE_URL       | UI application URL |
| API_BASE_URL      | API base URL       |
| REQRES_API_KEY    | Reqres API key     |
| STANDARD_USER     | Test username      |
| STANDARD_PASSWORD | Test password      |

---

## About

This repository is part of my QA engineering portfolio and demonstrates practical automation testing skills using modern Python testing tools and industry-standard testing practices.
