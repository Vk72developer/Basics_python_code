# Comprehension with if-else

numbers = [4, -2, 7, -9, 0, 3, -3]

cleaned = [n if n >= 0 else 0 for n in  numbers]

print("Original:", numbers)
print("Cleaned:", cleaned)