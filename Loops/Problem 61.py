# Reverse of a Number 

n = int(input("Eneter a number: "))

temp = n
rev_num = 0 
while temp > 0:
    rev_num = rev_num * 10 + temp % 10
    temp //= 10

print(f"Reverse of {n} is {rev_num}")