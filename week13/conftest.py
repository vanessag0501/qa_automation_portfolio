# week13/conftest.py
import pytest
from playwright.sync_api import sync_playwright

# Devices we'll test against
DEVICES = ["iPhone 13", "Pixel 5", "Galaxy S9+"]


@pytest.fixture(params=DEVICES)
def mobile_page(request):
    """Launch a browser context emulating a specific mobile device."""
    device_name = request.param
    with sync_playwright() as p:
        device = p.devices[device_name]
        browser = p.chromium.launch()
        context = browser.new_context(**device)
        page = context.new_page()
        yield page
        context.close()
        browser.close()