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

    def register(self, first_name, last_name, dob, house_number, street,
                  postal_code, city, state, country, phone, email, password):
        self.first_name.fill(first_name)
        self.last_name.fill(last_name)
        self.dob.fill(dob)
        self.house_number.fill(house_number)
        self.street.fill(street)
        self.postal_code.fill(postal_code)
        self.city.fill(city)
        self.state.fill(state)
        self.country.select_option(label=country)
        self.phone.fill(phone)
        self.email.fill(email)
        self.password.fill(password)
        # Wait for address lookup to finish before submitting
        self.register_button.click()