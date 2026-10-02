# Lab 1: Password Math
# How many passwords are possible, and how long would it take to try every one?

guesses_per_second = 10_000_000_000   # the course's fixed attack speed: 10 billion guesses a second

# Scenario A: 8 characters, lowercase letters only
label = "A: 8 lowercase letters"
characters = 26        # choices for each position
length = 8             # number of positions

possible = characters ** length       # ** means "to the power of"
seconds = possible / guesses_per_second
days = seconds / 86400                # 86,400 seconds in a day
years = days / 365
over_a_year = years >= 1              # True or False

print(label)
print("Possible passwords:", f"{possible:,}")
print("Seconds to try them all:", round(seconds))
print("Days to try them all:", round(days, 1))
print("Years to try them all:", round(years, 1))
print("More than a year?", over_a_year)
print()
