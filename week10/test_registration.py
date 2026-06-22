import pytest
import allure
from pages.registration_page import RegistrationPage
from playwright.sync_api import expect
import random

@allure.severity(allure.severity_level.CRITICAL)
@allure.title("New customer can register successfully")
@allure.description("Verifies that a new user can complete the registration form and is redirected to the login page.")
@pytest.mark.local_only
def test_successful_registration(page):
    reg_page = RegistrationPage(page)

    with allure.step("Navigate to the registration page"):
        reg_page.goto()

    with allure.step("Fill out and submit the registration form"):
        reg_page.register(
            first_name="Vanessa",
            last_name="Garcia",
            dob="1995-01-01",
            house_number="123",
            street="Main Street",
            postal_code="32771",
            city="Sanford",
            state="Florida",
            country="United States of America (the)",
            phone="4075551234",
            email=f"qatest{random.randint(1000,9999)}@example.com",
            password="Vx9!QaTest26"
        )

    with allure.step("Verify redirect to login page"):
        expect(page).to_have_url("https://practicesoftwaretesting.com/auth/login")