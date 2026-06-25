[![CI](https://github.com/vanessag0501/qa_automation_portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/vanessag0501/qa_automation_portfolio/actions/workflows/ci.yml/badge.svg) [![Playwright Tests](https://github.com/vanessag0501/qa_automation_portfolio/actions/workflows/playwright.yml/badge.svg)](https://github.com/vanessag0501/qa_automation_portfolio/actions/workflows/playwright.yml/badge.svg)

# QA Automation Portfolio

Built by **Vanessa Garcia**, a Software QA Tester transitioning into automation.

This repository documents a self-directed 16-week automation learning path, progressing from Python fundamentals through UI automation, API testing, SQL, performance testing, end-to-end automation, reporting, security testing, and CI/CD. It also includes a full manual testing engagement on a live e-commerce demo site.

---

## What's in here

| Week | Focus | Key Output |
|------|-------|------------|
| 1-2 | Python core | CSV test reporter that reads results and generates pass/fail summaries |
| 3 | Playwright UI | Automated form, checkbox, and radio button tests using Page Object Model |
| 4 | pytest structure | Full test suite with fixtures, conftest.py, custom markers, and auto-generated HTML reports |
| 5 | API automation | CRUD, schema validation, parametrized and chained API tests |
| 6 | Advanced API | Auth headers, bearer tokens, sessions, CSV-driven data tests, advanced fixtures and markers |
| 7 | SQL fundamentals | SQLite database with SELECT/WHERE/ORDER BY, aggregates, JOINs, subqueries, NULL handling |
| 8 | SQL + Postman/Newman | QA-focused data validation queries; Postman/Newman API collection integrated into CI |
| 9 | Performance testing | Locust load tests against a live REST API with multiple user scenarios |
| 10 | End-to-end automation | Registration and login flows automated with Page Object Model on a live e-commerce site |
| 11 | Test reporting | Allure reports with severity levels, step breakdowns, and screenshot-on-failure attachments |
| 12 | API security testing | Multi-target security header audit that reports findings and handles unreachable targets |
| - | Manual testing project | Full manual QA engagement on the OpenCart demo storefront: test plan, test cases, bug report, and execution summary |

---

## Tech stack

- **Python 3.13** for the core language
- **Playwright** for cross-browser UI automation
- **pytest** for the test runner, fixtures, parametrize, custom markers, and HTML reports
- **requests** for API and security testing
- **SQLite** for database querying and data validation
- **Postman / Newman** for API collection testing, integrated into CI
- **Locust** for performance and load testing
- **Allure** for rich, interactive test reporting
- **pytest-rerunfailures** for absorbing transient failures from flaky external services
- **GitHub Actions** for the CI/CD pipelines that run on every push

---

## Framework highlights

- **Page Object Model** keeps locators and interactions separated from test logic
- **End-to-end flows** automate full registration and login journeys, including handling an address autofill race condition and breached-password validation
- **Data-driven testing** uses parametrize with custom IDs and CSV-driven test cases
- **Custom markers** include `smoke`, `regression`, `security`, and a `local_only` marker for tests that cannot run on CI runner IPs
- **Auth testing** covers bearer tokens, basic auth, session management, and 401 validation
- **Request chaining** runs multi-step API flows (create, fetch, verify, delete)
- **SQL-based QA validation** covers duplicate detection, orphaned record checks, and JOIN-based data integrity queries
- **Performance testing** uses Locust scenarios covering GET and POST requests with response time and failure rate analysis
- **Allure reporting** adds severity levels, descriptive titles, labeled test steps, and automatic screenshot attachment on failure
- **Security auditing** checks HTTP security headers across multiple targets and reports findings rather than failing on weak security
- **External-service resilience** skips tests that depend on a third-party service when it returns a 503, so outages do not fail the build
- **Manual test documentation** includes a professional test plan, test case matrix, bug reports, and execution summary for a live application
- **Retry logic** uses pytest-rerunfailures so transient errors from public test APIs do not fail the build
- **CI pipelines** run automatically on every push to main

---

## Running the tests

**Requirements**

```
pip install requests pytest pytest-html playwright pytest-playwright locust pytest-rerunfailures allure-pytest
python -m playwright install
```

**UI tests (Playwright + POM)**

```
cd week4
python -m pytest -v
```

**API tests**

```
cd week5
python -m pytest test_posts_api.py -v

cd week6
python -m pytest test_suite.py -v
```

Run only smoke or regression tests:

```
python -m pytest -m smoke -v
python -m pytest -m regression -v
```

**SQL queries**

```
cd week7
python day1_queries.py
```

**Postman/Newman collection**

```
cd week8
newman run jsonplaceholder_collection.json -e jsonplaceholder_env.json
```

**Performance tests (Locust)**

```
cd week9
python -m locust -f locustfile.py
```

Then open `http://localhost:8089` to configure users, spawn rate, and start the load test.

**End-to-end tests (Playwright + POM)**

```
cd week10
python -m pytest -v -m local_only
```

These tests target practicesoftwaretesting.com, which blocks CI runner IPs via Cloudflare, so they are marked `local_only` and run locally rather than in CI.

**Allure reports**

Requires the Allure command-line tool and Java to be installed and on PATH.

```
cd week10
python -m pytest --alluredir=../week11/allure-results -m local_only --clean-alluredir
allure serve ../week11/allure-results
```

**Security header audit**

```
cd week12
python -m pytest test_security.py -v -m security -s
```

Results are written to `week12/security_audit_report.md`.

---

## Continuous integration

Two GitHub Actions workflows run on every push and pull request to main:

- **ci.yml** runs the week5 and week6 API test suites and publishes HTML reports as artifacts.
- **playwright.yml** runs the week4, week5, and week6 suites.

Each week folder runs as its own pytest invocation so each picks up its own `pytest.ini` and `conftest.py` without configuration bleeding between folders. Tests that depend on external services skip gracefully when those services are unavailable, so third-party outages do not turn the pipeline red.

---

## Key files

| File | What it does |
|------|----------------|
| `week2/day10_csv_test_reporter.py` | Reads a CSV of test results, outputs a formatted execution report |
| `week3/pages/text_box_page.py` | Page Object for DemoQA text box, locators and actions in one place |
| `week4/test_text_box.py` | pytest UI test using POM fixtures, parametrize, and markers |
| `week5/test_posts_api.py` | Full API test suite covering CRUD, schema, filters, 404, headers |
| `week6/test_suite.py` | Advanced API suite covering auth, sessions, fixtures, parametrize, custom markers |
| `week7/setup_db.py` | Builds the SQLite school database used for SQL practice queries |
| `week8/jsonplaceholder_collection.json` | Postman collection with assertions across multiple endpoints |
| `week9/locustfile.py` | Load test simulating concurrent users against a live REST API |
| `week10/pages/registration_page.py` | Page Object for the registration form, including address-lookup handling |
| `week10/test_registration.py` | End-to-end registration test with Allure steps and severity |
| `week10/test_login.py` | End-to-end login test that registers an account, logs in, and verifies the account page |
| `week11/README.md` | How to generate and view the Allure report |
| `week12/test_security.py` | Multi-target security header audit with findings report |
| `week12/security_audit_report.md` | Generated audit report comparing a secured site to a minimal one |
| `opencart-manual-testing/test-plan.md` | Manual test plan for the OpenCart demo storefront |
| `opencart-manual-testing/test-cases.xlsx` | Registration and login test cases with execution results |
| `opencart-manual-testing/bug-report.xlsx` | Logged defects found during manual testing |
| `BUGS.md` | Log of application defects and technical issues found across the portfolio |
| `.github/workflows/ci.yml` | GitHub Actions workflow that runs the API test suites on every push |
| `.github/workflows/playwright.yml` | GitHub Actions workflow that runs the Playwright and API suites on every push |

---

## About

I'm a Software QA Tester with a B.A. in Computer Science and ITIL v4 certification, building toward a full automation engineering skill set. This portfolio represents real, runnable code and documentation written as part of a structured self-study program.

[LinkedIn](https://www.linkedin.com/in/vanessa-garcia-ab090314b/) · [GitHub](https://github.com/vanessag0501)