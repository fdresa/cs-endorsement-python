# Lab 2: Caesar Cipher
# Shifts every letter of a message the same number of places. Spaces and punctuation stay as they are.

message = "Meet me in the library after sixth period."
shift = 3

result = ""
for ch in message:
    if ch.isupper():
        position = ord(ch) - 65                # A is 65, so A becomes 0, B becomes 1, and so on
        position = (position + shift) % 26    # move along the alphabet, wrapping past Z back to A
        result = result + chr(position + 65)
    elif ch.islower():
        position = ord(ch) - 97                # a is 97
        position = (position + shift) % 26
        result = result + chr(position + 97)
    else:
        result = result + ch                   # not a letter: copy it unchanged

print("Shift: ", shift)
print("Before:", message)
print("After: ", result)
