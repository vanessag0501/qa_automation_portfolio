#Day 4 - Functions

#Basic Functions -wraps logic you'd otherwise repeat

def get_pass_rate(passed, total):
    if total == 0:
        return 0.0
    return round ((passed/total )*100, 1)

#function with a  default parameter

def get_verdict(pass_rate, threshold=80):
    if pass_rate >= threshold:
        return "Ready to release"
    elif pass_rate >=  60:
        return "Needs Review"
    else:
        return "Not ready"
    

#calling them
rate = get_pass_rate(6, 10)
print(f" Pass rate : {rate} %")
print(f" Verdict:  {get_verdict(rate)} ")

#default threshold is 80 but you can override it

print(f" Verdict at 60% threshold:{ get_verdict(rate, threshold=60 )}")

#functions that work with lists

def filter_by_status(test_case, results, target_status):
    filtered = []
    for i, status in enumerate (results):
        if status  == target_status:
            filtered.append(test_case[i])
    return filtered

def print_summary(test_cases, results):
    total = len(results)
    passed = len(filter_by_status(test_cases, results , "Pass"))
    failed = filter_by_status(test_cases,results, "Fail")
    blocked = filter_by_status(test_cases, results, "Blocked")
    
    rate =  get_pass_rate(passed, total)
    verdict = get_verdict (rate)

    print(f"\n--- Test Summary ---")
    print(f"Total   : {total}")
    print(f"Passed  : {passed}")
    print(f"Failed  : {len(failed)}")
    print(f"Blocked : {len(blocked)}")
    print(f"Rate    : {rate}%")
    print(f"Verdict : {verdict}")

    if failed:
        print(f"\nFailed tests:")
        for t in failed:
            print(f"  - {t}")


# Test it with your data
tests   = ["TC-001", "TC-002", "TC-003", "TC-004", "TC-005"]
results = ["Pass",   "Fail",   "Pass",   "Pass",   "Blocked"]

print_summary(tests, results)

# TO DO: Call filter_by_status on its own to print just the blocked tests
# Hint: print(filter_by_status(tests, results, "Blocked"))

print(filter_by_status(tests, results, "Blocked"))

