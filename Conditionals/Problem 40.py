# Vowel or Consonant

ch = input("Enter a letter: ")

if ch.lower() in "aeiou": #lower() makes the check case-insensitive
    print(ch, "is a Vowel")
else:
    print(ch, "is a Consonant")