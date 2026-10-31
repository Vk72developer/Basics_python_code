# Swap case without swapcase()

text = input("Enter a string: ")

result = ""
for ch in text:
    if ch.isupper():
        result += ch.lower()
    elif ch.islower():
        result += ch.upper()
    else:
        result += ch 

print("Swapped:", result)