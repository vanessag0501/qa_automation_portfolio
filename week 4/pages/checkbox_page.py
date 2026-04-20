# pages/checkbox_page.py

from playwright.sync_api import Page, expect

class CheckboxPage:
    def __init__(self, page: Page):
        self.page = page
        self.result = page.locator("#result")

    def navigate(self):
        self.page.goto("https://demoqa.com/checkbox")

    def expand_home(self):
        # Click the toggle arrow next to Home to expand the tree
        self.page.locator(".rc-tree-switcher").first.click()

    def select_checkbox(self, label):
        self.page.get_by_label(f"Select {label}").click()

    def verify_selected(self, item):
        expect(self.result).to_be_visible()
        expect(self.result).to_contain_text(item)