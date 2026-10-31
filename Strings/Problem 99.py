# Check substring without using in 

text = "Programming"
sub = "gram"
found = -1 

for i in range(len(text) - len(sub) + 1):
    if text[i:i + len(sub)] == sub:
        found = 1
        break 

if found == -1:
    print("Substring not found")
else:
    print("Found at index", found)