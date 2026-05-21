# week4/conftest.py

import pytest

# This runs automatically before every test — no need to import it
@pytest.fixture(scope="session")
def base_url():
    return "https://demoqa.com"