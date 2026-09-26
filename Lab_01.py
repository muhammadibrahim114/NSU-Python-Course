# Lab 01 — Python Basics

# Task 1 — Personal Information

print("Task 1 — Personal Information")

name = input("Enter your name: ")

age = int(input("Enter your age: "))

print(f"Hello, {name}!")
print(f"Next year you will be {age + 1} years old.")

print()


# ============================================================
# Task 2 — Rectangle
# ============================================================

print("Task 2 — Rectangle")

width = float(input("Enter width: "))
height = float(input("Enter height: "))

area = width * height

perimeter = 2 * (width + height)

print(f"Area: {area}")
print(f"Perimeter: {perimeter}")

print()

# ============================================================
# Task 3 — Temperature Converter
# ============================================================

print("Task 3 — Temperature Converter")

celsius = float(input("Enter Celsius temperature: "))

fahrenheit = celsius * 9 / 5 + 32

print(f"Fahrenheit: {fahrenheit}")

print()

# ============================================================
# Task 4 — Purchase Calculator
# ============================================================

print("Task 4 — Purchase Calculator")

quantity = int(input("Enter number of items: "))

price = float(input("Enter price of one item: "))

total_price = quantity * price

discounted_price = total_price * 0.90

print(f"Total price: {total_price}")
print(f"Price after 10% discount: {discounted_price}")

print()

# ============================================================
# Task 5 — Arithmetic Operators
# ============================================================

print("Task 5 — Arithmetic Operators")

a = 17
b = 5

print(f"Addition: {a + b}")
print(f"Subtraction: {a - b}")
print(f"Multiplication: {a * b}")
print(f"Division: {a / b}")
print(f"Floor division: {a // b}")
print(f"Remainder: {a % b}")
print(f"Power: {a ** b}")

print()


# ============================================================
# Task 6 — Data Types
# ============================================================

print("Task 6 — Data Types")

integer_value = 42
float_value = 3.14
complex_value = 2 + 3j
text_value = "Python"
boolean_value = True

print(type(integer_value))
print(type(float_value))
print(type(complex_value))
print(type(text_value))
print(type(boolean_value))

print()


# ============================================================
# Task 7 — Comparisons and Boolean Logic
# ============================================================

print("Task 7 — Comparisons and Boolean Logic")

a = 10
b = 5

print("a > b:", a > b)
print("a < b:", a < b)
print("a == b:", a == b)
print("a != b:", a != b)
print("a >= b:", a >= b)
print("a <= b:", a <= b)

print("a > 5 and b < 10:", a > 5 and b < 10)
print("a > 20 or b < 10:", a > 20 or b < 10)
print("not a < b:", not a < b)

print()


# ============================================================
# Task 8 — Python Collections
# ============================================================

print("Task 8 — Python Collections")

programming_languages = ["Python", "Java", "C++"]

numbers = (10, 20, 30)

cities = {"Novosibirsk", "Lagos", "Abuja"}

student = {
    "name": "Muhammad Ibrahim",
    "age": 26,
    "university": "Novosibirsk State University",
}

print(programming_languages)
print(numbers)
print(cities)
print(student)

print(type(programming_languages))
print(type(numbers))
print(type(cities))
print(type(student))

print()


# ============================================================
# Task 9 — Indexing and Slicing
# ============================================================

print("Task 9 — Indexing and Slicing")

numbers = [0, 1, 2, 3, 4, 5, 6, 7]

print("First element:", numbers[0])

print("Last element:", numbers[-1])

print("Elements from index 1 up to index 4:", numbers[1:4])

print("Every second element:", numbers[::2])


word = "Python"

print("First character:", word[0])

print("Last character:", word[-1])

print("First three characters:", word[:3])

print()


# ============================================================
# Task 10 — Dictionaries and Membership
# ============================================================

print("Task 10 — Dictionaries and Membership")

student = {
    "name": "Muhammad Ibrahim",
    "age": 26,
    "university": "Novosibirsk State University"
}

print("Student name:", student["name"])

print("Student age:", student["age"])

print("Student university:", student["university"])

print("name" in student)

print("email" in student)

print()


# ============================================================
# Task 11 — Formatted Output
# ============================================================

print("Task 11 — Formatted Output")

radius = float(input("Enter the radius of the circle: "))

area = 3.14159 * radius ** 2

print(f"Radius: {radius}")
print(f"Area: {area:.2f}")

print()


# ============================================================
# Task 12 — Trip Cost Calculator
# ============================================================

print("Task 12 — Trip Cost Calculator")

distance = float(input("Enter distance in kilometers: "))
fuel_consumption = float(input("Enter fuel consumption (liters per 100 km): "))
fuel_price = float(input("Enter fuel price per liter: "))

liters_needed = distance / 100 * fuel_consumption
trip_cost = liters_needed * fuel_price

print(f"Distance: {distance} km")
print(f"Fuel required: {liters_needed:.2f} liters")
print(f"Trip cost: {trip_cost:.2f}")

print()


