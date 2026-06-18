from playwright.sync_api import expect
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
import random


def test_successful_login(page):
    # Register a new user first so we have valid credentials
    email = f"qatest{random.randint(1000,9999)}@example.com"
    password = "Vx9!QaTest26"

    reg_page = RegistrationPage(page)
    reg_page.goto()
    reg_page.register(
        first_name="Vanessa",
        last_name="QATest",
        dob="1995-01-01",
        house_number="123",
        street="Main Stree",
        postal_code="32771",
        city="Sanford",
        state="Florida",
        country="United States of America (the)",
        phone="4075551234",
        email=email,
        password=password
    )

    page.wait_for_timeout(1500)
    page.screenshot(path="after_register_login_test.png", full_page=True)
    print("EMAIL USED:", email)
    print("CURRENT URL:", page.url)

    # Print any visible error/alert text on the page
    error_texts = page.locator(".alert, .error, [role='alert']").all_text_contents()
    print("ERROR ELEMENTS FOUND:", error_texts)
    page.screenshot(path="after_register_login_test.png", full_page=True)

    expect(page).to_have_url("https://practicesoftwaretesting.com/auth/login")

    # Now log in with the account we just created
    login_page = LoginPage(page)
    login_page.login(email, password)

    expect(login_page.page_title).to_be_visible()