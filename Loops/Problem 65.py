# Primes in a range 

low = int(input("Enter low: "))
high = int(input("Enter high: "))

for n in range(max(low, 2), high + 1):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            break 

    else:
            print(n, end=" ")

print()
    