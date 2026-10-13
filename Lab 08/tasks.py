
from pathlib import Path
import re

# ============================================================
# Folder paths
# ============================================================
BASE_DIR = Path(__file__).resolve().parent
DATA = BASE_DIR / "data"
OUTPUT = BASE_DIR / "output"


# ============================================================
# Task 1 — Read a whole file
# ============================================================
path = DATA / "note.txt"

with open(path, "r", encoding="utf-8") as file:
    content = file.read()

print(content)
print(len(content))


# ============================================================
# Task 2 — Read two lines
# ============================================================
path = DATA / "note.txt"

with open(path, "r", encoding="utf-8") as file:
    line1 = file.readline()
    line2 = file.readline()

print(repr(line1))
print(repr(line2))


# ============================================================
# Task 3 — Read lines into a list
# ============================================================
path = DATA / "names.txt"

with open(path, "r", encoding="utf-8") as file:
    lines = file.readlines()

print(len(lines))

if lines:
    print(lines[-1].strip())


# ============================================================
# Task 4 — Count nonblank lines
# ============================================================
count = 0

with open(DATA / "names.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.strip():
            count += 1

print(count)


# ============================================================
# Task 5 — Write a report
# ============================================================
count = 0

with open(DATA / "names.txt", "r", encoding="utf-8") as file:
    for line in file:
        if line.strip():
            count += 1

with open(OUTPUT / "name_report.txt", "w", encoding="utf-8") as file:
    file.write(f"Names: {count}\n")


# ============================================================
# Task 6 — Append a log entry
# ============================================================
with open(OUTPUT / "activity.log", "a", encoding="utf-8") as file:
    file.write("Lab 08 completed\n")


# ============================================================
# Task 7 — Create without overwriting
# ============================================================
try:
    with open(OUTPUT / "first_run.txt", "x", encoding="utf-8") as file:
        file.write("First run")
except FileExistsError:
    print("first_run.txt already exists")


# ============================================================
# Task 8 — Handle a missing file
# ============================================================
try:
    with open(DATA / "missing.txt", "r", encoding="utf-8") as file:
        content = file.read()
        print(content)
except FileNotFoundError:
    print("Input file not found")


# ============================================================
# Task 9 — Filter names to a new file
# ============================================================
with open(DATA / "names.txt", "r", encoding="utf-8") as input_file:
    with open(OUTPUT / "a_names.txt", "w", encoding="utf-8") as output_file:
        for line in input_file:
            name = line.strip()

            if name and name[0].lower() == "a":
                output_file.write(name + "\n")


# ============================================================
# Task 10 — Average from a file
# ============================================================
scores = []

with open(DATA / "scores.txt", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if line:
            scores.append(int(line))

with open(OUTPUT / "average.txt", "w", encoding="utf-8") as file:
    if scores:
        average = sum(scores) / len(scores)
        file.write(f"Average: {average:.1f}\n")
    else:
        file.write("Average: 0.0\n")


# ============================================================
# Task 11 — Read a simple table
# ============================================================
with open(DATA / "students.csv", "r", encoding="utf-8") as file:
    for line in file:
        line = line.strip()

        if line:
            name, score = line.split(",")
            name = name.strip()
            score = int(score.strip())

            if score >= 80:
                print(name, score)


# ============================================================
# Task 12 — Save a word count
# ============================================================
with open(DATA / "note.txt", "r", encoding="utf-8") as file:
    text = file.read()

words = text.split()

with open(OUTPUT / "word_count.txt", "w", encoding="utf-8") as file:
    file.write(f"Words: {len(words)}\n")


# ============================================================
# Task 13 — BONUS: Clean nonblank lines
# ============================================================
with open(DATA / "names.txt", "r", encoding="utf-8") as input_file:
    with open(OUTPUT / "clean_names.txt", "w", encoding="utf-8") as output_file:
        for line in input_file:
            name = line.strip()

            if name:
                output_file.write(name + "\n")


# ============================================================
# Task 14 — BONUS: File and regex
# ============================================================
with open(DATA / "note.txt", "r", encoding="utf-8") as file:
    text = file.read()

numbers = re.findall(r"[0-9]+", text)

with open(OUTPUT / "numbers.txt", "w", encoding="utf-8") as file:
    for number in numbers:
        file.write(number + "\n")
