#Day 11 - First Playwright Script

from playwright.sync_api import sync_playwright

with sync_playwright() as p:

    #Launch a real Chrome Browser

    browser = p.chromium.launch(headless = False)
    page = browser.new_page()

    #Navigate to a page

    page.goto("https://google.com")

    #Print the page title 
    print(f" page title: {page.title()}")

    page.screenshot(path="google_homepage.png")

    browser.close()
    print("Browser closed")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto("https://demoqa.com/text-box")

    page.fill("#userName", "Vanessa Garcia")
    page.fill("#userEmail", "vanessa@test.com")
    page.fill("#currentAddress", "123 Main St, Anytown")

    #click the submit button
    page.click("#submit")

    output = page.locator("#output")
    print(f"Output visible: { output.is_visible() }")

    # Take a screenshot of the result
    page.screenshot(path="demoqa_textbox.png")
    print("Screenshot saved - open demoqa_textbox.png to see the result")

    browser.close()
    print("Browser closed")


