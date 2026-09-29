# ============================================================
# Task 10 — Dictionaries and Membership
# ============================================================

print("Task 10 — Dictionaries and Membership")

student = {
    "name": "Anna",
    "age": 22,
    "city": "Novosibirsk",
}

print(student["name"])
print(student["age"])

# `in` on a dict checks KEYS, not values.
print("age" in student)         # True
print("email" in student)       # False

numbers = [10, 20, 30, 40]

print(20 in numbers)            # True
print(50 in numbers)            # False

print()