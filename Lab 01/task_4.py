# ============================================================
# Task 4 — Purchase Calculator
# ============================================================

print("Task 4 — Purchase Calculator")

quantity = int(input("Number of items: "))
price = float(input("Price per item: "))

# Total before discount, then apply a 10% discount.
total_price = quantity * price
discounted_price = total_price * 0.9     # keep 90% of the total

print(f"Total price: {total_price:.2f}")
print(f"After 10% discount: {discounted_price:.2f}")

print()