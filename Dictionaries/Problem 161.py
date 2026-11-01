# Word Frequency Counter

text = "to be or not to be"
freq = {}

for word in text.split():
    freq[word] = freq.get(word, 0) + 1

print(freq)