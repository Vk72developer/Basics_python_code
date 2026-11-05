# Dict Comprehension 

words = ["python", "is", "fun", "to", "learn"]

lengths = {word: len(word) for word in words}

print(lengths)

long_words = {word: len(word) for word in words if len(word) > 2}
print(long_words)