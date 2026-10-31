# Count Occurence of a value
# Count how many times a given value appears in a list, without using list.count()

numbers = [1, 3, 5, 4, 8, 2]
target = 2
count = 0

for n in numbers:
    if n == target:
        count += 1

print(target, "appears", count, "times")