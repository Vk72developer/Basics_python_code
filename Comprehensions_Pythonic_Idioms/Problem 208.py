# Nested Comprehension: Flatten a Matrix 

matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]
          ]

flat = [value for row in matrix for value in row]
print(flat)