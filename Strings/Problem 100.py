# Replace a substring without replace()

text = "the cat sat on the cat mat"
old = "cat"
new = "dog"
result = ""

i = 0
while i < len(text):
    if text[i:i + len(old)] == old:
        result += new
        i += len(old) 
    else:
        result += text[i]
        i += 1 

print(result)