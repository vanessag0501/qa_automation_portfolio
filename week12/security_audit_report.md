# Security Header Audit Report


## https://example.com

- **X-Content-Type-Options**: FINDING (header missing)
- **X-Frame-Options**: FINDING (header missing)
- **Strict-Transport-Security**: FINDING (header missing)
- **Server version disclosure**: PASS (cloudflare)

## https://github.com

- **X-Content-Type-Options**: PASS (nosniff)
- **X-Frame-Options**: PASS (deny)
- **Strict-Transport-Security**: PASS (max-age=31536000; includeSubdomains; preload)
- **Server version disclosure**: PASS (github.com)

---

**Summary:** 3 findings across 8 checks.
