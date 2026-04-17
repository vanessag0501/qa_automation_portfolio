# DAY 11 — First real test with assertions

from playwright.sync_api import sync_playwright

def test_text_box_form():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()

        page.goto("https://demoqa.com/text-box")

        # Fill the form
        page.fill("#userName",       "Vanessa Garcia")
        page.fill("#userEmail",      "vanessa@test.com")
        page.fill("#currentAddress", "123 QA Street, Sanford FL")
        page.click("#submit")

        # Assertions — this is what makes it a TEST not just a script
        output = page.locator("#output")
        assert output.is_visible(), "Output section did not appear after submit"

        name_output = page.locator("#name")
        assert "Vanessa Garcia" in name_output.inner_text(), "Name not in output"

        email_output = page.locator("#email")
        assert "vanessa@test.com" in email_output.inner_text(), "Email not in output"

        print("All assertions passed")
        page.screenshot(path="test_passed.png")
        browser.close()

test_text_box_form()