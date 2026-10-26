# Collatz sequence 

n = int(input("Enter a number: "))

steps = 0
while n != 1:
    print(n, end="")
    if n % 2 == 0:
        n //= 2
    else:
        n = 3 * n + 1
    steps += 1

print(1)
print(f"Steps taken: {steps}")