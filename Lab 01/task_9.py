# ============================================================
# Task 9 — Indexing and Slicing
# ============================================================

print("Task 9 — Indexing and Slicing")

numbers = [0, 1, 2, 3, 4, 5, 6, 7]

print(numbers[0])       # first element
print(numbers[-1])      # last element via negative index
print(numbers[1:4])     # from index 1 up to (not including) 4 -> [1, 2, 3]
print(numbers[::2])     # every second element -> [0, 2, 4, 6]

word = "Python"

print(word[0])          # 'P'
print(word[-1])         # 'n'
print(word[:3])         # 'Pyt'

print()