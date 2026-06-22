import pytest
import allure
from pages.login_page import LoginPage
from pages.registration_page import RegistrationPage
from playwright.sync_api import expect
import random

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("Registered user can log in successfully")
@allure.description("Registers a new account, then verifies the user can log in with those credentials and reach their account page.")
@pytest.mark.local_only
def test_successful_login(page):
    email = f"qatest{random.randint(1000,9999)}@example.com"
    password = "Vx9!QaTest26"

    reg_page = RegistrationPage(page)

    with allure.step("Register a new account to use for login"):
        reg_page.goto()
        reg_page.register(
            first_name="Vanessa",
            last_name="QATest",
            dob="1995-01-01",
            house_number="123",
            street="Main Street",
            postal_code="32771",
            city="Sanford",
            state="Florida",
            country="United States of America (the)",
            phone="4075551234",
            email=email,
            password=password
        )
        expect(page).to_have_url("https://practicesoftwaretesting.com/auth/login")

    with allure.step("Log in with the new account"):
        login_page = LoginPage(page)
        login_page.login(email, password)

    with allure.step("Verify the account page is shown"):
        try:
            expect(login_page.page_title).to_be_visible()
        except Exception:
            allure.attach(
                page.screenshot(),
                name="login_failure",
                attachment_type=allure.attachment_type.PNG
            )
            raise