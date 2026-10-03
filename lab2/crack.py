# Lab 2: Cracking a Caesar Cipher
# A Caesar cipher has only 25 useful keys, so a program can try every one and a person can spot the readable line.

secret = "Ehpyej-qtgp vpjd lcp yze pyzfrs ez vppa l dpncpe."

# YOUR CODE: this tries only shift 1. Change the range so it tries every shift from 1 to 25.
for shift in range(1, 2):
    result = ""
    for ch in secret:
        if ch.isupper():
            position = ord(ch) - 65
            position = (position - shift) % 26    # shift back to undo the cipher
            result = result + chr(position + 65)
        elif ch.islower():
            position = ord(ch) - 97
            position = (position - shift) % 26
            result = result + chr(position + 97)
        else:
            result = result + ch
    print(shift, result)
