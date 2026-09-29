# ============================================================
# Task 1 — Countdown with while
# ============================================================

print("Task 1 — Countdown with while")

number = int(input("Enter a positive integer: "))

while number >= 1:
    print(number)
    number -= 1

print("Go!")

print()


# ============================================================
# Task 2 — Repeat until zero
# ============================================================

print("Task 2 — Repeat until zero")

number = int(input("Enter an integer: "))

count = 0
total = 0

while number != 0:
    count += 1
    total += number

    number = int(input("Enter an integer: "))

print(f"Count: {count}")
print(f"Sum: {total}")

print()

# ============================================================
# Task 3 — Valid input with while True
# ============================================================

print("Task 3 — Valid input with while True")

while True:
    number = int(input("Enter an integer from 1 to 10: "))

    if number < 1 or number > 10:
        print("Invalid value")
    else:
        print("Accepted")
        break

print()


# ============================================================
# Task 4 — continue in a while loop
# ============================================================

print("Task 4 — continue in a while loop")

number = 1

while number <= 20:
    if number % 3 == 0:
        number += 1
        continue

    print(number)
    number += 1

print()


# ============================================================
# Task 5 — Search with loop else
# ============================================================

print("Task 5 — Search with loop else")

numbers = [4, 8, 12, 16, 21, 24]

for number in numbers:
    if number % 2 != 0:
        print(f"First odd number: {number}")
        break
else:
    print("All values are even")

print()