# Rotate a List by k

numbers = [1, 2, 3, 4, 5]
k = 2
k = k % len(numbers) 
rotated = numbers[-k:] + numbers[:-k]

print("Rotated:", rotated)