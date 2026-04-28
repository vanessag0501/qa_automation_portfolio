# # Day 3 Lists and Loops

# # A list is just a collection of items in order

# test_ids= ["TC-001", "TC-002", "TC-003", "TC-004", "TC-005"]
# statuses = ["Pass", "Fail", "Pass", "Pass", "Blocked"]

# #Accessing items - index starts at 0 not 1 

# print(test_ids[0]) #TC-001
# print(test_ids[-1]) #TC-005 - negative index counts backwards from end of list
# print(test_ids[1:3]) #slice - items at index 1 and 2 only - TC-002 and TC-003

# #basic list info
# print(len(test_ids)) #how many items in the list? 5

# #looping through lists - for each item in the list, do something
# for test in test_ids:
#     print(test)

# # Looping with index - when you need to know the position too
# for i, test in enumerate(test_ids):
#     print(f"{i} - {test}")

# #print("END")



# #loop 2 lists together - status per test
# for i, test in enumerate(test_ids):
#     print(f"{test} - {statuses[i]}")
    
# #print("2 lists above")

# #filtering - only show failed tests
# print("\nFailed tests:")
# for i, status in enumerate(statuses):
#     if status == "Fail":
#         print(f"{test_ids[i]} - Failed")

# #Counting statues
# pass_count = 0
# for status in statuses:
#     if status == "Pass":
#         pass_count += 1
# print(f"Total passed: {pass_count} out of {len(statuses)}")

# #adding and removing from a list
# statuses.append("Fail")
# test_ids.append("TC-006")
# print(f"\nAfter adding TC-006: {test_ids}")

#putting it all together - a mini status summary

test_cases = ["TC-001", "TC-002", "TC-003", "TC-004", "TC-005"]
results = ["Pass", "Fail", "Pass", "Pass", "Blocked"]

summary = {"Pass": [], "Fail": [], "Blocked": [], "Skipped": []}

for i, status in enumerate(results):
    if status in summary:
        summary[status].append(test_cases[i])

#print each group
for status, tests in summary.items():
    print(f"\n{status} ({len(tests)}):")
    for t in tests:
        print(f" - {t}")

# TO DO: Calculate and print the pass rate using what you learned in Day 2
# Hint: len(summary["Pass"]) gives you the pass count
pass_rate = (len(summary["Pass"])/ len(test_cases)) * 100
print(f" Pass rate is {pass_rate}")