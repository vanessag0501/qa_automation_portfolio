![CI](https://github.com/vanessag0501/qa_automation_portfolio/actions/workflows/ci.yml/badge.svg)

# QA Automation Portfolio

Built by **Vanessa Garcia** — Manual Software QA Tester transitioning into automation.

This repository documents a self-directed 8-week automation learning path,
progressing from Python fundamentals to a full UI + API test framework with
CI/CD integration.

---

## What's in here

| Week | Focus | Key Output |
|------|-------|------------|
| 1–2 | Python core | CSV test reporter that reads results and generates pass/fail summaries |
| 3 | Playwright UI | Automated form, checkbox, and radio button tests using Page Object Model |
| 4 | pytest structure | Full test suite with fixtures, conftest.py, and auto-generated HTML reports |
| 5 | API automation | CRUD, schema validation, parametrized and chained API tests |
| 6 | Advanced API | Auth headers, bearer tokens, sessions, CSV-driven data tests |
| 7–8 | CI/CD + polish | GitHub Actions pipeline, CI badge, portfolio documentation |

---

## Tech stack

- **Python 3.13** — core language
- **Playwright** — cross-browser UI automation
- **pytest** — test runner, fixtures, parametrize, HTML reports
- **requests** — API testing
- **GitHub Actions** — CI/CD pipeline that runs on every push

---

## Framework highlights

- **Page Object Model** — locators and interactions separated from test logic
- **Data-driven testing** — parametrize and CSV-driven test cases
- **Auth testing** — bearer tokens, basic auth, session management, 401 validation
- **Request chaining** — multi-step API flows (create → fetch → verify → delete)
- **Auto-generated reports** — HTML test reports produced on every run
- **CI pipeline** — tests run automatically on every push to main

---

## Running the tests

**Requirements**
```bash
pip install requests pytest pytest-html playwright pytest-playwright
python -m playwright install
```

**API tests**
```bash
cd "week 5"
python -m pytest test_posts_api.py -v

cd "week 6"
python -m pytest test_suite.py -v
```

**UI tests**
```bash
cd "week 4"
python -m pytest -v
```

---

## Key files

| File | What it does |
|------|-------------|
| `week 2/day10_csv_test_reporter.py` | Reads a CSV of test results, outputs a formatted execution report |
| `week 3/pages/text_box_page.py` | Page Object for DemoQA text box — locators + actions in one place |
| `week 4/test_text_box.py` | pytest UI test using POM fixtures |
| `week 5/test_posts_api.py` | Full API test suite — CRUD, schema, filters, 404, headers |
| `week 6/test_suite.py` | Advanced API suite — auth, sessions, parametrize, chaining |
| `.github/workflows/ci.yml` | GitHub Actions workflow — runs API tests on every push |

---

## About

I'm a QA Engineer with a B.S. in Computer Science and ITIL v4 certification,
building toward a full automation engineering skill set. This portfolio
represents real, runnable code written as part of a structured self-study
program.

[LinkedIn](https://www.linkedin.com/in/vanessa-garcia-ab090314b/) · [GitHub](https://github.com/vanessag0501)