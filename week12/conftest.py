import pytest

@pytest.fixture(scope="module")
def api_base_url():
    return "https://github.com"