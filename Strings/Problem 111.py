# Count Substring Occurences (Overlapping)

text = "aaaa"
sub = "aa"
count = 0

for i in range(len(text) - len(sub) + 1):
    if text[i:i + len(sub)] == sub:
        count += 1

print("Occurences: ", count)