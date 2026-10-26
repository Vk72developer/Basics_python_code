# Prime Number Check 

n = int(input("Enter a number: "))

is_prime = n > 1
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        is_prime = False 
        break 

if is_prime:
    print(f"{n} is prime")
else:
    print(f"{n} is not prime")