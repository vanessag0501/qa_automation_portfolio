import pytest

@pytest.mark.mobile
def test_mobile_page_loads(mobile_page):
    """The login page loads and the login button is visible on mobile."""
    mobile_page.goto("https://www.saucedemo.com/")
    login_button = mobile_page.locator("#login-button")
    assert login_button.is_visible(), "Login button should be visible on mobile"

@pytest.mark.mobile
def test_mobile_viewport_width(mobile_page):
    """Confirm the page is actually rendering at a mobile viewport width."""
    mobile_page.goto("https://www.saucedemo.com/")
    width = mobile_page.viewport_size["width"]
    assert width < 500, f"Expected a mobile-width viewport, got {width}px"

@pytest.mark.mobile
def test_mobile_login_and_menu(mobile_page):
    """Log in and open the hamburger menu on a mobile viewport."""
    mobile_page.goto("https://www.saucedemo.com/")

    # Log in with the standard demo credentials
    mobile_page.locator("#user-name").fill("standard_user")
    mobile_page.locator("#password").fill("secret_sauce")
    mobile_page.locator("#login-button").click()

    # Confirm we reached the products page
    mobile_page.wait_for_url("**/inventory.html")

    # Open the hamburger menu (the burger icon)
    mobile_page.locator("#react-burger-menu-btn").click()

    # The logout link inside the menu should now be visible
    logout_link = mobile_page.locator("#logout_sidebar_link")
    assert logout_link.is_visible(), "Logout link should appear after opening the menu"

@pytest.mark.mobile
def test_mobile_add_to_cart(mobile_page):
    """Add an item to the cart and verify the cart badge updates on mobile."""
    mobile_page.goto("https://www.saucedemo.com/")

    mobile_page.locator("#user-name").fill("standard_user")
    mobile_page.locator("#password").fill("secret_sauce")
    mobile_page.locator("#login-button").click()
    mobile_page.wait_for_url("**/inventory.html")

    # Add the first product to the cart
    mobile_page.locator("button[data-test^='add-to-cart']").first.click()

    # The cart badge should show "1"
    cart_badge = mobile_page.locator(".shopping_cart_badge")
    assert cart_badge.inner_text() == "1", "Cart badge should show 1 item"