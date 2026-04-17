from playwright.sync_api import sync_playwright
from pages.text_box_page import TextBoxPage
from pages.checkbox_page import CheckboxPage
from pages.radio_button_page import RadioButtonPage

def test_text_box():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        text_box = TextBoxPage(page)
        text_box.navigate()
        text_box.fill_form("Vanessa Garcia", "vanessa@test.com", "123 Main Street")
        text_box.submit()
        text_box.verify_output("Vanessa Garcia", "vanessa@test.com", "123 Main Street")
        print("Text box test passed")
        browser.close()

def test_radio_button():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        radio_button = RadioButtonPage(page)
        radio_button.navigate()

        radio_button.select("Yes")
        radio_button.verify_selected("Yes")
        print("Yes selected and verified")

        radio_button.select("Impressive")
        radio_button.verify_selected("Impressive")
        print("Impressive selected and verified")

        browser.close()

def test_checkbox():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        checkbox = CheckboxPage(page)
        checkbox.navigate()
        checkbox.expand_home()

        checkbox.select_checkbox("Downloads")
        checkbox.verify_selected("downloads")
        print("Downloads checkbox selected and verified")

        browser.close()

#run all three
test_text_box()
test_radio_button()
test_checkbox()

