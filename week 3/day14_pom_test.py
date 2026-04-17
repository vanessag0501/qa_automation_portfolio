from playwright.sync_api import sync_playwright
from pages.text_box_page import TextBoxPage

def test_valid_form_submission():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        #use the page object - no locators in the test itself
        text_box_page = TextBoxPage(page)
        text_box_page.navigate()
        text_box_page.fill_form(
            name = "Vanessa Garcia",
            email = "vanessa@test.com",
            address = "123 Main Street"
        )
        
        text_box_page.submit()
        text_box_page.verify_output("Vanessa Garcia", "vanessa@test.com", "123 Main Street")

        print("Test passed successfully - form submitted and output verified")
        page.screenshot(path="day14_pom.png")
        browser.close()

def test_different_user():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        
        text_box_page = TextBoxPage(page)
        text_box_page.navigate()
        text_box_page.fill_form(
            name = "John Doe",
            email = "john@test.com",
            address = "456 Elm Street"
        )
        text_box_page.submit()
        text_box_page.verify_output("John Doe", "john@test.com", "456 Elm Street")

        print("Test passed - different user verified")
        browser.close()

#run both tests
test_valid_form_submission()
test_different_user()

                                