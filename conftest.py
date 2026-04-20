import pytest
import requests
import os
from dotenv import load_dotenv

load_dotenv()

# Global variables from .env
BASE_URL = os.getenv("BASE_URL")
API_KEY = os.getenv("API_KEY")
HEADERS = {"x-api-key": API_KEY}

# 1. Change this to session scope to satisfy Playwright/base-url plugin
@pytest.fixture(scope="session")
def base_url():
    return BASE_URL

@pytest.fixture(scope="session")
def headers():
    return HEADERS

# 2. Usually, you want auth_token to be session scoped too 
# so you don't log in 50 times during one test run.
@pytest.fixture(scope="session")
def auth_token(base_url, headers):
    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    # Note: Using json=payload is better for modern APIs
    response = requests.post(f"{base_url}/login", json=payload, headers=headers)
    token = response.json()['token']
    return token

@pytest.fixture(scope="session")
def auth_headers(headers, auth_token):
    combined_headers = headers.copy()
    combined_headers['authorization'] = f"Bearer {auth_token}"
    return combined_headers

# These remain function scoped (default) because you 
# want a fresh request for every test case.
@pytest.fixture
def get_all_user(base_url, headers):
    return requests.get(f"{base_url}/users", headers=headers)

@pytest.fixture
def user_id_1(base_url, headers):
    return requests.get(f"{base_url}/users/1", headers=headers)

from playwright.async_api import Page
from pages.login_page import Login

@pytest.fixture
def logged_in_user(page:Page):
    login=Login(page)
    login.goto()
    login.login("standard_user","secret_sauce")
    return page
