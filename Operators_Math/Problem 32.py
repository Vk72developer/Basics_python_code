# Reverse of a number
# eg - 1234 = 4321

num = int(input("Enter a number: "))

rev = 0
n = num 
while n > 0:
    rev = rev * 10 + n % 10
    n //= 10

print(f"Reverse of a number {num} equal to : {rev}")