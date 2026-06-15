[![CI](https://github.com/vanessag0501/qa_automation_portfolio/actions/workflows/ci.yml/badge.svg)](https://github.com/vanessag0501/qa_automation_portfolio/actions/workflows/ci.yml/badge.svg) [![Playwright Tests](https://github.com/vanessag0501/qa_automation_portfolio/actions/workflows/playwright.yml/badge.svg)](https://github.com/vanessag0501/qa_automation_portfolio/actions/workflows/playwright.yml/badge.svg)

# QA Automation Portfolio

Built by **Vanessa Garcia** — Software QA Tester transitioning into automation .

This repository documents a self-directed 16-week automation learning path, progressing from Python fundamentals through UI automation, API testing, SQL, performance testing, and CI/CD. It also includes a full manual testing engagement on a live e-commerce demo site.

---

## What's in here

| Week | Focus | Key Output |
|------|-------|------------|
| 1–2 | Python core | CSV test reporter that reads results and generates pass/fail summaries |
| 3 | Playwright UI | Automated form, checkbox, and radio button tests using Page Object Model |
| 4 | pytest structure | Full test suite with fixtures, conftest.py, custom markers, and auto-generated HTML reports |
| 5 | API automation | CRUD, schema validation, parametrized and chained API tests |
| 6 | Advanced API | Auth headers, bearer tokens, sessions, CSV-driven data tests, advanced fixtures and markers |
| 7 | SQL fundamentals | SQLite database with SELECT/WHERE/ORDER BY, aggregates, JOINs, subqueries, NULL handling |
| 8 | SQL + Postman/Newman | QA-focused data validation queries; Postman/Newman API collection integrated into CI |
| 9 | Performance testing | Locust load tests against a live REST API with multiple user scenarios |
| — | Manual testing project | Full manual QA engagement on the OpenCart demo storefront — test plan, test cases, bug report, and execution summary |

---

## Tech stack

- **Python 3.13** — core language
- **Playwright** — cross-browser UI automation
- **pytest** — test runner, fixtures, parametrize, custom markers, HTML reports
- **requests** — API testing
- **SQLite** — database querying and data validation
- **Postman / Newman** — API collection testing, integrated into CI
- **Locust** — performance and load testing
- **GitHub Actions** — CI/CD pipeline that runs on every push

---

## Framework highlights

- **Page Object Model** — locators and interactions separated from test logic
- **Data-driven testing** — parametrize with custom IDs, and CSV-driven test cases
- **Custom markers** — `smoke` and `regression` markers for selective test runs
- **Auth testing** — bearer tokens, basic auth, session management, 401 validation
- **Request chaining** — multi-step API flows (create → fetch → verify → delete)
- **SQL-based QA validation** — duplicate detection, orphaned record checks, JOIN-based data integrity queries
- **Performance testing** — Locust scenarios covering GET and POST requests with response time and failure rate analysis
- **Manual test documentation** — professional test plan, test case matrix, bug reports, and execution summary for a live application
- **Auto-generated reports** — HTML test reports produced on every run
- **CI pipeline** — tests run automatically on every push to main

---

## Running the tests

**Requirements**

```
pip install requests pytest pytest-html playwright pytest-playwright locust
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

---

## Key files

| File | What it does |
|------|----------------|
| `week2/day10_csv_test_reporter.py` | Reads a CSV of test results, outputs a formatted execution report |
| `week3/pages/text_box_page.py` | Page Object for DemoQA text box — locators + actions in one place |
| `week4/test_text_box.py` | pytest UI test using POM fixtures, parametrize, and markers |
| `week5/test_posts_api.py` | Full API test suite — CRUD, schema, filters, 404, headers |
| `week6/test_suite.py` | Advanced API suite — auth, sessions, fixtures, parametrize, custom markers |
| `week7/setup_db.py` | Builds the SQLite school database used for SQL practice queries |
| `week8/jsonplaceholder_collection.json` | Postman collection with assertions across multiple endpoints |
| `week9/locustfile.py` | Load test simulating concurrent users against a live REST API |
| `opencart-manual-testing/test-plan.md` | Manual test plan for the OpenCart demo storefront |
| `opencart-manual-testing/test-cases.xlsx` | Registration and login test cases with execution results |
| `opencart-manual-testing/bug-report.xlsx` | Logged defects found during manual testing |
| `.github/workflows/ci.yml` | GitHub Actions workflow — runs API tests on every push |
| `.github/workflows/playwright.yml` | GitHub Actions workflow — runs Playwright UI tests on every push |

---

## About

I'm a QA Engineer with a B.A. in Computer Science and ITIL v4 certification, building toward a full automation engineering skill set. This portfolio represents real, runnable code and documentation written as part of a structured self-study program.

[LinkedIn](https://www.linkedin.com/in/vanessa-garcia-ab090314b/) · [GitHub](https://github.com/vanessag0501)