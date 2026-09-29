# ============================================================
# Task 12 — Trip Cost Calculator
# ============================================================

print("Task 12 — Trip Cost Calculator")

distance = float(input("Distance (km): "))
fuel_consumption = float(input("Fuel consumption (L per 100 km): "))
fuel_price = float(input("Fuel price per liter: "))

# Liters needed = (distance / 100) * consumption per 100 km.
liters_needed = distance / 100 * fuel_consumption

# Cost = liters * price per liter.
trip_cost = liters_needed * fuel_price

print(f"Distance: {distance} km")
print(f"Fuel required: {liters_needed:.2f} liters")
print(f"Trip cost: {trip_cost:.2f}")

print()