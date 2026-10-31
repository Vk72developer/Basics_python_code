# Pangram check
# Check whether a sentence is pangram, meaning.
# it uses every letter of the English alphabet at least once. 

sentence = input("Enter a sentence: ").lower()

letters = set()
for ch in sentence:
    if ch.isalpha():
        letters.add(ch)

if len(letters) == 26:
    print("It is a pangram")

else:
    print("Not a pangram")