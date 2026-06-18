class LoginPage:
    def __init__(self, page):
        self.page = page
        self.url = "https://practicesoftwaretesting.com/auth/login"

        self.email = page.locator("#email")
        self.password = page.locator("#password")
        self.login_button = page.locator("[data-test='login-submit']")
        self.page_title = page.locator("[data-test='page-title']")
    
    def goto(self):
        self.page.goto(self.url)
    
    def login(self, email, password):
        self.email.fill(email)
        self.password.fill(password)
        self.login_button.click()
        