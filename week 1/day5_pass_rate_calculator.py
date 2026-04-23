# ─────────────────────────────────────────────
# DAY 5 MINI PROJECT — Test Result Calculator
# ─────────────────────────────────────────────
# WHAT YOU'LL PRACTICE:
#   variables, input(), if/else, functions, f-strings
#
# HOW TO RUN:
#   python day5_pass_rate_calculator.py
# ─────────────────────────────────────────────

def calculate_pass_rate(passed, failed, blocked, skipped):
    total = passed + failed + blocked + skipped

    # TODO: What should happen if total is 0?
    # Hint: you don't want to divide by zero — add an if check here
    if total == 0:
        return None

    pass_rate = (passed / total) * 100
    return round(pass_rate, 1)


def get_verdict(pass_rate):
    # TODO: Try adjusting these thresholds to match your team's standards
    if pass_rate >= 80:
        return "READY TO RELEASE"
    elif pass_rate >= 60:
        return "NEEDS REVIEW"
    else:
        return "NOT READY — TOO MANY FAILURES"


def print_report(sprint, passed, failed, blocked, skipped, pass_rate):
    total = passed + failed + blocked + skipped
    verdict = get_verdict(pass_rate)

    print("\n" + "=" * 40)
    print(f"  TEST SUMMARY — {sprint}")
    print("=" * 40)
    print(f"  Total test cases : {total}")
    print(f"  Passed           : {passed}")
    print(f"  Failed           : {failed}")
    print(f"  Blocked          : {blocked}")
    print(f"  Skipped          : {skipped}")
    print(f"  Pass rate        : {pass_rate}%")
    print(f"  Verdict          : {verdict}")
    print("=" * 40 + "\n")

def get_number(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("  Please enter a positive number.")
                continue
            return value
        except ValueError:
            print("  Invalid input — please enter a number.")

def main():
    print("\n--- QA Test Result Calculator ---\n")

    sprint = input("Sprint or release name: ").strip()

    # TODO: Add input validation — what if someone types "abc" instead of a number?
    # Hint: look up int() and how it raises a ValueError
    passed  = get_number("How many passed?  ")
    failed  = get_number("How many failed?  ")
    blocked = get_number("How many blocked? ")
    skipped = get_number("How many skipped? ")

    pass_rate = calculate_pass_rate(passed, failed, blocked, skipped)

    if pass_rate is None:
        print("\nNo test cases entered. Nothing to report.")
        return

    print_report(sprint, passed, failed, blocked, skipped, pass_rate)

    # TODO CHALLENGE: Save the report to a .txt file
    # Hint: open("report.txt", "w") as f: then f.write(...)
    total = passed + failed + blocked + skipped
    verdict = get_verdict(pass_rate)

    with open("report.txt", "w") as f:
        f.write(
            f"TEST SUMMARY — {sprint}\n"
            f"Total test cases : {total}\n"
            f"Passed           : {passed}\n"
            f"Failed           : {failed}\n"
            f"Blocked          : {blocked}\n"
            f"Skipped          : {skipped}\n"
            f"Pass rate        : {pass_rate}%\n"
        f"Verdict          : {verdict}\n")


main()
