# Sort Without sort() (Bubble Sort )

numbers = [64, 34, 12, 22, 11, 90]
n = len(numbers)
for i in range(n - 1):
    for j in range(n - 1 - i):
        if numbers[j] > numbers[j + 1]:
            numbers[j], numbers[j + 1] = numbers[j + 1], numbers[j]

print("Sorted:", numbers)