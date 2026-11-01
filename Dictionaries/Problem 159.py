# Dictionary Comprehension 

squares = {n: n * n for n in range(1, 6)}
print(squares)

even_squares = {n: n * n for n in range(1, 11) if n % 2 == 0}

print(even_squares)