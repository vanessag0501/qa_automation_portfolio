# Week 13 - Mobile Web Testing

Mobile web testing using Playwright device emulation. Each test runs across several emulated devices to verify the mobile experience.

## Contents
- `test_mobile.py` - page load, viewport, mobile login with the hamburger menu, and add-to-cart
- `conftest.py` - a parametrized fixture that launches a browser context per device (iPhone 13, Pixel 5, Galaxy S9+)
- `pytest.ini` - config and the mobile marker

## Target
Tests run against saucedemo.com, which has a clear mobile layout including a hamburger menu that only appears on mobile viewports.

## Running
```
python -m pytest test_mobile.py -v -m mobileS
```

## Notes
This is mobile web testing on emulated devices, not native iOS or Android app testing. No Android SDK or emulator is required, so the suite runs anywhere Playwright runs, including CI.