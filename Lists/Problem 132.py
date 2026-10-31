# Find the Missing Number 

numbers = [1, 2, 4, 5, 6]

n = 6 
expected = n * (n + 1) // 2
actual = sum(numbers)

print("missing number:", expected - actual)