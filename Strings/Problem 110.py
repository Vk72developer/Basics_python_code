# Remove Punctuation 
# Remove all punctuation from a string, keeping only letters, digits and spaces

text = input("Enter a string: ")
result  = ""
for ch in text:
    if ch.isalnum() or ch == " ":
        result += ch 
print("Cleaned: ", result)