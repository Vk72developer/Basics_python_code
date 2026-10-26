# Pallindrome Number 

n = int(input("Enter a number: "))

temp = n
rev_num = 0
while temp > 0:
    rev_num = rev_num * 10 + temp % 10
    temp //= 10

if rev_num == n:
    print(f"{n} is a pallindrome")
else:
    print(f"{n} is not a pallindrome")