# Pascal's Triangle

n = 5
for i in range(n):
    val = 1
    row = []
    for j in range(i + 1):
        row.append(str(val))
        val = val * (i - j) // (j + 1)

    print(" ".join(row).center(2 * n - 1))