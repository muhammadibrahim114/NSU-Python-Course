# ============================================================
# Task 1 — Personal Information
# ============================================================

print("Task 1 — Personal Information")

# input() always returns a string.
name = input("Enter your name: ")

# int() converts the string to a number so we can add 1 later.
age = int(input("Enter your age: "))

print(f"Hello, {name}!")
print(f"Next year you will be {age + 1} years old.")

print()