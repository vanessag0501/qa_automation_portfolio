#Day 12 - Locators 

from playwright.sync_api import sync_playwright

# with sync_playwright() as p:
#     browser = p.chromium.launch(headless=False)
#     page = browser.new_page()
#     page.goto("https://demoqa.com/text-box")

#     # -- 4 ways to find elements---
#     #1. By ID - most reliable, use when available
#     page.fill("#userName", "Vanessa")

#     #2. By Placeholder text - readable and stable
#     page.fill("[placeholder='name@example.com']", "vanessa@test.com")

#     #3. By label text - closest to how a real user finds a field
#     page.fill("textarea[id='currentAddress']", "123 QA Street, Sanford FL")

#     #4. By CSS selector -flexible, works on anything 
#     page.click("button#submit")

#     # Verify that the output is visible
#     assert page.locator("#output").is_visible(), "Output did not appear"
#     print("Form submitted and output is visible")

#     page.screenshot(path= "day12.png")
#     browser.close()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demoqa.com/text-box")

    # Using what actually works on this page
    page.get_by_placeholder("Full Name").fill("Vanessa Garcia")
    page.get_by_placeholder("name@example.com").fill("vanessa@test.com")
    page.get_by_placeholder("Current Address").fill("123 QA Street")

    # get_by_role works for the button
    page.get_by_role("button", name="Submit").click()

    output = page.locator("#output")
    assert output.is_visible(), "Output did not appear"
    print("All locators passed")

    page.screenshot(path="day12_roles.png")
    browser.close()