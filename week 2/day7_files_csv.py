# Day 7 - Reading and writing files + CSV
import csv

#Part 1 - Basic file writing 

with open("notes.txt", "w") as f:
    f.write("QA Automation Study Log \n")
    f.write("Day 7 - files and CSV\n")
    f.write("Status: In progress \n")

# Reading it back
with open("notes.txt",  "r") as f: 
    contents = f.read()
    print(contents)

# Reading line by line - useful for large files
with open ("notes.txt", "r") as f:
    for line in f:
        print(line.strip()) #strip() removes extra whitespace
          

# ── Part 2: Writing a CSV ─────────────────────────────────────────────

with open("test_results.csv", "w", newline="") as f:
    writer = csv.writer(f)

    # Write the header row first
    writer.writerow(["TC ID", "Title", "Status", "Priority"])

    # Write data rows
    writer.writerow(["TC-001", "Valid login",       "Pass",    "High"])
    writer.writerow(["TC-002", "Invalid password",  "Fail",    "High"])
    writer.writerow(["TC-003", "Empty fields",      "Pass",    "Medium"])
    writer.writerow(["TC-004", "Duplicate email",   "Pass",    "High"])
    writer.writerow(["TC-005", "Password strength", "Blocked", "Low"])

print("CSV written successfully")

# ── Part 3: Reading a CSV ─────────────────────────────────────────────

with open("test_results.csv", "r") as f:
    reader = csv.DictReader(f)   # DictReader makes each row a dictionary
    for row in reader:
        print(f"[{row['TC ID']}] {row['Title']} — {row['Status']}")

# ── Part 4: Reading and filtering ────────────────────────────────────

print("\n--- Failed or Blocked tests ---")
with open("test_results.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Status"] in ["Fail", "Blocked"]:
            print(f"  [{row['TC ID']}] {row['Title']} — {row['Priority']} priority")

# TODO: Read the CSV and count how many High priority tests exist
# Hint: use a counter variable and increment it inside the loop
print("\n--- High priority tests ---")
high_priority_count = 0
with open("test_results.csv", "r") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row["Priority"] in ["High"]:
            high_priority_count += 1
            print(f"[{row['TC ID']}] {row['Title']} — {row['Priority']} priority")
