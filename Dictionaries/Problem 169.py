# Group items by key 

words = ["apple", "banana", "avocado", "cherry", "blueberry"]

groups = {}

for word in words:
    first = word[0]
    groups.setdefault(first, []).append(word)

print(groups)

