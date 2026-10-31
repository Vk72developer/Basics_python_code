# Linear Search 

# search for a target value in a list and print the index of its first
# occurence, or -1. if it is not present 

numbers = [4, 6, 8, 9, 5]
target = 9
index = -1

for i in range(len(numbers)):
    if numbers[i] == target:
        index = i
        break 

print("Index of", target, ":", index)