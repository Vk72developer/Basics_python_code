# Capitalize Each word without title()

sentence = input("Enter a sentence: ")
words = sentence.split()
capitalize = []

for word in words:
    capitalize.append(word[0].upper() + word[1:])

print(" ".join(capitalize))