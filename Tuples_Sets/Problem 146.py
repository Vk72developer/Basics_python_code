# Min/Max in a Tuple of Tuples

scores = (("Amit", 92), ("Bela", 91), ("Chad", 77))

top = max(scores, key=lambda s: s[1])
low = min(scores, key=lambda s: s[1])

print("Highest:", top)
print("Lowest:", low)