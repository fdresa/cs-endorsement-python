# Lab 5: Data Structures and Protection
# Loads a fictional class roster, summarizes it, and saves a de-identified copy to share.

import csv
from pathlib import Path

FOLDER = Path(__file__).parent   # the lab5 folder, wherever you run the program from


# Provided tools: you call these, you don't write them.

def load_roster(filename):
    """Read a CSV file from the lab5 folder and return a list of dictionaries, one per row."""
    with open(FOLDER / filename, newline="") as file:
        return list(csv.DictReader(file))


def save_roster(rows, filename):
    """Write a list of dictionaries to a CSV file in the lab5 folder. The first row's keys become the column headers."""
    with open(FOLDER / filename, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=list(rows[0].keys()))
        writer.writeheader()
        writer.writerows(rows)


def group_sizes(rows, field):
    """Count how many rows share each value of one field. A count of 1 can point to a single student."""
    counts = {}
    for row in rows:
        value = row.get(field, "(not in file)")
        counts[value] = counts.get(value, 0) + 1
    return counts


# Part 1: one list, eight dictionaries

roster = load_roster("roster_full.csv")
print("Students on the roster:", len(roster))
print("First record:", roster[0])
print("First student's score:", roster[0]["score"])
print()

# Part 2: one line per student, the class average, and the highest score

scores = []
for student in roster:
    score = int(student["score"])   # values read from a file arrive as text
    scores.append(score)
    print(student["name"], score)

print("Class average:", round(sum(scores) / len(scores), 1))

highest = 0
top_name = ""
for student in roster:
    score = int(student["score"])
    # YOUR CODE: if this score is higher than highest, store it in highest
    # and store the student's name in top_name.

print("Highest score:", highest, top_name)
print()


# Part 3: a de-identified copy to share

def deidentify(roster):
    """Return a new roster that is safe to share: a code in place of each name, and only the fields the reader needs."""
    shared = []
    number = 1
    for student in roster:
        record = {}
        record["code"] = "S" + str(number)   # S1, S2, S3, ...
        # YOUR CODE: copy over only the fields the reader needs, for example
        # record["score"] = student["score"]
        shared.append(record)
        number = number + 1
    return shared


shared = deidentify(roster)
save_roster(shared, "roster_shared.csv")
print("Saved roster_shared.csv with", len(shared), "students")
print("First shared record:", shared[0])
print("Group sizes by grade level in the shared file:", group_sizes(shared, "grade_level"))
