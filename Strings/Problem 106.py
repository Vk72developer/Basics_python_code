# Reverse the word order

sentence = input("Enter a sentence: ")
words = sentence.split()

rev_words = words[:: -1]
print(" ".join(rev_words))