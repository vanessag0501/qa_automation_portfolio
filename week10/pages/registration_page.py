class RegistrationPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://practicesoftwaretesting.com/auth/register"

        self.first_name = page.locator("#first_name")
        self.last_name = page.locator("#last_name")
        self.dob = page.locator("#dob")
        self.house_number = page.locator("#house_number")
        self.street = page.locator("#street")
        self.postal_code = page.locator("#postal_code")
        self.city = page.locator("#city")
        self.state = page.locator("#state")
        self.country = page.locator("#country")
        self.phone = page.locator("#phone")
        self.email = page.locator("#email")
        self.password = page.locator("#password")
        self.register_button = page.locator("[data-test='register-submit']")

    def goto(self):
        self.page.goto(self.url)
        self.first_name.wait_for(state="visible", timeout=15000)

    def register(self, first_name, last_name, dob, house_number, street,
                    postal_code, city, state, country, phone, email, password):
            self.page.screenshot(path="ci_before_fill.png", full_page=True)
            self.first_name.fill(first_name)
            self.last_name.fill(last_name)
            self.dob.fill(dob)
            self.country.select_option(label=country)

            with self.page.expect_response(lambda r: "postcode-lookup" in r.url, timeout=10000):
                self.postal_code.fill(postal_code)
                self.house_number.fill(house_number)

            # Give the autofill a moment to finish writing to the fields,
            # then overwrite everything it touched with our actual values
            self.page.wait_for_timeout(500)
            self.postal_code.fill(postal_code)
            self.house_number.fill(house_number)
            self.street.fill(street)
            self.city.fill(city)
            self.state.fill(state)

            self.phone.fill(phone)
            self.email.fill(email)
            self.password.fill(password)
            self.register_button.click()