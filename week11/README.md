# Week 11 - Test Reporting with Allure

Rich, interactive test reporting layered on top of the week 10 Playwright suite.

## What this demonstrates
- Allure report generation from pytest results
- Custom severity levels, titles, and descriptions on tests
- Step-by-step test breakdowns using `allure.step()`
- Automatic screenshot attachment on test failure

## Prerequisites
- `pip install allure-pytest`
- The Allure command-line tool installed and on PATH
- Java (required by the Allure CLI)

## Generating the report

Run the week 10 tests and output raw Allure results:
```
cd week10
python -m pytest --alluredir=../week11/allure-results -m local_only --clean-alluredir
```

Generate the static HTML report:
```
allure generate week11/allure-results -o week11/allure-report --clean
```

Or preview it live in the browser:
```
allure serve week11/allure-results
```

## Notes
- The week 10 tests target practicesoftwaretesting.com, which blocks CI runner IPs via Cloudflare, so they are marked `local_only` and run locally.
- `allure-results/` (raw data) and `allure-report/` (generated HTML) are build output and are gitignored rather than committed.