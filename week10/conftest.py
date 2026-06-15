# week10/conftest.py
import pytest

@pytest.fixture(scope="session")
def base_url():
    return "https://practicesoftwaretesting.com"