# Count Digits in a number
# eg -> 1234 
# count = 4

num = int(input("Enter a number: "))

n = num 
count = 0
while n > 0:
    count += 1
    n //= 10

print(num, "has", count, "digits")