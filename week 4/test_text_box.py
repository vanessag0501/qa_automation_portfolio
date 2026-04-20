# week4/test_text_box.py

import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'week3'))
from pages.text_box_page import TextBoxPage


def test_valid_submission(page):
    text_box = TextBoxPage(page)
    text_box.navigate()
    text_box.fill_form("Vanessa Garcia", "vanessa@test.com", "123 QA Street")
    text_box.submit()
    text_box.verify_output("Vanessa Garcia", "vanessa@test.com", "123 QA Street")


def test_email_appears_in_output(page):
    text_box = TextBoxPage(page)
    text_box.navigate()
    text_box.fill_form("John Smith", "john@test.com", "456 Auto Ave")
    text_box.submit()
    text_box.verify_output("John Smith", "john@test.com", "456 Auto Ave")