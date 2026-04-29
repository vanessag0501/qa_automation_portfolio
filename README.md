![CI](https://github.com/vanessag0501/qa_automation_portfolio/actions/workflows/ci.yml/badge.svg)

# QA Automation Portfolio
**Vanessa Garcia**

A full UI and API automation framework built with Python, Playwright, and pytest.

## Tech Stack
- Python 3.13
- Playwright — UI automation
- pytest — test runner
- requests — API testing
- GitHub Actions — CI/CD

## Structure
- `week 1-2` — Python foundations + CSV test reporter
- `week 3` — Playwright UI tests + Page Object Model
- `week 4` — pytest suite with HTML reports
- `week 5` — API automation (CRUD, schema, parametrize, chaining)
- `week 6` — Advanced API (auth, sessions, CSV-driven tests)

## Running the tests
```bash
# API tests
cd "week 5"
python -m pytest test_posts_api.py -v

# UI tests
cd "week 4"
python -m pytest -v
```