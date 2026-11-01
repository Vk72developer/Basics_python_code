# collections.Counter

from collections import Counter

letters = Counter("mississippi")

print(letters)
print(letters.most_common(2))

print(letters["s"])
