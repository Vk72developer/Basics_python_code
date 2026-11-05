# List Comprehension: Squares and Evens

squares = [n ** 2 for n in range(1, 11)]

evens = [n for n in range(1, 11) if n % 2 == 0]

print("Squares:", squares)
print("Evens:", evens)