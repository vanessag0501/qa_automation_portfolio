import pytest 

@pytest.fixture
def base_url():
    return "https://jsonplaceholder.typicode.com"

@pytest.fixture
def post_payload():
    return {
        "title":  "QA Automation Test Post",
        "body":   "Created by Vanessa's API test suite",
        "userId": 1
    }