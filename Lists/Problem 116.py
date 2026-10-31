# Maximum Without max() 

numbers = [12, 45, 2, 67, 33]
largest = numbers[0]

for n in numbers:
    if n > largest:
        largest = n 
print("Largest: ", largest)