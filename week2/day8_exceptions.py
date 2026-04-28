# Day 8 - Exception handling 


# ── Part 1: Basic try/except recap ───────────────────────────────────

def read_number(value):
    try:
        return int(value)
    except ValueError:
        print(f" Could not convert '{value}' to a number.")
        return None

print(read_number("42"))  # works 42
print(read_number("abc")) # caught
print(read_number("3.14")) # caught - int() can't convert float string


# ── Part 2: Multiple exception types ─────────────────────────────────

def divide(a, b):
    try:
        result = a/b
        return round(result, 2)
    except ZeroDivisionError:
        print(" Cannot divide by zero.")
        return None
    except TypeError:
        print(f" Invalid types - expected numbers, got {type(a)} and {type(b)}.")
        return None

print(divide(10,2)) #5.0
print(divide(10,0)) #caught ZeroDivisionError
print(divide(10,"two")) #caught TypeError

# ── Part 3: finally ───────────────────────────────────────────────────

def open_test_file(filepath):
    f = None
    try:
        f = open(filepath, "r")
        contents = f.read()
        print(f"  File loaded — {len(contents)} characters")
        return contents
    except FileNotFoundError:
        print(f"  ERROR: '{filepath}' not found")
        return None
    except PermissionError:
        print(f"  ERROR: No permission to read '{filepath}'")
        return None
    finally:
        # finally ALWAYS runs — whether it worked or crashed
        if f:
            f.close()
            print("  File closed cleanly")
        print("  open_test_file() finished")

print("\n--- Loading existing file ---")
open_test_file("test_results.csv")

print("\n--- Loading missing file ---")
open_test_file("missing_file.csv")

# ── Part 4: Raising your own exceptions ──────────────────────────────

def validate_status(status):
    valid = ["Pass", "Fail", "Blocked", "Skipped"]
    if status not in valid:
        raise ValueError(f"Invalid status '{status}' — must be one of {valid}")
    return True

print("\n--- Validating statuses ---")
try:
    validate_status("Pass")
    print("  Pass is valid")
    validate_status("Maybe")   # this should raise
    print("  Maybe is valid")  # this should never print
except ValueError as e:
    print(f"  Caught: {e}")

# TODO: Call validate_status("Fail") and validate_status("Unknown")
# in their own try/except blocks and print what happens
try:
    validate_status("Fail")
    print ("Fail is valid")
    validate_status("Unknown")
    print("Unknown is not valid")
except ValueError as e:
    print(f" Caught: {e}" )