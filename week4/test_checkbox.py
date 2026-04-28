# week4/test_checkbox.py

from pages.checkbox_page import CheckboxPage


def test_downloads_checkbox(page):
    checkbox = CheckboxPage(page)
    checkbox.navigate()
    checkbox.expand_home()
    checkbox.select_checkbox("Downloads")
    checkbox.verify_selected("downloads")