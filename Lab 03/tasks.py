# ============================================================
# Task 1 — Positive, negative, or zero
# ============================================================

print("Task 1 — Positive, negative, or zero")

number = int(input("Enter an integer: "))

if number > 0:
    print("Positive")
elif number < 0:
    print("Negative")
else:
    print("Zero")

print()


# ============================================================
# Task 2 — Age category
# ============================================================

print("Task 2 — Age category")

age = int(input("Enter your age: "))

if age < 13:
    print("Child")
elif age < 18:
    print("Teenager")
elif age < 65:
    print("Adult")
else:
    print("Senior")

print()


# ============================================================
# Task 3 — Grade classifier
# ============================================================

print("Task 3 — Grade classifier")

score = float(input("Enter your score: "))

if score < 0 or score > 100:
    print("Invalid score")
elif score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else:
    print("Fail")

print()


# ============================================================
# Task 4 — Access decision
# ============================================================

print("Task 4 — Access decision")

age = int(input("Enter your age: "))
has_ticket = input("Do you have a ticket? (yes/no): ")

if age < 18:
    print("Must be 18 or older")
elif has_ticket == "yes":
    print("Access granted")
else:
    print("Ticket required")

print()


# ============================================================
# Task 5 — Even numbers with range
# ============================================================

print("Task 5 — Even numbers with range")

for number in range(2, 31, 2):
    print(number)

print()


