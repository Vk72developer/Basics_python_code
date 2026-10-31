# Union Of two Lists

a = [1, 2, 3, 4]
b = [3, 4, 5, 6]

union = []
for x in a + b:
    if x not in union:
        union.append(x)

print("union:", union)