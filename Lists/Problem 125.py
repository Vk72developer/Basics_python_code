# Remove Duplicates (Keep Order)

num = [1, 3, 5, 7, 9]
unique = []
for n in num:
    if n not in unique:
        unique.append(n)

print("unique:", unique)