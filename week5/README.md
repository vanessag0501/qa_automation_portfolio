# Week 5 - API Automation

API testing with requests and pytest, covering the full CRUD cycle and validation.

## Contents
- `test_posts_api.py` - the main suite: CRUD, schema validation, filtering, 404 handling, response headers
- `day21_first_api.test.py` through `day25_chaining.py` - the daily build-up exercises
- `conftest.py` - fixtures including the API base URL and a sample payload
- `pytest.ini` - config

## Target
Tests run against jsonplaceholder.typicode.com.

## Running
```
python -m pytest test_posts_api.py -v
```