# week6/conftest.py
import pytest
import requests

@pytest.fixture(scope="session")
def api_base_url():
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

@pytest.fixture(scope="session")
def posts_endpoint(api_base_url):
    return f"{api_base_url}/posts"

@pytest.fixture(scope="session")
def api_client(auth_headers):
    session = requests.Session()
    session.headers.update(auth_headers)
    yield session
    session.close()

@pytest.mark.parametrize("post_id", [1, 50, 100])
def test_get_post_by_id(api_client, api_base_url, post_id):
    response = api_client.get(f"{api_base_url}/posts/{post_id}")
    assert response.status_code == 200, f"Expected status code 200 but got {response.status_code} for post ID {post_id}"