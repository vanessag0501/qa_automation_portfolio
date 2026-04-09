#Day 6- Dictionaries
# A dictionary stores key-value pairs - like a mini database

test_case ={
    "id": "TC-001",
    "title": " Valid user login",
    "status": "Pass",
    "priority": "High",
    "assignee": "your-name",
}

#Accessing values
print(test_case["id"]) #TC-001
print(test_case["status"])

#Safe access with get() - returns None if key doesn't exist instead of error
print(test_case.get("envrionment")) #None
print(test_case.get("environment", "N/A")) #N/A - default value if key not found

#Adding and updating 
test_case["environment"] = "Chrome/Windows"
test_case["status"] = "Fail" #update existing key
print(test_case)

#Looping over a dictionary
print("\nTest case details:")
for key, value in test_case.items():
    print(f" {key} : {value}")

# A list of dictionaries — this is how real test data looks
test_suite = [
    {"id": "TC-001", "title": "Valid login",         "status": "Pass",    "priority": "High"},
    {"id": "TC-002", "title": "Invalid password",    "status": "Fail",    "priority": "High"},
    {"id": "TC-003", "title": "Empty fields",        "status": "Pass",    "priority": "Medium"},
    {"id": "TC-004", "title": "Duplicate email",     "status": "Pass",    "priority": "High"},
    {"id": "TC-005", "title": "Password strength",   "status": "Blocked", "priority": "Low"},
]

# Loop and filter
print("\n--- High priority failures ---")
for test in test_suite:
    if test["status"] == "Fail" and test["priority"] == "High":
        print(f"  [{test['id']}] {test['title']}")

# Build a summary dictionary from the list
summary = {}
for test in test_suite:
    status = test["status"]
    if status not in summary:
        summary[status] = 0
    summary[status] += 1

print(f"\n--- Status summary ---")
for status, count in summary.items():
    print(f"  {status}: {count}")

# TO DO: Calculate and print the pass rate from the summary dictionary
# Hint: summary.get("Pass", 0) gives you the pass count safely

pass_rate = summary.get("Pass",0) / len(test_suite) * 100
print(f" Test pass rate: {pass_rate}%")