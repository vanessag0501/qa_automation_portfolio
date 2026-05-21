# week4/test_checkbox.py

import pytest

from week4.pages.checkbox_page import CheckboxPage

@pytest.mark.regression
def test_downloads_checkbox(page):
    checkbox = CheckboxPage(page)
    checkbox.navigate()
    checkbox.expand_home()
    checkbox.select_checkbox("Downloads")
    checkbox.verify_selected("downloads")