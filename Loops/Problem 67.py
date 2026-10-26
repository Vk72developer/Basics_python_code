# Perfect Number

n = int(input("Enter a number: "))

div_sum = 0
for i in range(1, n):
    if n % i == 0:
        div_sum += i 

if div_sum == n:
    print(f"{n} is a perfect number ")
else:
    print(f"{n} is not a perfect number ")