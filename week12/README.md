# Week 12 - API Security Testing

A security header audit built with pytest. It checks live sites for common security controls and reports findings rather than failing the build when a site is insecure.

## Contents
- `test_security.py` - the audit: checks X-Content-Type-Options, X-Frame-Options, HSTS, and server version disclosure across multiple targets
- `conftest.py`, `pytest.ini` - config and the security marker
- `security_audit_report.md` - the generated report

## How it works
A parametrized fixture fetches each target once and skips it if it is unreachable or returns a non-200 status. Each check records a PASS or FINDING, and a final step writes everything to a grouped report.

## Running
```
python -m pytest test_security.py -v -m security -s
```

## Notes
A false positive was found and fixed during development: the X-Frame-Options check originally did a case-sensitive comparison and flagged a valid lowercase `deny` value. The check now normalizes case before comparing.