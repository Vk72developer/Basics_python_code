# Minimum Without min()

numbers  = [12, 45, 3, 67, 87]
smallest = numbers[0]

for n in numbers:
    if n < smallest:
        smallest = n 

print("Smallest:", smallest) 