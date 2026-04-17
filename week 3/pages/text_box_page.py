# pages/text_box_page.py

from playwright.sync_api import Page, expect

class TextBoxPage:
    def __init__(self, page: Page):
        self.page = page

        #All locators defined in one place
        self.name_filed = page.get_by_placeholder("Full Name")
        self.email_field = page.get_by_placeholder("name@example.com")
        self.address_field = page.get_by_placeholder("Current Address")
        self.submit_button = page.get_by_role("button", name="Submit")
        self.output = page.locator("#output")
        self.name_output = page.locator("#name")
        self.email_output = page.locator("#email")
        self.address_output = page.locator("#output #currentAddress")

    def navigate(self):
        self.page.goto("https://demoqa.com/text-box")
    
    def fill_form(self, name, email, address):
        self.name_filed.fill(name)
        self.email_field.fill(email)
        self.address_field.fill(address)
    
    def submit (self):
        self.submit_button.click()
    
    def verify_output(self, name, email, address):
        expect(self.output).to_be_visible()
        expect(self.name_output).to_contain_text(name)
        expect(self.email_output).to_contain_text(email)
        expect(self.address_output).to_contain_text(address)