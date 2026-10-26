# Armstrong Number 

n = int(input("Enter a 3-digit number: "))

temp = n 
total = 0
while temp > 0:
    digit = temp % 10
    total += digit ** 3 
    temp //= 10 

if total == n:
    print(f"{n} is an Armstrong number ")
else:
    print(f"{n} is not an Armstrong number ")