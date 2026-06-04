# OpenCart Manual Test Execution Summary

**Tester:** Vanessa Garcia
**Environment:** demo.opencart.com | Chrome | Windows
**Execution Date:** June 2026

## Scope
Functional manual testing of the Registration and Login modules on the OpenCart demo site.

## Results

| Total Test Cases | Passed | Failed | Blocked |
|-----------------|--------|--------|---------|
| 10              | 9      | 0      | 1       |

## Defects Found

| Bug ID  | Title                                                        | Severity |
|---------|--------------------------------------------------------------|----------|
| BUG-001 | Missing Confirm Password field on registration form          | Medium   |
| BUG-002 | Error and validation messages display in upper right corner  | Low      |

## Notes
- TC-003 was marked Blocked due to the absence of a Confirm Password field on the registration form. The test could not be executed as written.
- Error messages across both modules appear in the upper right corner of the page and are easy to overlook. This affects 6 of the 10 test cases.

## Conclusion
Core registration and login flows are functional. Two defects were identified and logged. No critical or high severity issues found.