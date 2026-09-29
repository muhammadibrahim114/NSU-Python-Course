# ============================================================
# Task 11 — Formatted Output
# ============================================================

print("Task 11 — Formatted Output")

radius = float(input("Enter the radius: "))

area = 3.14159 * radius ** 2

# :.2f -> exactly two digits after the decimal point.
print(f"Radius: {radius}")
print(f"Area: {area:.2f}")

print()