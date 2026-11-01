# Subset and Superset checks

small = {1, 2}
big = {1, 2, 3, 4}

print(small.issubset(big))

print(big.issuperset(small))
print(small <= big)
print(big < big)
