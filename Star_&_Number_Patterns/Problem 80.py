# Alphabet Pattern 
# ex-: (A, AB, ABC...)

rows = 5
for i in range(rows):
    for j in range(i + 1):
        print(chr(ord("A") + j), end="")

    print()