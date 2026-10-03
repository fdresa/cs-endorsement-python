# Lab 2: Password Strength Checker
# Rates a practice password as Weak, Fair, or Strong. Never type a real password here.

common = ["password", "123456", "123456789", "qwerty", "letmein",
          "iloveyou", "admin", "welcome", "password1", "abc123"]

# Input validation: keep asking until something is typed
password = input("Practice password (never a real one): ")
while password == "":
    print("Nothing was entered. Try again.")
    password = input("Practice password (never a real one): ")

# Count each kind of character, one character at a time
uppercase = 0
lowercase = 0
digits = 0
symbols = 0
for ch in password:
    if ch.isupper():
        uppercase = uppercase + 1
    elif ch.islower():
        lowercase = lowercase + 1
    # YOUR CODE: add an elif that counts digits
    # YOUR CODE: add an else that counts everything left as a symbol

# How many of the four kinds appear at least once (0 to 4)
kinds = 0
if uppercase > 0:
    kinds = kinds + 1
if lowercase > 0:
    kinds = kinds + 1
if digits > 0:
    kinds = kinds + 1
if symbols > 0:
    kinds = kinds + 1

# The rating rules, checked in order. The first rule that matches wins.
length = len(password)
if password.lower() in common:
    rating = "Weak (on the common-password list)"
elif length >= 16:
    rating = "Strong"
elif length >= 12 and kinds >= 2:
    rating = "Strong"
# YOUR CODE: add the Fair rule here (at least 8 characters and at least 3 kinds)
else:
    rating = "Weak"

print()
print("Length:", length)
print("Uppercase:", uppercase, "| Lowercase:", lowercase, "| Digits:", digits, "| Symbols:", symbols)
print("Kinds of characters:", kinds)
print("Rating:", rating)
