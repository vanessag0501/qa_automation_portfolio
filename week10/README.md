# Week 10 - End-to-End Automation

Full registration and login flows automated with Playwright and the Page Object Model.

## Contents
- `pages/registration_page.py` - Page Object for the registration form, including handling of the address autofill lookup
- `pages/login_page.py` - Page Object for the login form
- `test_registration.py` - registers a new account and verifies the redirect, with Allure steps and severity
- `test_login.py` - registers an account, logs in, and verifies the account page
- `conftest.py`, `pytest.ini` - config and the local_only marker

## Target
Tests run against practicesoftwaretesting.com. The site blocks CI runner IPs via Cloudflare, so these tests are marked `local_only` and run locally rather than in CI.

## Running
```
python -m pytest -v -m local_only
```

## Notes
Three real application behaviors were found while building this suite: an address autofill that overwrites manually entered data, a race condition on submit during the address lookup, and a breached-password rejection with no client-side warning. See the repo-level BUGS.md.