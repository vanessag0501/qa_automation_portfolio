import pytest
from pages.registration_page import RegistrationPage
from playwright.sync_api import expect


def test_successful_registration(page):
    reg_page = RegistrationPage(page)
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
        email=f"qatest{__import__('random').randint(1000,9999)}@example.com",
        password="WillowTrees436!"
    )
    # Expect redirect to login page after successful registration
    expect(page).to_have_url("https://practicesoftwaretesting.com/auth/login")