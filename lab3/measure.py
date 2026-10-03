# Lab 3: Measure, as a Function
# Lab 1's scenario block, written once as a function and called once per password.

guesses_per_second = 10_000_000_000   # the course's fixed attack speed: 10 billion guesses a second


def possible_passwords(characters, length):
    return characters ** length


def measure(label, characters, length):
    """Print how many passwords a rule allows and how long trying them all would take.

    label: a short name for the scenario, printed first
    characters: the choices for each position (26 letters, 94 keys, or 7,776 words)
    length: the number of positions
    """
    possible = possible_passwords(characters, length)
    seconds = possible / guesses_per_second
    days = seconds / 86400                # 86,400 seconds in a day
    years = days / 365
    over_a_year = years >= 1              # True or False

    # YOUR CODE: copy the seven print lines from lab1/password_math.py and paste them here.
    # Indent each one four spaces so it sits inside the function.


measure("A: 8 lowercase letters", 26, 8)
# YOUR CODE: add three more calls below this line, one each for scenarios B, C, and D from Lab 1.
