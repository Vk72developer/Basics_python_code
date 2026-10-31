# Move Zeros to the End 

numbers = [0, 1, 0, 3, 12]
non_zero = [n for n in numbers if n != 0]

zero_count = len(numbers) - len(non_zero)
result = non_zero + [0] * zero_count 
print("Result:", result)