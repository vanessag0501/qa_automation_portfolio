# Bug and Issue Log

A record of defects found in applications under test, and technical issues resolved while building this portfolio. Application defects are genuine product findings. Technical issues are environment and tooling problems that were debugged during development.

---

## Application Defects

Real bugs found in the software under test.

### OpenCart manual testing project

**BUG-001: Missing Confirm Password field on registration form**
Severity: Medium
Module: Registration
The registration form has a single Password field with no confirmation field. A user can mistype their password during signup with nothing to catch the error, potentially locking themselves out of their account.

**BUG-002: Error and validation messages are easy to miss**
Severity: Low
Module: Registration, Login
Validation and error messages render in the upper right corner of the page rather than inline near the relevant field. They are easy to overlook. This affected six of the ten executed test cases.

### practicesoftwaretesting.com (week 10 automation)

**BUG-003: Address autofill overwrites manually entered data**
Severity: Medium
Module: Registration
After the postcode lookup completes, it silently replaces the street, city, and state values the user has already typed, and in some cases overwrites the postal code and house number as well. There is no warning that the user's input has been changed. A data integrity issue.

**BUG-004: Address lookup race condition on submit**
Severity: Medium
Module: Registration
If the registration form is submitted while the address lookup is still running, the submission silently fails. The page stays on the registration screen with no error message or feedback to the user.

**BUG-005: Breached-password rejection with no client-side warning**
Severity: Low
Module: Registration
The server rejects passwords that appear in known data breach databases, but only after the form is submitted. The client-side password strength meter shows the password as valid up until the server rejects it, creating a confusing experience where a password marked acceptable is then refused.

---

## Technical and Environment Issues

Problems debugged while building and running the test suites. Not product defects, but documented for reference.

1. **Empty test file**: pytest collected zero tests because a test file had been saved as an empty (0 byte) file.

2. **Dropdown label mismatch**: The country dropdown selection failed because the option label was "United States of America (the)" rather than the assumed "United States."

3. **Fixture scope collision**: A custom `base_url` fixture collided with the reserved `base_url` fixture from the `pytest-base-url` plugin, causing ScopeMismatch errors in week5 and week6 on CI. Resolved by renaming the custom fixture to `api_base_url`.

4. **pytest rootdir config bleed**: Running multiple week folders in a single pytest command caused them all to inherit week4's `pytest.ini` and `conftest.py`. Resolved by running each week folder as its own separate pytest invocation.

5. **Angular render timing**: On slower CI runners, the registration form had not finished rendering before the test tried to interact with it. Resolved by waiting explicitly for the first field to be visible.

6. **Cloudflare bot blocking**: GitHub Actions runner IPs were served a Cloudflare bot challenge instead of the real page, so the week10 end-to-end tests could not run in CI. Resolved by marking those tests `local_only` and excluding them from the CI run.

7. **Transient 503s from httpbin.org**: The public test API intermittently returned 503 errors, failing auth tests. Resolved with pytest-rerunfailures retry logic.

8. **CI exit code 5**: The build failed when every week10 test was deselected and zero tests ran, because pytest returns exit code 5 for "no tests collected." Resolved by removing the redundant week10 line from the CI workflow.

9. **Allure import error in CI**: Adding `import allure` to the week10 tests crashed pytest collection in a workflow where the `allure-pytest` plugin was not installed, because pytest imports every test file during collection even for tests that will be deselected. Resolved by adding the plugin to that workflow's install step.

10. **Local environment setup**: A corrupted JAVA_HOME value and a PATH that was not picking up the Allure command-line tool were fixed while setting up Allure reporting.