# Remove All Occurrences of a Value

numbers = [1, 2, 3, 2, 4, 2]
value = 2
result = [n for n in numbers if n != value]

print("After removal:", result)