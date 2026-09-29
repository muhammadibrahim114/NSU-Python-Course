"""
Lab 02 — Python Basics II

Topics:
- built-in functions
- assignment and augmented assignment
- operator precedence
- type conversion
- strings
- print() options
- collections
- mutable and immutable objects
- formatted output
- basic PEP 8
- reading common errors
"""


# ============================================================
# Task 1 — Built-in Functions
# ============================================================

print("Task 1 — Built-in Functions")

values = [12, 7, 19, 5, 14]

count = len(values)
smallest = min(values)
largest = max(values)
total = sum(values)
mean = total / count

print(f"Number of values: {count}")
print(f"Smallest value: {smallest}")
print(f"Largest value: {largest}")
print(f"Total: {total}")
print(f"Mean: {mean}")

print()


# ============================================================
# Task 2 — Absolute Value and Rounding
# ============================================================

print("Task 2 — Absolute Value and Rounding")

temperature_change = -7.438
measurement = 19.87654

absolute_temperature_change = abs(temperature_change)

print(f"Absolute value: {absolute_temperature_change}")
print(f"Rounded to 1 decimal place: {round(measurement, 1)}")
print(f"Rounded to 2 decimal places: {round(measurement, 2)}")
print(f"Rounded to 3 decimal places: {round(measurement, 3)}")

print()


# ============================================================
# Task 3 — Assignment and Augmented Assignment
# ============================================================

print("Task 3 — Assignment and Augmented Assignment")

balance = 1000.0

balance += 250
balance -= 120
balance *= 1.05

print(f"Final balance: {balance:.2f}")

print()


# ============================================================
# Task 4 — Operator Precedence
# ============================================================

print("Task 4 — Operator Precedence")

expression_1 = 2 + 3 * 4
expression_2 = (2 + 3) * 4
expression_3 = 20 / 5 + 3
expression_4 = 20 / (5 + 3)
expression_5 = 2 ** 3 ** 2

print(f"2 + 3 * 4 = {expression_1}")
print(f"(2 + 3) * 4 = {expression_2}")
print(f"20 / 5 + 3 = {expression_3}")
print(f"20 / (5 + 3) = {expression_4}")
print(f"2 ** 3 ** 2 = {expression_5}")

print()


# ============================================================
# Task 5 — Time Conversion
# ============================================================

print("Task 5 — Time Conversion")

total_seconds = int(input("Enter number of seconds: "))

minutes = total_seconds // 60
remaining_seconds = total_seconds % 60

print(
    f"{total_seconds} seconds = "
    f"{minutes} minute(s) and {remaining_seconds} second(s)"
)

print()


#print("Task 6 — Type Conversion")

# Original float with a fractional part.
value = 17.95

# int() chops off the decimal part — it does NOT round.
# int(17.95) -> 17   (not 18)
integer_value = int(value)
print(f"int(value): {integer_value}")     # 17

# Converting the int back to float gives 17.0, not 17.95.
# The fractional part is gone forever — the round trip
# is not reversible.
float_value = float(integer_value)
print(f"float(integer_value): {float_value}")     # 17.0

# str() converts a number into text.
# type() tells us the data type of the object.
text_value = str(integer_value)
print(f"Value as text: {text_value}")             # "17"
print(f"Type: {type(text_value)}")                # <class 'str'>

print()


# ============================================================
# Task 7 — Basic String Operations
# ============================================================

print("Task 7 — Basic String Operations")

first_name = input("First name: ")
last_name = input("Last name: ")

full_name = first_name + " " + last_name

print(f"Full name: {full_name}")
print(f"Number of characters: {len(full_name)}")
print(f"First character: {full_name[0]}")
print(f"Last character: {full_name[-1]}")
print(f"First three characters: {full_name[:3]}")

print(full_name * 3)

print()


# ============================================================
# Task 8 — Useful print() Options
# ============================================================

print("Task 8 — Useful print() Options")

language = "Python"
course = "AI and Big Data Analytics"
university = "NSU"

print(language, course, university, sep=" | ")

print("Python", end=" ")
print("Programming")

print()


# ============================================================
# Task 9 — Collections and Choosing Data Structures
# ============================================================

print("Task 9 — Collections")

student_name = "Anna"
student_age = 22
student_skills = ["Python", "Mathematics", "Machine Learning"]
student_university = "NSU"

student = {
    "name": student_name,
    "age": student_age,
    "skills": student_skills,
    "university": student_university,
}

print(f"Name: {student['name']}")
print(f"University: {student['university']}")
print(f"First skill: {student['skills'][0]}")
print(f"Number of skills: {len(student['skills'])}")

print()


# ============================================================
# Task 10 — Mutable and Immutable Objects
# ============================================================

print("Task 10 — Mutable and Immutable Objects")

# List example — mutable

numbers = [10, 20, 30]
same_numbers = numbers

numbers[0] = 99

print(f"numbers: {numbers}")
print(f"same_numbers: {same_numbers}")

# String example — immutable

text = "Python"
same_text = text

text = text + " Course"

print(f"text: {text}")
print(f"same_text: {same_text}")

print()


# ============================================================
# Task 11 — Small Statistics Report
# ============================================================

print("Task 11 — Small Statistics Report")

scores = [78, 92, 85, 69, 88]

score_count = len(scores)
minimum_score = min(scores)
maximum_score = max(scores)
total_score = sum(scores)
mean_score = total_score / score_count

print(f"Number of scores: {score_count}")
print(f"Minimum: {minimum_score}")
print(f"Maximum: {maximum_score}")
print(f"Mean: {mean_score:.2f}")

print()


# ============================================================
# Task 12 — PEP 8 Cleanup
# ============================================================

