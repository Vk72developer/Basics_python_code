# Merge Two Sorted Lists

a = [1, 3, 5]
b = [2, 4, 6, 8]

merged = []
i = 0
j = 0
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        merged.append(a[i])
        i += 1
    else:
        merged.append(b[j])
        j += 1

merged.extend(a[i:])
merged.extend(b[j:])
print("Merged:", merged)