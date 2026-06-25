# Week 6 - Advanced API Testing

Auth, sessions, data-driven tests, and advanced pytest patterns.

## Contents
- `test_suite.py` - the main suite: bearer and basic auth, sessions, schema validation, parametrized and chained requests
- `day26_auth_headers.py`, `day27_csv_driven.py` - the daily exercises
- `api_test_data.csv`, `post_payloads.csv` - data for the CSV-driven tests
- `conftest.py` - fixtures for base URLs, auth headers, payloads, and a reusable session client
- `pytest.ini` - config with retry logic for transient failures

## Targets
Tests run against jsonplaceholder.typicode.com and httpbin.org. The auth tests skip cleanly if httpbin returns a 503, so a third-party outage does not fail the build.

## Running
```
python -m pytest test_suite.py -v
```