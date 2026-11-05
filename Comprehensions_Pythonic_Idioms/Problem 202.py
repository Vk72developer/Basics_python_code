# Set Comprehension 

words = ["Apple", "banana", "Avocado", "cherry", "Blueberry"]

first_letters = {word[0].lower() for word in words} 

print(first_letters)
print("Count of unique first letters:", len(first_letters))
