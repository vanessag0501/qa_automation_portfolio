# week6/conftest.py

import pytest
import requests

@pytest.fixture(scope="session")
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture(scope="session")
def http_url():
    return "https://httpbin.org"

@pytest.fixture(scope="session")
def post_payload():
    return {
        "title":  "QA Automation Test Post",
        "body":   "Created by Vanessa's API test suite",
        "userId": 1
    }

@pytest.fixture(scope="session")
def auth_headers():
    return {
        "Authorization": "Bearer test-token-123",
        "Content-Type":  "application/json"
    }