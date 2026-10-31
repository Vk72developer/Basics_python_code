# Insert into a Sorted List 

numbers = [2, 5, 8, 12]
value = 7
position = len(numbers)

for i in range(len(numbers)):
    if numbers[i] > value:
        position = i 
        break 

numbers.insert(position, value)
print("After insert:", numbers)