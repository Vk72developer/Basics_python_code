# Acronym Generator 
# Build acronym from a phrase by taking the first letter of each word in uppercase.


phrase = input("Enter a phrase: ")
acronym = ""

for word in phrase.split():
    acronym += word[0].upper()
print("Acronym:", acronym)