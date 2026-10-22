# Factorial of a Number

# 1 * 2 * 3 * ....... * N

n = int(input("Enter a number: "))

fact = 1
for i in range(1, n + 1):
    fact *= i 

print(f"{n}! = {fact}")