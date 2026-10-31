# Find Duplicate elements

numbers = [1, 2, 3, 2, 4, 1, 5]
seen = set()
duplicates = []

for n in numbers:
    if n in seen and n not in duplicates:
        duplicates.append(n)
    seen.add(n)

print("Duplicates:", duplicates)