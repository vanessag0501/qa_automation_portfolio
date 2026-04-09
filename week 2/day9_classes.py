# Day 9 Classes and OOP


# ── Part 1: Basic class ───────────────────────────────────────────────
class TestCase:

    def __init__(self, tc_id, title, status, priority):
        self.tc_id = tc_id
        self.title = title
        self.status = status
        self.priority = priority
    
    def is_pass(self):
        return self.status == "Pass"
    
    def is_fail (self):
        return self.status == "Fail"
    
    def is_blocked(self):
        return self.status == "Blocked"
    
    def summary (self):
        return f"[{self.tc_id}] {self.title} - {self.status} ({self.priority})"
    

#Creating instances

tc1 = TestCase("TC-001", "Valid login",            "Pass", "High")
tc2 = TestCase("TC-002", "Invalid password", "Fail", "High")
tc3 = TestCase("TC-003", "Empty fields",  "Pass", "Medium")


#Using the class
print(tc1.summary()) # [TC-001] Valid login - Pass (High)
print(tc2.summary()) # [TC-002] Invalid password - Fail (High)

print(f" TC-001 Passed: {tc1.is_pass()}") #True
print(f" TC-002 Failed: {tc2.is_fail()}") #True

# A list of TestCase objects
suite = [tc1, tc2, tc3]

for tc in suite:
    print(tc.summary())

    # ── Part 2: A class that uses another class ───────────────────────────

class TestSuite:
    def __init__(self, name):
        self.name  = name
        self.tests = []

    def add(self, test_case):
        self.tests.append(test_case)

    def total(self):
        return len(self.tests)

    def passed(self):
        return [t for t in self.tests if t.is_pass()]

    def failed(self):
        return [t for t in self.tests if t.is_fail()]
    
    def blocked(self):
        return [t for t in self.tests if t.is_blocked()]
    
    def pass_rate(self):
        if self.total() == 0:
            return 0.0
        return round(len(self.passed()) / self.total() * 100, 1)

    def report(self):
        print(f"\n--- {self.name} ---")
        print(f"Total   : {self.total()}")
        print(f"Passed  : {len(self.passed())}")
        print(f"Failed  : {len(self.failed())}")
        print(f"Blocked : {len(self.blocked())}")
        print(f"Rate    : {self.pass_rate()}%")
        if self.failed():
            print("\nFailed tests:")
            for t in self.failed():
                print(f"  - {t.summary()}")
        if self.blocked():
            print("\nBlocked Tests:")
            for t in self.blocked():
                print(f" - {t.summary()}")


# Build a suite and run the report
suite = TestSuite("Sprint 12 — Login Module")
suite.add(TestCase("TC-001", "Valid login",       "Pass", "High"))
suite.add(TestCase("TC-002", "Invalid password",  "Fail", "High"))
suite.add(TestCase("TC-003", "Empty fields",      "Pass", "Medium"))
suite.add(TestCase("TC-004", "Duplicate email",   "Pass", "High"))
suite.add(TestCase("TC-005", "Password strength", "Blocked", "Low"))

suite.report()

# TODO: Add is_blocked() to TestCase, then add a blocked() method
# to TestSuite that returns blocked tests, and print them in report()