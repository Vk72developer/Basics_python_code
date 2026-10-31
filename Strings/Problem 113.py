# Caesar Clipher

text = input("Enter a message: ")
shift = int(input("Enter shift: "))
result = ""
for ch in text:
    if ch.isupper():
        result += chr((ord(ch) - ord("A") + shift) % 26 + ord("A"))
    elif ch.islower():
        result += chr((ord(ch) - ord("a") + shift) % 26 + ord("a"))
    else:
        result += ch 

print("Encrypted:", result)