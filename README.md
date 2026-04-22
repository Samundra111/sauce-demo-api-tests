# Saucedemo QA Automation Project

A complete QA automation project built with Python, Pytest and Playwright.

## Tech Stack
- Python 3.9
- Pytest
- Playwright (UI Automation)
- Requests (API Automation)
- Pydantic (Schema Validation)
- Allure Reports
- GitHub Actions (CI/CD)

## Project Structure
```
saucedemo_tests/
    ├── pages/              # Page Object Model
    │   ├── login_page.py
    │   └── inventory_page.py
    ├── tests/
    │   ├── test_ui.py      # UI automation tests
    │   ├── test_api.py     # API tests
    │   ├── test_crud.py    # CRUD operation tests
    │   ├── test_auth.py    # Authentication tests
    │   └── test_schema.py  # Schema validation tests
    ├── reports/            # Test reports
    ├── conftest.py         # Shared fixtures
    └── pytest.ini          # Pytest configuration
```

## Test Coverage
### UI Tests
- Login with valid credentials
- Login with invalid credentials
- Locked out user login
- Inventory page verification
- Add to cart functionality

### API Tests
- GET all users
- GET single user
- POST create user
- PUT update user
- DELETE user
- Authentication (login/logout)
- Schema validation
- Response time validation
- Negative testing

## How to Run Tests

### Install dependencies
pip install -r requirements.txt
playwright install

### Run all tests
pytest tests/ -v

### Run UI tests only
pytest tests/test_ui.py -v

### Run API tests only
pytest tests/test_api.py -v

### Run with HTML report
pytest tests/ -v --html=reports/report.html --self-contained-html

### Run with Allure report
pytest tests/ -v --alluredir=reports/allure-results
allure serve reports/allure-results

### Run headed (see browser)
pytest tests/test_ui.py -v --headed

### Run in parallel
pytest tests/ -v -n=2

## CI/CD
Tests run automatically on every push via GitHub Actions.
