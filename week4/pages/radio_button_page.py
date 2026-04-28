from playwright.sync_api import Page, expect

class RadioButtonPage:
    def __init__(self, page: Page):
        self.page = page
        self.result = page.locator(".mt-3")
    
    def navigate(self):
        self.page.goto("https://demoqa.com/radio-button")
    
    def select(self, option):
        #option should be yes impressive or no
        self.page.get_by_text(option, exact = True).click()
    
    def verify_selected(self, option):
        expect(self.result).to_be_visible()
        expect(self.result).to_contain_text(option)
