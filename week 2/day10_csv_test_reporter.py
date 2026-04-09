# ─────────────────────────────────────────────
# DAY 10 CAPSTONE — CSV Test Reporter
# ─────────────────────────────────────────────
# WHAT YOU'LL PRACTICE:
#   file I/O, csv module, dictionaries, classes,
#   exception handling, f-strings, loops
#
# HOW TO RUN:
#   python day10_csv_test_reporter.py
#
# SAMPLE CSV FORMAT (save as test_results.csv):
#   TC ID,Title,Status
#   TC-001,Valid login,Pass
#   TC-002,Invalid password,Fail
#   TC-003,Empty fields,Pass
#   TC-004,Duplicate email,Blocked
#   TC-005,Mobile layout,Fail
#
# TIP: Export your test cases spreadsheet tab as CSV and use that!
# ─────────────────────────────────────────────

import csv
from datetime import date


# ── Data class to hold a single test result ──────────────────────────
class TestResult:
    def __init__(self, tc_id, title, status):
        self.tc_id  = tc_id
        self.title  = title
        # Normalise status so "pass", "PASS", "Pass" all match
        self.status = status.strip().capitalize()

    def is_pass(self):
        return self.status == "Pass"

    def is_fail(self):
        return self.status == "Fail"

    # TODO:  is_blocked() and is_skipped() methods yourself
    # Hint: copy the pattern from is_pass() above
    def is_blocked(self):
        return self.status == "Blocked"
    def is_skipped(self):
        return self.status == "Skipped"


# ── Load results from CSV ─────────────────────────────────────────────
def load_results(filepath):
    results = []

    # TODO: What happens if the file doesn't exist?
    # This is where you practice try/except — wrap the open() call
    try:
        with open(filepath, newline="", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # TODO: What if a row is missing the Status column?
                # Hint: use row.get("Status", "Unknown") as a safe fallback
                result = TestResult(
                    tc_id  = row["TC ID"],
                    title  = row["Title"],
                    status = row["Status"]
                )
                results.append(result)
    except FileNotFoundError:
        print(f"\n  ERROR: File '{filepath}' not found.")
        print("  Make sure the CSV is in the same folder as this script.\n")
        return []
    except KeyError as e:
        print(f"\n  ERROR: Missing expected column {e} in CSV.")
        print("  Check your CSV headers match: TC ID, Title, Status\n")
        return []

    return results


# ── Summarise results into a dictionary ──────────────────────────────
def summarise(results):
    counts = {"Pass": 0, "Fail": 0, "Blocked": 0, "Skipped": 0, "Other": 0}

    for r in results:
        if r.status in counts:
            counts[r.status] += 1
        else:
            # TODO: Print a warning for unexpected status values
            counts["Other"] += 1
            print(f"  WARNING: Unexpected status '{r.status}' found for test case '{r.tc_id}'.")

    return counts


# ── Calculate pass rate ───────────────────────────────────────────────
def pass_rate(counts):
    total = sum(counts.values())
    if total == 0:
        return 0.0
    return round((counts["Pass"] / total) * 100, 1)


# ── Print the report to terminal ──────────────────────────────────────
def print_report(results, counts, rate, filepath, sprint_name=""):
    total = sum(counts.values())
    today = date.today().strftime("%Y-%m-%d")

    print("\n" + "=" * 48)
    print(f"  QA TEST EXECUTION REPORT")
    if sprint_name:
        print(f"  Sprint     : {sprint_name}")
    print(f"  Generated : {today}")
    print(f"  Source    : {filepath}")
    print("=" * 48)
    print(f"  Total cases  : {total}")
    print(f"  Passed       : {counts['Pass']}")
    print(f"  Failed       : {counts['Fail']}")
    print(f"  Blocked      : {counts['Blocked']}")
    print(f"  Skipped      : {counts['Skipped']}")
    print(f"  Pass rate    : {rate}%")
    print("-" * 48)

    # Print failed test cases so they're easy to spot
    failed = [r for r in results if r.is_fail()]
    if failed:
        print(f"\n  FAILED TESTS ({len(failed)}):")
        for r in failed:
            print(f"    - [{r.tc_id}] {r.title}")

    # TODO CHALLENGE: Also print blocked tests the same way

    print("\n" + "=" * 48 + "\n")

    blocked = [r for r in results if r.is_blocked()]
    if blocked:
        print(f"\n BLOCKED TESTS ({len(blocked)}):")
        for r in blocked:
            print(f"    - [{r.tc_id}] {r.title}")


# ── Save report to a .txt file ────────────────────────────────────────
def save_report(counts, rate, filepath):
    today = date.today().strftime("%Y-%m-%d")
    output_file = f"qa_report_{today}.txt"

    # TODO: Expand this to write more detail — failed test titles etc.
    with open(output_file, "w") as f:
        f.write(f"QA Test Report — {today}\n")
        f.write(f"Source: {filepath}\n\n")
        for status, count in counts.items():
            f.write(f"{status}: {count}\n")
        f.write(f"\nPass rate: {rate}%\n")
        

    print(f"  Report saved to: {output_file}\n")


# ── Main ──────────────────────────────────────────────────────────────
def main():
    print("\n--- QA CSV Test Reporter ---")

    filepath = input("\nEnter CSV filename (or press Enter for 'test_results.csv'): ").strip()
    if not filepath:
        filepath = "test_results.csv"

    results = load_results(filepath)
    if not results:
        print("No results to report. Exiting.")
        return

    counts = summarise(results)
    rate   = pass_rate(counts)

    sprint_name = input("Enter sprint name (or press Enter to skip): ").strip()

    print_report(results, counts, rate, filepath, sprint_name)

    save_txt = input("Save report to a .txt file? (y/n): ").strip().lower()
    if save_txt == "y":
        save_report(counts, rate, filepath)

    save_csv = input("Save report to a .csv file? (y/n): ").strip().lower()
    if save_csv == "y":
        output_csv = f"qa_report_{date.today().strftime('%Y-%m-%d')}.csv"
        with open(output_csv, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Status", "Count"])
            for status, count in counts.items():
                writer.writerow([status, count])
            writer.writerow(["Pass Rate", f"{rate}%"])
        print(f"  Report saved to: {output_csv}\n")

main()