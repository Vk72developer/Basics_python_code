# Digit, Alphabet or Special Character

ch = input("Enter a character: ")

if ch.isdigit():
    print(ch, "is a Digit")
elif ch.isalpha():
    print(ch, "is an Alphabet letter")
else:
    print(ch, "is a special Character")