# Week 4 - pytest Structure

Turns the week 3 scripts into a properly structured pytest suite with fixtures, config, and reports.

## Contents
- `test_checkbox.py`, `test_radio_button.py`, `test_text_box.py` - UI tests using the Page Object Model
- `pages/` - Page Objects shared by the tests
- `conftest.py` - shared fixtures
- `pytest.ini` - config and custom markers (smoke, regression)

## Target
Tests run against demoqa.com.

## Running
```
python -m pytest -v
```

Run a subset by marker:
```
python -m pytest -m smoke -v
```