print("Task 12 — PEP 8 Cleanup")

price = 1250
quantity = 3
discount = 10

discount_amount = discount / 100 * price * quantity
final_total = price * quantity - discount_amount

print(f"Final: {final_total:.2f}")

print()


# ============================================================
# Optional Challenge — Student Score Summary
# ============================================================

print("Optional Challenge — Student Score Summary")

student_name = input("Student name: ")

score_1 = float(input("First score: "))
score_2 = float(input("Second score: "))
score_3 = float(input("Third score: "))

scores = [score_1, score_2, score_3]

minimum_score = min(scores)
maximum_score = max(scores)
mean_score = sum(scores) / len(scores)

print(f"Student: {student_name}")
print(f"Scores: {scores}")
print(f"Minimum: {minimum_score:.2f}")
print(f"Maximum: {maximum_score:.2f}")
print(f"Mean: {mean_score:.2f}")

print()


# ============================================================
# Task 13 — Multiple Assignment
# ============================================================

print("Task 13 — Multiple Assignment")

x, y, z = 10, 20, 30

print(f"x = {x}")
print(f"y = {y}")
print(f"z = {z}")

a = 5
b = 10

a, b = b, a

print(f"a = {a}")
print(f"b = {b}")

print()


# ============================================================
# Task 14 — String Methods
# ============================================================

print("Task 14 — String Methods")

text = "  Python Programming Course  "

cleaned_text = text.strip()

print(f"Without spaces: {cleaned_text}")
print(f"Lowercase: {cleaned_text.lower()}")
print(f"Uppercase: {cleaned_text.upper()}")
print(f"Replaced: {cleaned_text.replace('Course', 'Lab')}")

print(f"Starts with Python: {cleaned_text.startswith('Python')}")
print(f"Ends with Course: {cleaned_text.endswith('Course')}")

print()


# ============================================================
# Task 15 — Boolean Expressions
# ============================================================

print("Task 15 — Boolean Expressions")

age = 22
score = 85
is_master_student = True

print(f"age >= 18: {age >= 18}")
print(f"score >= 60: {score >= 60}")
print(
    f"score >= 60 and is_master_student: "
    f"{score >= 60 and is_master_student}"
)
print(f"score < 60 or age < 18: {score < 60 or age < 18}")
print(f"not is_master_student: {not is_master_student}")

print(f"bool(0): {bool(0)}")
print(f"bool(1): {bool(1)}")
print(f'bool(""): {bool("")}')
print(f'bool("Python"): {bool("Python")}')
print(f"bool([]): {bool([])}")
print(f"bool([1, 2]): {bool([1, 2])}")

print()


# ============================================================
# Task 16 — Membership
# ============================================================

print("Task 16 — Membership")

numbers = [10, 20, 30]
text = "Python Programming"

student = {
    "name": "Anna",
    "age": 22,
    "university": "NSU"
}

print(f"20 in numbers: {20 in numbers}")
print(f"40 in numbers: {40 in numbers}")

print(f'"Python" in text: {"Python" in text}')
print(f'"Java" in text: {"Java" in text}')

print(f'"name" in student: {"name" in student}')
print(f'"Anna" in student: {"Anna" in student}')

print()


# ============================================================
# Task 17 — Time Decomposition
# ============================================================

print("Task 17 — Time Decomposition")

total_seconds = int(input("Enter number of seconds: "))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600

minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(
    f"{total_seconds} seconds = "
    f"{hours} hour(s), {minutes} minute(s), and {seconds} second(s)"
)

print()


# ============================================================
# Task 18 — Order Invoice
# ============================================================

print("Task 18 — Order Invoice")

price_1 = float(input("Enter price for product 1: "))
quantity_1 = int(input("Enter quantity for product 1: "))

price_2 = float(input("Enter price for product 2: "))
quantity_2 = int(input("Enter quantity for product 2: "))

price_3 = float(input("Enter price for product 3: "))
quantity_3 = int(input("Enter quantity for product 3: "))

total_1 = price_1 * quantity_1
total_2 = price_2 * quantity_2
total_3 = price_3 * quantity_3

subtotal = total_1 + total_2 + total_3
tax = subtotal * 0.05
final_total = subtotal + tax

print(f"Product 1 total: {total_1:.2f}")
print(f"Product 2 total: {total_2:.2f}")
print(f"Product 3 total: {total_3:.2f}")
print(f"Subtotal: {subtotal:.2f}")
print(f"Tax (5%): {tax:.2f}")
print(f"Final total: {final_total:.2f}")

print()


# ============================================================
# Task 19 — Coordinate Analysis
# ============================================================

print("Task 19 — Coordinate Analysis")

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

point_1 = (x1, y1)
point_2 = (x2, y2)

delta_x = x2 - x1
delta_y = y2 - y1

squared_distance = delta_x ** 2 + delta_y ** 2
distance = squared_distance ** 0.5

print(f"Point 1: {point_1}")
print(f"Point 2: {point_2}")
print(f"Delta x: {delta_x}")
print(f"Delta y: {delta_y}")
print(f"Squared distance: {squared_distance}")
print(f"Distance: {distance:.2f}")

print()


# ============================================================
# Task 20 — Complex Numbers
# ============================================================

print("Task 20 — Complex Numbers")

z1 = 3 + 4j
z2 = 2 - 1j

print(f"z1: {z1}")
print(f"z2: {z2}")
print(f"Type of z1: {type(z1)}")

print(f"Addition: {z1 + z2}")
print(f"Subtraction: {z1 - z2}")
print(f"Multiplication: {z1 * z2}")
print(f"Division: {z1 / z2}")

print(f"Real part of z1: {z1.real}")
print(f"Imaginary part of z1: {z1.imag}")

print()


