# Sum of Digits 
# eg- 4 + 5 + 7 + 8 = 24 

num = int(input("Enter a number: "))

total = 0
n = num 
while n > 0:
    total += n % 10 #gives last digit 
    n //= 10

print(f"sum of digit {num} = {total}" )