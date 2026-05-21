# week4/test_text_box.py

import sys, os

import pytest
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'week3'))
from week4.pages.text_box_page import TextBoxPage

@pytest.mark.smoke
@pytest.mark.parametrize("name, email, address", [
    ("Vanessa Garcia", "vanessa@test.com", "123 QA Street"),
    ("John Smith", "john@test.com", "456 Auto Ave")
])
def test_valid_submission(page, name, email, address):
    text_box = TextBoxPage(page)
    text_box.navigate()
    text_box.fill_form(name, email, address)
    text_box.submit()
    text_box.verify_output(name, email, address)
