import requests
import pytest

# Collect findings across all checks and targets
findings = []


def record(target, check, passed, detail):
    findings.append({
        "target": target,
        "check": check,
        "status": "PASS" if passed else "FINDING",
        "detail": detail
    })


# The four targets: 
TARGETS = [
    "https://github.com",
    "https://httpbin.org",
    "http://neverssl.com",
    "https://example.com",
]


@pytest.fixture(params=TARGETS, scope="module")
def target_response(request):
    """Fetch each target once. Skip that target if it's unavailable."""
    url = request.param
    try:
        resp = requests.get(url, timeout=10)
    except requests.RequestException as e:
        pytest.skip(f"{url} unreachable: {e}")
    if resp.status_code != 200:
        pytest.skip(f"{url} returned {resp.status_code}, cannot audit")
    return url, resp


# ── Security Header Audit ─────────────────────────────────────────────
@pytest.mark.security
def test_content_type_options(target_response):
    """X-Content-Type-Options: nosniff prevents MIME-type sniffing."""
    url, resp = target_response
    value = resp.headers.get("X-Content-Type-Options")
    passed = value == "nosniff"
    record(url, "X-Content-Type-Options", passed, value or "header missing")
    assert True


@pytest.mark.security
def test_frame_options(target_response):
    """X-Frame-Options protects against clickjacking."""
    url, resp = target_response
    value = resp.headers.get("X-Frame-Options")
    passed = value is not None and value.upper() in ["DENY", "SAMEORIGIN"]
    record(url, "X-Frame-Options", passed, value or "header missing")
    assert True


@pytest.mark.security
def test_hsts(target_response):
    """Strict-Transport-Security enforces HTTPS."""
    url, resp = target_response
    value = resp.headers.get("Strict-Transport-Security")
    passed = value is not None
    record(url, "Strict-Transport-Security", passed, value or "header missing")
    assert True


@pytest.mark.security
def test_server_disclosure(target_response):
    """Server header should not reveal version details."""
    url, resp = target_response
    value = resp.headers.get("Server", "")
    passed = not any(char.isdigit() for char in value)
    record(url, "Server version disclosure", passed, value or "no Server header")
    assert True


# ── Report writer ─────────────────────────────────────────────────────
@pytest.mark.security
def test_write_report():
    """Write all collected findings to a grouped report file."""
    if not findings:
        pytest.skip("No findings collected (targets may be down)")

    lines = ["# Security Header Audit Report\n"]

    # Group findings by target
    targets = sorted(set(f["target"] for f in findings))
    for target in targets:
        lines.append(f"\n## {target}\n")
        for f in findings:
            if f["target"] == target:
                lines.append(f"- **{f['check']}**: {f['status']} ({f['detail']})")

    total = len(findings)
    flagged = sum(1 for f in findings if f["status"] == "FINDING")
    lines.append(f"\n---\n\n**Summary:** {flagged} findings across {total} checks.")

    with open("security_audit_report.md", "w") as out:
        out.write("\n".join(lines) + "\n")

    print(f"\nAudit complete: {flagged} findings out of {total} checks")
    assert True