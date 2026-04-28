# Day 13 - Assertions 

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demoqa.com/text-box")

    #-- Part 1 : Element state assertions --

    # Is the element visible on the page?
    assert page.locator("#userName").is_visible(), "Name field is not visible"
    print("Name field is visible")

    # Is the element enabled (not greyed out)?
    assert page.locator("#userName").is_enabled(), "Name field not enabled"
    print("Name field is enabled")

    # Is the element empty before we type?
    assert page.locator("#userName").input_value() == "", "Field should be empty"
    print("Name field is empty")


    #--Part 2: Content assertions ----

    #Fill and submit the form
    page.get_by_placeholder("Full Name").fill("Vanessa Garcia")
    page.get_by_placeholder("name@example.com").fill("vanessa@test.com")
    page.get_by_placeholder("Current Address").fill("123 QA Street")
    page.get_by_role("button", name="Submit").click()

    # Does the output contain the right text?
    output = page.locator("#output")
    assert output.is_visible(), "Output did not appear"

    full_text = output.inner_text()
    assert "Vanessa Garcia" in full_text, "Name not found in output"
    assert "vanessa@test.com" in full_text, "Email not found in output"
    assert "123 QA Street" in full_text, "Address not found in output"
    print("All content assertions passed")

    # --Part 3: URL and title assertions ----

    assert "demoqa.com" in page.url, "Not on the expected URL"
    assert page.title() != "", "Page has no title"
    print(f"URL check passed: {page.url}")
    print(f"Title check passed: {page.title()}")

    page.screenshot(path="day13.png")
    browser.close()

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://demoqa.com/text-box")

    # ── Part 4: expect() — Playwright's built in assertions ───────────
    from playwright.sync_api import expect

    # expect() is smarter than assert — it automatically waits
    # for the condition to be true before failing
    expect(page.locator("#userName")).to_be_visible()
    expect(page.locator("#userName")).to_be_enabled()
    expect(page.locator("#userName")).to_be_empty()
    print("expect() state checks passed")

    # Fill and submit
    page.get_by_placeholder("Full Name").fill("Vanessa Garcia")
    page.get_by_placeholder("name@example.com").fill("vanessa@test.com")
    page.get_by_placeholder("Current Address").fill("123 QA Street")
    page.get_by_role("button", name="Submit").click()

    # expect() content checks
    expect(page.locator("#output")).to_be_visible()
    expect(page.locator("#name")).to_contain_text("Vanessa Garcia")
    expect(page.locator("#email")).to_contain_text("vanessa@test.com")
    print("expect() content checks passed")

    # expect() URL check
    expect(page).to_have_url("https://demoqa.com/text-box")
    expect(page).to_have_title("demosite")
    print("expect() URL and title checks passed")

    page.screenshot(path="day13_expect.png")
    browser.close()


#assert checks right now.... expect() is better because it automatically waits 
# for the condition to be true before failing, which makes tests more reliable and less flaky.