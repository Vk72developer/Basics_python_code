# Sum of digits 

n = int(input("Enter an N: "))

temp = n 
sum = 0

while temp > 0:
    sum += temp % 10
    temp //= 10

print(f"Sum of digits {n} is {sum}")