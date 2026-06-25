[![CI](https://github.com/vanessag0501/qa_automation_portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/vanessag0501/qa_automation_portfolio/actions/workflows/ci.yml/badge.svg) [![Playwright Tests](https://github.com/vanessag0501/qa_automation_portfolio/actions/workflows/playwright.yml/badge.svg)](https://github.com/vanessag0501/qa_automation_portfolio/actions/workflows/playwright.yml/badge.svg)

# QA Automation Portfolio

Built by **Vanessa Garcia**, a Software QA Tester transitioning into automation.

This repository documents a self-directed 16-week automation learning path, progressing from Python fundamentals through UI automation, API testing, SQL, performance testing, end-to-end automation, reporting, security testing, mobile web testing, and CI/CD. It also includes a full manual testing engagement on a live e-commerce demo site.

Every week folder has its own README explaining what is in it and how to run it.

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
| 13 | Mobile web testing | Cross-device responsive tests using Playwright device emulation |
| - | Manual testing project | Full manual QA engagement on the OpenCart demo storefront: test plan, test cases, bug report, and execution summary |

---

## Tech stack

- **Python 3.13** for the core language
- **Playwright** for cross-browser UI automation and mobile device emulation
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
- **Cross-device testing** runs the same suite across emulated mobile devices using parametrized fixtures
- **Data-driven testing** uses parametrize with custom IDs and CSV-driven test cases
- **Custom markers** include `smoke`, `regression`, `security`, `mobile`, and a `local_only` marker for tests that cannot run on CI runner IPs
- **Auth testing** covers bearer tokens, basic auth, session management, and 401 validation
- **Request chaining** runs multi-step API flows (create, fetch, verify, delete)
- **SQL-based QA validation** covers duplicate detection, orphaned record checks, and JOIN-based data integrity queries
- **Performance testing** uses Locust scenarios covering GET and POST requests with response time and failure rate analysis
- **Allure reporting** adds severity levels, descriptive titles, labeled test steps, and automatic screenshot attachment on failure
- **Security auditing** checks HTTP security headers across multiple targets and reports findings rather than failing on weak security
- **External-service resilience** skips tests that depend on a third-party service when it returns a 503, so outages do not fail the build
- **Manual test documentation** includes a professional test plan, test case matrix, bug reports, and execution summary for a live application
- **CI pipelines** run automatically on every push to main

---

## Running the tests

**Requirements**

```
pip install requests pytest pytest-html playwright pytest-playwright locust pytest-rerunfailures allure-pytest
python -m playwright install
```

Each week folder has its own README with run instructions. A few common ones:

**UI tests (Playwright + POM)**
```
cd week4
python -m pytest -v
```

**API tests**
```
cd week5
python -m pytest test_posts_api.py -v
```

**Performance tests (Locust)**
```
cd week9
python -m locust -f locustfile.py
```

**End-to-end tests (local only, Cloudflare blocks CI)**
```
cd week10
python -m pytest -v -m local_only
```

**Security header audit**
```
cd week12
python -m pytest test_security.py -v -m security -s
```

**Mobile web tests**
```
cd week13
python -m pytest test_mobile.py -v -m mobile
```

---

## Continuous integration

Two GitHub Actions workflows run on every push and pull request to main:

- **ci.yml** runs the week5 and week6 API test suites and publishes HTML reports as artifacts.
- **playwright.yml** runs the week4, week5, week6, and week13 suites.

Each week folder runs as its own pytest invocation so each picks up its own `pytest.ini` and `conftest.py` without configuration bleeding between folders. Tests that depend on external services skip gracefully when those services are unavailable, so third-party outages do not turn the pipeline red. The week10 end-to-end tests are excluded from CI because the target site blocks runner IPs.

---

## Repository notes

- Build artifacts (`__pycache__/`, `.pytest_cache/`, Allure results and reports, generated HTML reports) are gitignored and not committed.
- `BUGS.md` at the repo root logs both the application defects found in the sites under test and the technical issues resolved while building the suites.

---

## Key documents

| File | What it does |
|------|----------------|
| `BUGS.md` | Log of application defects and technical issues found across the portfolio |
| `opencart-manual-testing/test-plan.md` | Manual test plan for the OpenCart demo storefront |
| `opencart-manual-testing/test-cases.xlsx` | Registration and login test cases with execution results |
| `opencart-manual-testing/bug-report.xlsx` | Logged defects found during manual testing |
| `week12/security_audit_report.md` | Generated security header audit comparing a secured site to a minimal one |
| `.github/workflows/ci.yml` | GitHub Actions workflow that runs the API test suites |
| `.github/workflows/playwright.yml` | GitHub Actions workflow that runs the Playwright and API suites |

---

## About

I'm a Software QA Tester with a B.A. in Computer Science and ITIL v4 certification, building toward a full automation engineering skill set. This portfolio represents real, runnable code and documentation written as part of a structured self-study program.

[LinkedIn](https://www.linkedin.com/in/vanessa-garcia-ab090314b/) · [GitHub](https://github.com/vanessag0501)