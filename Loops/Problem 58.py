# Count Digits in a Number
# Read a positive integer and count how many digits . Using a while loop

n = int(input("Enter a number :" ))

temp = n
count = 0

while temp > 0:
    temp //= 10
    count += 1 

print(f"{n} has {count} digits")

