#day 2 - variabels and data types

#strings
test_id = "TC-001"
test_title = "Valid user login"
status = "Pass"

#integers and floats
total_tests = 10
passed = 6
pass_rate = (passed / total_tests) * 100

#booleans
is_ready_for_release = pass_rate >= 80

#f-strings - how you'll format output in every script you write
print(f"Test: {test_id} - {test_title}")
print(f"Status: {status}")
print(f"Pass rate: {pass_rate}%")
print(f"Ready for release: {is_ready_for_release}")

#type () - tells you what kind of data something is
print(type(test_id))  # <class 'str'>
print(type(total_tests))  # <class 'int'>
print(type(pass_rate))  # <class 'float'>
print(type(is_ready_for_release))  # <class 'bool'>

#String methods - you'll use these constantly when parsing test data

print(status.upper())  # "PASS"
print(status.lower())  # "pass"
print(test_title.replace("Valid", "Invalid")) #swap a word
print(test_id.startswith("TC")) # True - useful for validating IDS

#Checking and converting types
score = "95" #this is a STRING, not a number
print(type(score))
print(int(score) + 5) #TO DO:run this - what error do you get? type error - can't add string and int together

print(float(score)) #95 to 95.0
print(str(pass_rate)) #60.0 to "60.0"
print(int(pass_rate)) #60.0 to 60 - note it rounds down, it doesn't round to nearest whole number

messy_status = "  Pass  "
print(messy_status.strip()) #removes whitespace from start and end of string
print(messy_status.strip()=="Pass") #now the comparison works - true 