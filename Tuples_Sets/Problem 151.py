# Unique words in a sentence

sentence = "the cat and the dog chased the cat"

words = set(sentence.lower().split())

print("Unique words:", sorted(words))
print("count:", len(words))