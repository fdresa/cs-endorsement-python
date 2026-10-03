# Lab 6: Attendance Report
# Prints one class's attendance for the week. Student names appear only after the staff password.
# Four problems are planted in this file. The Lab 6 page walks you through finding each one.

import os

ADMIN_PASSWORD = "lakeside-admin"

days_in_week = 5

# Days present this week for each student (fictional students)
attendance = {
    "Ava Reyes": 5,
    "Ben Okafor": 4,
    "Cara Lindqvist": 5,
    "Dev Patel": 2,
    "Elena Brooks": 3,
    "Felix Moreau": 5,
}

# Add up every student's days present
for name in attendance:
    total_present = 0
    total_present = total_present + attendance[name]

average = total_present / len(attendance)

print("Class attendance report")
print("Students:", len(attendance))
print("Average days present: " + round(average, 1) + " of " + str(days_in_week))
print()

password = input("Staff password for the full report: ")

if password == ADMIN_PASSWORD
    for name in attendance:
        print(name, "was present", attendance[name], "of", days_in_week, "days")
else:
    print("Full report hidden. Totals only.")
