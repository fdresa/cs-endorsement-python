# Lab 3: Privacy Tools
# Two small functions that protect student data, and tests that check them.


def check(actual, expected):
    """Provided tool: print PASS if actual matches expected, FAIL if it does not."""
    if actual == expected:
        print("PASS:", actual)
    else:
        print("FAIL: got", actual, "but expected", expected)


def is_valid_id(text):
    """Return True if text is a valid student ID, and False if it is not.

    A valid ID is exactly 7 characters long, and every character is a digit.
    Anything else is rejected, not repaired.
    """
    # YOUR CODE: replace the line below with the real check.
    return False


def mask(text):
    """Return text with every character but the last four replaced by *.

    Example: mask("4417730") returns "***7730".
    """
    # YOUR CODE: replace the line below with the real mask.
    return text


print("Testing is_valid_id")
check(is_valid_id("4417730"), True)
check(is_valid_id("441773"), False)      # too short
check(is_valid_id("44177301"), False)    # too long
check(is_valid_id("44A7730"), False)     # contains a letter
check(is_valid_id(" 4417730"), False)    # a space in front
check(is_valid_id(""), False)            # empty
print()

print("Testing mask")
check(mask("4417730"), "***7730")
check(mask("912-555-0142"), "********0142")
# YOUR CODE: add your two tests below this line.
