# Decimal to Binary 

n = int(input("Enter a decimal number: "))

temp = n
binary = ""
while temp > 0:
    binary = str(temp % 2) + binary 
    temp //= 2 

print(f"Binary of {n} is {binary}")
